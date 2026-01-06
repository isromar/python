# main.py (menú principal)
import sys
from digit_fifth_powers.main import DigitosPotencias

def main_menu():
    while True:
        print("\n📚 Menú de problemas de Euler")
        print("30. Digit Fifth Powers")
        # Puedes añadir más opciones aquí
        print("2. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "30":
            DigitosPotencias.main()  # llama al método main de la clase
        elif opcion == "2":
            print("¡Hasta luego!")
            sys.exit()
        else:
            print("❌ Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main_menu()

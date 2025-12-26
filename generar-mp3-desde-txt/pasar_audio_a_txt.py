import speech_recognition as sr
from pydub import AudioSegment
import os
from pydub.utils import which
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph

#AudioSegment.converter = which("C:\\Programas\\ffmpeg-7.0.2-full_build\\bin\\ffmpeg.exe")
#AudioSegment.ffmpeg = which("C:\\Programas\\ffmpeg-7.0.2-full_build\\bin\\ffmpeg.exe")
#AudioSegment.ffprobe = which("C:\\Programas\\ffmpeg-7.0.2-full_build\\bin\\ffprobe.exe")


# Configuración de FFmpeg (mantén esta parte igual)
AudioSegment.converter = r"C:\Program Files\ffmpeg-7.0.2-full_build\bin"
AudioSegment.ffmpeg = r"C:\Program Files\ffmpeg-7.0.2-full_build\bin"
AudioSegment.ffprobe = r"C:\Program Files\ffmpeg-7.0.2-full_build\bin"

def mp3_a_wav(archivo_mp3, archivo_wav):
    """Convierte un archivo MP3 a WAV."""
    audio = AudioSegment.from_mp3(archivo_mp3)
    audio.export(archivo_wav, format="wav")

def transcribir_audio(archivo_wav):
    """Transcribe un archivo de audio WAV a texto."""
    reconocedor = sr.Recognizer()
    with sr.AudioFile(archivo_wav) as fuente:
        audio = reconocedor.record(fuente)

    try:
        texto = reconocedor.recognize_google(audio, language="es-ES")
        return texto
    except sr.UnknownValueError:
        return "No se pudo entender el audio"
    except sr.RequestError as e:
        return f"Error en la solicitud al servicio de reconocimiento de voz: {e}"

def crear_pdf(texto, archivo_pdf):
    """Crea un archivo PDF con el texto transcrito."""
    # Registrar una fuente que soporte caracteres españoles
    pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))
    
    # Crear el documento
    doc = SimpleDocTemplate(archivo_pdf, pagesize=letter,
                            rightMargin=72, leftMargin=72,
                            topMargin=72, bottomMargin=18)
    
    # Estilos
    styles = getSampleStyleSheet()
    style = styles["Normal"]
    style.fontName = "Arial"
    
    # Crear los párrafos
    story = []
    for parrafo in texto.split('\n'):
        p = Paragraph(parrafo, style)
        story.append(p)
    
    # Construir el PDF
    doc.build(story)

def main():
    archivo_entrada = input("Ingrese el nombre del archivo de audio (con extensión .mp3 o .wav): ")
    nombre_base, extension = os.path.splitext(archivo_entrada)
    archivo_wav = "temporal.wav"
    archivo_txt = f"{nombre_base}_transcripcion.txt"
    archivo_pdf = f"{nombre_base}_transcripcion.pdf"

    if extension.lower() == '.mp3':
        print("Convirtiendo MP3 a WAV...")
        mp3_a_wav(archivo_entrada, archivo_wav)
    elif extension.lower() == '.wav':
        archivo_wav = archivo_entrada
    else:
        print("Formato de archivo no soportado. Por favor, use .mp3 o .wav")
        return

    print("Transcribiendo el audio...")
    texto_transcrito = transcribir_audio(archivo_wav)

    # Guardar la transcripción en un archivo de texto
    with open(archivo_txt, "w", encoding="utf-8") as archivo:
        archivo.write(texto_transcrito)

    # Crear el archivo PDF
    crear_pdf(texto_transcrito, archivo_pdf)

    print(f"Transcripción completada y guardada en {archivo_txt} y {archivo_pdf}")

    # Eliminar el archivo WAV temporal si se creó
    if extension.lower() == '.mp3':
        os.remove(archivo_wav)

if __name__ == "__main__":
    main()
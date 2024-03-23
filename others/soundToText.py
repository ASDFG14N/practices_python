import speech_recognition as sr
import newReplace as nr


class Elisa():
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def __sound_to_text(self):
        with sr.Microphone() as origen:
            self.recognizer.pause_threshold = 1
            print("Escuchando...")
            self.recognizer.adjust_for_ambient_noise(origen)
            audio = self.recognizer.listen(origen)
        try:
            print("Convirtiendo audio a texto")
            text = self.recognizer.recognize_google(audio, language='es-PER')
            print(f"Texto antes: {text}")
            print("Reemplazando signos de puntuación")
            texto = self.__modificarText(texto=text)
            print("Texto modificado existosamanete")
            #self.__write_text(text=text)
            print("Ya puedes abrir el archivo")
            return texto.lower()
        except sr.UnknownValueError:
            print("No se pudo entender el audio. Volver a intentarlo.")
            return "Escuchando..."
        except sr.RequestError as e:
            print(f"No se pudo obtener respuesta del servicio de reconocimiento: {e}")
            return "Error en el servicio de reconocimiento."

    def __modificarText(self, texto):
        a = nr.replaceNew(texto=texto)
        diccionarioPunt = {'signo de interrogación de apertura': '¿',
                           'signo de interrogación de cierre': '?',
                           'signo de exclamación de cierre': '!',
                           'signo de exclamación de apertura': '¡',
                           'parentesis de apertura': '(',
                           'parentesis de cierre': ')',
                           'llave de apertura': '{',
                           'llave de cierre': '}',
                           'punto y coma': ';',
                           'dos puntos': ':',
                           'comillas': '"',
                           'coma': ',',
                           'punto': '.'
                           }
        for palabra, signo in diccionarioPunt.items():
            texto = a.reemplazarDerecha(palabra, signo)
        return texto
    
    def __write_text(self, text):
        with open(r"C:\Users\Gian\Desktop\ProgramPython\Otros Adicional\text.txt", "a", encoding="utf-8") as file:
            file.write(text)
        print("Archivo generado")

    
    def start(self):
        active = True
        while active:
            result = self.__sound_to_text()
            print(f"Texto despues: {result}")
            # Agrega lógica para determinar cuándo salir del bucle
            if result == "salir":
                active = False

elisa = Elisa()
elisa.start()




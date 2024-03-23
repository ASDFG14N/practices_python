#La biblioteca unittest verifica si nuestro programa hace lo que nosotros esperamos que haga
import unittest
import cambiaTexto

#creamos una clase nueva que herede unittest
class probarCambiaTexto(unittest.TestCase):
    #siempre debe iniciar con la palabra text
    def test_mayusculas(self):
        palabra = "hola mundo"
        resultado = cambiaTexto.todoMayuscula(palabra)
        self.assertEqual(resultado, "HOLA MUNDO")
if __name__ == "__main__":
    unittest.main()
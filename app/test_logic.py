import unittest

# Importamos la función de nuestro archivo main
from main import obtener_mensaje_html


class TestWebLogic(unittest.TestCase):
    def test_contenido_no_es_vacio(self):
        """Prueba 1: El sitio no debe estar vacío"""
        respuesta = obtener_mensaje_html()
        self.assertTrue(len(respuesta) > 0, "El HTML está vacío, algo anda mal")

    def test_codificacion_correcta(self):
        """Prueba 2: Debe ser bytes (no string plano) para que HTTP lo acepte"""
        respuesta = obtener_mensaje_html()
        self.assertIsInstance(
            respuesta, bytes, "El output debe estar en bytes (UTF-8 encoded)"
        )

    def test_palabras_clave(self):
        """Prueba 3: Debe mencionar 'Versión' o 'Jenkins'"""
        respuesta_str = obtener_mensaje_html().decode("utf-8")
        # Si alguien borra la palabra "Versión", el test fallará y bloqueará el deploy
        self.assertIn("Versión", respuesta_str)


if __name__ == "__main__":
    unittest.main()

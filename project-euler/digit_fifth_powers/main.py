"""
DigitosPotencias - Números iguales a la suma de potencias de sus dígitos

Este programa permite calcular todos los números que son iguales a la
suma de sus dígitos elevados a una potencia determinada por el usuario.

Ejemplo: para potencia = 4, 1634 es válido porque 1^4 + 6^4 + 3^4 + 4^4 = 1634

Características:
- Clase 'DigitosPotencias' que encapsula la lógica de cálculo.
- Validación de entrada del usuario (potencias entre 3 y 6).
- Calcula el máximo número a revisar automáticamente.
- Muestra los números encontrados y su suma total.

Autor: Isabel Rodenas
Fecha: 2026-01-06
"""


class DigitosPotencias:
    """Plantilla generica para proyectos Python con clases."""

    def __init__(self, potencia):
        self.nombre = "DigitosPotencias"
        self.potencia = potencia
        self.resultados = []

    def calcular_numero_maximo(self):
        n = 1
        while n * (9**self.potencia) >= 10 ** (n - 1):
            n += 1
        return (n - 1) * (9**self.potencia)

    def es_valido(self, numero):
        separar_cifras = [int(d) for d in str(numero)]
        suma = sum(d**self.potencia for d in separar_cifras)
        return suma == numero

    def buscar_numeros(self):
        minimo = 2
        maximo = self.calcular_numero_maximo()
        for numero in range(minimo, maximo + 1):
            if self.es_valido(numero):
                self.resultados.append(numero)

    def calcular_suma_numeros_validos(self):
        return sum(self.resultados)

    def mostrar_resultados(self):
        print(f"Resultado: {self.resultados}")
        print(f"Suma: {self.calcular_suma_numeros_validos()}")

    def main():
        print("🚀 Iniciando DigitosPotencias")
        print("=" * 40)

        while True:
            potencia_usuario = input(
                "Introduce la potencia que quieres usar (entre 3 y 6): "
            )

            try:
                potencia = int(potencia_usuario)
            except ValueError:
                print("Ingresa un número")
                continue

            if potencia > 6 or potencia < 3:
                print("Introduce un número entre 3 y 6")
                continue
            else:
                break

        app = DigitosPotencias(potencia)
        app.buscar_numeros()
        app.mostrar_resultados()
        print("\n✨ ¡Ejecucion completada!")


if __name__ == "__main__":
    DigitosPotencias.main()

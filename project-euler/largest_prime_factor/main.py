"""
MayorFactorPrimo - Calcula el mayor factor primo de un número

Este programa calcula el mayor factor primo de un número dado.

Ejemplo: para number = 600851475143, el mayor factor primo es 6857.

Características:
- Clase 'MayorFactorPrimo' que encapsula la lógica de cálculo.
- Método para encontrar el mayor factor primo.
- Muestra el resultado.

Autor: Isabel Rodenas
Fecha: 2026-01-10
"""

class MayorFactorPrimo:
    """Clase para calcular el mayor factor primo de un número."""

    def __init__(self, number):
        self.number = number
        self.mayor_factor = None

    def calcular_mayor_factor_primo(self):
        """Calcula el mayor factor primo del número."""
        divisor = self.number
        i = 1
        while i <= divisor:
            i += 1
            if divisor % i == 0:
                divisor = divisor // i
        self.mayor_factor = i

    def mostrar_resultado(self):
        print(f"El mayor factor primo de {self.number} es: {self.mayor_factor}")
        print(f"The largest prime factor of {self.number} is: {self.mayor_factor}")

    @staticmethod
    def main():
        print("🚀 Iniciando MayorFactorPrimo")
        print("=" * 40)

        while True:
            try:
                numero_usuario = int(input("Introduce el número para calcular su mayor factor primo: "))
            except ValueError:
                print("Por favor, introduce un número válido")
                continue

            if numero_usuario <= 1:
                print("Introduce un número mayor que 1")
                continue
            else:
                break

        app = MayorFactorPrimo(numero_usuario)
        app.calcular_mayor_factor_primo()
        app.mostrar_resultado()
        print("\n✨ ¡Ejecución completada!")


if __name__ == "__main__":
    MayorFactorPrimo.main()

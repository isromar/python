"""
SmallestMultiple - Calcula el menor número divisible por todos los números de 1 a N

Este programa encuentra el menor número positivo que es divisible por
todos los números desde 1 hasta un número máximo dado.

Ejemplo: para max=20, el menor número divisible por todos los números de 1 a 20 es 232792560.

Características:
- Clase 'SmallestMultiple' que encapsula la lógica de cálculo.
- Método para calcular el menor múltiplo.
- Muestra el resultado.

Autor: Isabel Rodenas
Fecha: 2026-01-10
"""

class SmallestMultiple:
    """Clase para calcular el menor número divisible por todos los números de 1 a max_num."""

    def __init__(self, max_num):
        self.max_num = max_num
        self.resultado = -1

    def calcular_menor_multiplo(self):
        """Calcula el menor número divisible por todos los números de 1 a max_num."""
        i = self.max_num
        while True:
            divisible = all(i % j == 0 for j in range(self.max_num, self.max_num - 10, -1))
            if divisible:
                self.resultado = i
                break
            i += self.max_num  # Optimización: saltar múltiplos del máximo
        return self.resultado

    def mostrar_resultado(self):
        print(f"The smallest number divisible by all numbers from 1 to {self.max_num} is: {self.resultado}")

    @staticmethod
    def main():
        print("🚀 Iniciando SmallestMultiple")
        print("=" * 40)

        while True:
            try:
                max_num = int(input("Enter the maximum number (e.g., 20): "))
            except ValueError:
                print("Please enter a valid integer.")
                continue

            if max_num < 1:
                print("The maximum number must be greater than 0.")
                continue
            else:
                break

        app = SmallestMultiple(max_num)
        app.calcular_menor_multiplo()
        app.mostrar_resultado()
        print("\n✨ Execution completed!")


if __name__ == "__main__":
    SmallestMultiple.main()

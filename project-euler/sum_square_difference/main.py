"""
SumSquareDifference - Calcula la diferencia entre el cuadrado de la suma
y la suma de los cuadrados de los primeros N números naturales.

Ejemplo: para max=100, la diferencia es 25164150.

Características:
- Clase 'SumSquareDifference' que encapsula la lógica de cálculo.
- Métodos para calcular la suma de cuadrados, el cuadrado de la suma y la diferencia.
- Muestra el resultado.

Autor: Isabel Rodenas
Fecha: 2026-01-10
"""

class SumSquareDifference:
    """Clase para calcular la diferencia entre el cuadrado de la suma y la suma de cuadrados."""

    def __init__(self, max_num):
        self.max_num = max_num
        self.sum_of_squares = 0
        self.square_of_sum = 0
        self.difference = 0

    def calcular_suma_cuadrados(self):
        """Calcula la suma de los cuadrados de los primeros max_num números."""
        self.sum_of_squares = sum(i**2 for i in range(1, self.max_num + 1))

    def calcular_cuadrado_suma(self):
        """Calcula el cuadrado de la suma de los primeros max_num números."""
        self.square_of_sum = sum(range(1, self.max_num + 1))**2

    def calcular_diferencia(self):
        """Calcula la diferencia entre cuadrado de la suma y suma de cuadrados."""
        self.calcular_suma_cuadrados()
        self.calcular_cuadrado_suma()
        self.difference = self.square_of_sum - self.sum_of_squares

    def mostrar_resultado(self):
        print(f"Difference between the square of the sum and sum of squares of first {self.max_num} numbers: {self.difference}")

    @staticmethod
    def main():
        print("🚀 Iniciando SumSquareDifference")
        print("=" * 40)

        while True:
            try:
                max_num = int(input("Enter the maximum number (e.g., 100): "))
            except ValueError:
                print("Please enter a valid integer.")
                continue

            if max_num <= 0:
                print("Number must be greater than 0.")
                continue
            else:
                break

        app = SumSquareDifference(max_num)
        app.calcular_diferencia()
        app.mostrar_resultado()
        print("\n✨ Execution completed!")


if __name__ == "__main__":
    SumSquareDifference.main()

"""
HighlyDivisibleTriangleNumber - Encuentra el primer número triangular con más de N divisores

Este programa calcula números triangulares y encuentra el primero
que tiene más de un número determinado de divisores.

Autor: Isabel Rodenas
Fecha: 2026-01-10
"""

import math

class HighlyDivisibleTriangleNumber:
    """Clase para encontrar el primer número triangular con más de N divisores."""

    def __init__(self, min_divisors):
        self.min_divisors = min_divisors
        self.triangle_number = 0

    def contar_divisores(self, number):
        """Cuenta el número de divisores de un número dado."""
        divisores = 0
        sqrt_n = int(math.sqrt(number))
        for i in range(1, sqrt_n + 1):
            if number % i == 0:
                divisores += 2  # i y number//i
        if sqrt_n * sqrt_n == number:
            divisores -= 1  # si es cuadrado perfecto, no contar doble
        return divisores

    def encontrar_numero_triangulo(self):
        """Encuentra el primer número triangular con más de min_divisors divisores."""
        n = 1
        while True:
            triangle = n * (n + 1) // 2
            if self.contar_divisores(triangle) > self.min_divisors:
                self.triangle_number = triangle
                return self.triangle_number
            n += 1

    def mostrar_resultado(self):
        print(f"The first triangle number with over {self.min_divisors} divisors is: {self.triangle_number}")

    @staticmethod
    def main():
        print("🚀 Iniciando HighlyDivisibleTriangleNumber")
        print("=" * 40)

        while True:
            try:
                min_divisors = int(input("Enter the minimum number of divisors (e.g., 500): "))
            except ValueError:
                print("Please enter a valid integer.")
                continue

            if min_divisors <= 0:
                print("The number of divisors must be greater than 0.")
                continue
            else:
                break

        app = HighlyDivisibleTriangleNumber(min_divisors)
        app.encontrar_numero_triangulo()
        app.mostrar_resultado()
        print("\n✨ Execution completed!")


if __name__ == "__main__":
    HighlyDivisibleTriangleNumber.main()

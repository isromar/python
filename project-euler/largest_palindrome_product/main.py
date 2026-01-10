"""
LargestPalindromeProduct - Calcula el mayor palíndromo producto de dos números

Este programa calcula el mayor palíndromo que se puede obtener como producto
de dos números dentro de un rango dado.

Ejemplo: para números de 3 cifras (100-999), el mayor palíndromo es 906609.

Características:
- Clase 'LargestPalindromeProduct' que encapsula la lógica de cálculo.
- Métodos para calcular el mayor palíndromo y verificar si un número es palíndromo.
- Muestra el resultado.

Autor: Isabel Rodenas
Fecha: 2026-01-10
"""

class LargestPalindromeProduct:
    """Clase para calcular el mayor palíndromo producto de dos números."""

    def __init__(self, max_num, min_num):
        self.max_num = max_num
        self.min_num = min_num
        self.largest_palindrome = 0

    def is_palindrome(self, number):
        """Verifica si un número es palíndromo."""
        str_num = str(number)
        return str_num == str_num[::-1]

    def product_two_numbers(self):
        """Calcula el mayor palíndromo producto de dos números del rango."""
        for i in range(self.max_num, self.min_num - 1, -1):
            for j in range(self.max_num, self.min_num - 1, -1):
                product = i * j
                if self.is_palindrome(product) and product > self.largest_palindrome:
                    self.largest_palindrome = product
        return self.largest_palindrome

    def mostrar_resultado(self):
        print(f"Largest palindrome from product of numbers from {self.min_num} to {self.max_num}: {self.largest_palindrome}")

    @staticmethod
    def main():
        print("🚀 Iniciando LargestPalindromeProduct")
        print("=" * 40)

        while True:
            try:
                min_num = int(input("Enter the minimum number of the range: "))
                max_num = int(input("Enter the maximum number of the range: "))
            except ValueError:
                print("Please enter valid integers.")
                continue

            if min_num <= 0 or max_num <= 0 or min_num > max_num:
                print("Invalid range. Minimum should be >0 and less than maximum.")
                continue
            else:
                break

        app = LargestPalindromeProduct(max_num, min_num)
        app.product_two_numbers()
        app.mostrar_resultado()
        print("\n✨ Execution completed!")


if __name__ == "__main__":
    LargestPalindromeProduct.main()

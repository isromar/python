"""
SumOfPrimes - Calcula la suma de todos los números primos por debajo de un límite

Este programa encuentra todos los números primos por debajo de un número máximo
y calcula su suma.

Características:
- Clase 'SumOfPrimes' que encapsula la lógica de cálculo.
- Método para verificar si un número es primo.
- Método para calcular la suma de primos.
- Muestra el resultado.

Autor: Isabel Rodenas
Fecha: 2026-01-10
"""

class SumOfPrimes:
    """Clase para calcular la suma de todos los números primos por debajo de un límite."""

    def __init__(self, max_num):
        self.max_num = max_num
        self.sum_of_primes = 0

    def is_prime(self, number):
        """Verifica si un número es primo."""
        if number < 2:
            return False
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                return False
        return True

    def calcular_suma_primos(self):
        """Calcula la suma de todos los primos por debajo de max_num."""
        self.sum_of_primes = sum(i for i in range(2, self.max_num) if self.is_prime(i))

    def mostrar_resultado(self):
        print(f"Sum of prime numbers below {self.max_num}: {self.sum_of_primes}")

    @staticmethod
    def main():
        print("🚀 Iniciando SumOfPrimes")
        print("=" * 40)

        while True:
            try:
                max_num = int(input("Enter the maximum number (e.g., 2000000): "))
            except ValueError:
                print("Please enter a valid integer.")
                continue

            if max_num <= 1:
                print("Number must be greater than 1.")
                continue
            else:
                break

        app = SumOfPrimes(max_num)
        app.calcular_suma_primos()
        app.mostrar_resultado()
        print("\n✨ Execution completed!")


if __name__ == "__main__":
    SumOfPrimes.main()

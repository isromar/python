"""
NthPrime - Calcula el número primo n-ésimo

Este programa encuentra el n-ésimo número primo y lo muestra.

Características:
- Clase 'NthPrime' que encapsula la lógica de cálculo.
- Método para verificar si un número es primo.
- Método para encontrar el n-ésimo primo.
- Muestra el resultado.

Autor: Isabel Rodenas
Fecha: 2026-01-10
"""

class NthPrime:
    """Clase para calcular el n-ésimo número primo."""

    def __init__(self, n):
        self.n = n
        self.prime_number = 0

    def is_prime(self, number):
        """Verifica si un número es primo."""
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

    def calcular_n_esimo_primo(self):
        """Calcula el n-ésimo número primo."""
        count = 0
        i = 2
        while count < self.n:
            if self.is_prime(i):
                self.prime_number = i
                count += 1
            i += 1
        return self.prime_number

    def mostrar_resultado(self):
        print(f"The {self.n}-th prime number is: {self.prime_number}")

    @staticmethod
    def main():
        print("🚀 Iniciando NthPrime")
        print("=" * 40)

        while True:
            try:
                n = int(input("Enter which prime number to find (e.g., 10001): "))
            except ValueError:
                print("Please enter a valid integer.")
                continue

            if n <= 0:
                print("Number must be greater than 0.")
                continue
            else:
                break

        app = NthPrime(n)
        app.calcular_n_esimo_primo()
        app.mostrar_resultado()
        print("\n✨ Execution completed!")


if __name__ == "__main__":
    NthPrime.main()

"""
PythagoreanTriplet - Encuentra a, b, c que cumplan a+b+c=1000 y a^2+b^2=c^2

Este programa busca los números enteros positivos a, b y c
que cumplen la condición de ser un triplete pitagórico
con suma igual a 1000, y calcula su producto.

Características:
- Clase 'PythagoreanTriplet' que encapsula la búsqueda.
- Método para encontrar los tripletes y calcular su producto.
- Muestra el resultado.

Autor: Isabel Rodenas
Fecha: 2026-01-10
"""

class PythagoreanTriplet:
    """Clase para calcular el triplete pitagórico con suma 1000."""

    def __init__(self, total_sum):
        self.total_sum = total_sum
        self.a = 0
        self.b = 0
        self.c = 0
        self.product = 0

    def encontrar_triplete(self):
        """Busca el triplete pitagórico y calcula el producto."""
        for a in range(1, self.total_sum // 3):
            for b in range(a, self.total_sum // 2):
                c = self.total_sum - a - b
                if a*a + b*b == c*c:
                    self.a, self.b, self.c = a, b, c
                    self.product = a * b * c
                    return  # Encontramos el triplete, salimos

    def mostrar_resultado(self):
        print(f"a: {self.a}")
        print(f"b: {self.b}")
        print(f"c: {self.c}")
        print(f"a x b x c = {self.product}")

    @staticmethod
    def main():
        print("🚀 Iniciando PythagoreanTriplet")
        print("=" * 40)

        while True:
            try:
                total = int(input("Enter the total sum for the triplet (e.g., 1000): "))
            except ValueError:
                print("Please enter a valid integer.")
                continue

            if total <= 0:
                print("The sum must be greater than 0.")
                continue
            else:
                break

        app = PythagoreanTriplet(total)
        app.encontrar_triplete()
        app.mostrar_resultado()
        print("\n✨ Execution completed!")


if __name__ == "__main__":
    PythagoreanTriplet.main()

"""
MultiplosSuma - Suma de múltiplos de dos números

Este programa calcula la suma de todos los números naturales por debajo
de un límite dado que son múltiplos de dos números determinados por el usuario.

Ejemplo: para num1=3, num2=5 y top=1000, la suma es 233168.

Características:
- Clase 'MultiplosSuma' que encapsula la lógica de cálculo.
- Validación de entrada del usuario.
- Calcula la suma de todos los múltiplos.
- Muestra el resultado.

Autor: Isabel Rodenas
Fecha: 2026-01-10
"""

class MultiplosSuma:
    """Clase para calcular la suma de múltiplos de dos números."""

    def __init__(self, num1, num2, top):
        self.num1 = num1
        self.num2 = num2
        self.top = top
        self.resultado = 0

    def calcular_suma(self):
        """Calcula la suma de todos los múltiplos de num1 o num2 por debajo de top."""
        self.resultado = sum(
            i for i in range(self.top) if i % self.num1 == 0 or i % self.num2 == 0
        )

    def mostrar_resultado(self):
        print(f"Suma de múltiplos de {self.num1} o {self.num2} por debajo de {self.top}: {self.resultado}")

    @staticmethod
    def main():
        print("🚀 Iniciando MultiplosSuma")
        print("=" * 40)

        while True:
            try:
                num1 = int(input("Introduce el primer número: "))
                num2 = int(input("Introduce el segundo número: "))
                top = int(input("Introduce el límite superior: "))
            except ValueError:
                print("Por favor, introduce números válidos")
                continue

            if num1 <= 0 or num2 <= 0 or top <= 0:
                print("Todos los números deben ser mayores que 0")
                continue
            else:
                break

        app = MultiplosSuma(num1, num2, top)
        app.calcular_suma()
        app.mostrar_resultado()
        print("\n✨ ¡Ejecución completada!")


if __name__ == "__main__":
    MultiplosSuma.main()

class FibonacciEvenSum:
    """Calcula la serie de Fibonacci y suma sus términos pares hasta un límite."""

    def __init__(self, limite):
        self.nombre = "FibonacciEvenSum"
        self.limite = limite
        self.terminos_fibonacci = []
        self.suma_pares = 0

    def calcular_y_sumar_pares(self):
        """Genera la serie y suma los pares en un solo ciclo."""
        a, b = 0, 1

        while b < self.limite:
            # Verificamos si el término actual es par
            if b % 2 == 0:
                self.suma_pares += b

            # Guardamos el término en la lista (opcional, para registro)
            self.terminos_fibonacci.append(b)

            # Avanzamos en la serie: b se convierte en la suma de los dos anteriores
            # Usamos asignación múltiple para mayor limpieza
            a, b = b, a + b

    def mostrar_resultados(self):
        """Muestra los resultados formateados."""
        print(f"--- Resultados para límite {self.limite:,} ---")
        print(f"Suma de números pares: {self.suma_pares}")
        print(f"Cantidad de términos generados: {len(self.terminos_fibonacci)}")

    @staticmethod
    def main():
        """Punto de entrada de la aplicación."""
        print("🚀 Iniciando FibonacciEvenSum")
        print("=" * 40)

        while True:
            limite_usuario = input("Introduce el límite máximo (ej. 4000000): ")

            try:
                # Quitamos comas o puntos si el usuario los pone por error
                limite = int(limite_usuario.replace(".", "").replace(",", ""))
                if limite <= 0:
                    print("Por favor, introduce un número positivo.")
                    continue
                break
            except ValueError:
                print("Error: Ingresa un número válido.")

        app = FibonacciEvenSum(limite)
        app.calcular_y_sumar_pares()
        app.mostrar_resultados()
        print("\n✨ ¡Ejecución completada!")


if __name__ == "__main__":
    FibonacciEvenSum.main()

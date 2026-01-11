# main.py (Euler Problems Menu)
import sys
from even_fibonacci_numbers.main import FibonacciEvenSum
from digit_fifth_powers.main import DigitosPotencias
from multiplies_of_numbers.main import MultiplosSuma
from largest_prime_factor.main import MayorFactorPrimo
from largest_palindrome_product.main import LargestPalindromeProduct
from calculates_prime_numbers.main import NthPrime
from highly_divisible_triangular_number.main import HighlyDivisibleTriangleNumber
from largest_product_in_a_series.main import X
from smallest_multiple.main import SmallestMultiple
from special_pythagorean_triplet.main import PythagoreanTriplet
from sum_square_difference.main import SumSquareDifference
from summation_of_primes.main import SumOfPrimes

# Dictionary of menu options: option -> (description, class with main())
MENU_OPTIONS = {
    "1": ("Multiples of 3 or 5", MultiplosSuma),
    "2": ("Even Fibonacci Numbers", FibonacciEvenSum),
    "3": ("Largest Prime Factor", MayorFactorPrimo),
    "4": ("Largest Palindrome Product", LargestPalindromeProduct),
    "X": ("Calculates Prime Numbers", NthPrime),
    "X": ("Highly Divisible Triangular Number", HighlyDivisibleTriangleNumber),
    "X": ("Largest Product in a Series", X),
    "X": ("Smallest Multiple", SmallestMultiple),
    "X": ("Special Pythagorean Triplet", PythagoreanTriplet),
    "X": ("Sum Square Difference", SumSquareDifference),
    "X": ("Summation of Primes", SumOfPrimes),
    "30": ("Digit Fifth Powers", DigitosPotencias),
    "100": ("Exit", None),
}


def main_menu():
    while True:
        print("\n📚 Project Euler Problems Menu")
        for key, (desc, _) in sorted(MENU_OPTIONS.items(), key=lambda x: int(x[0])):
            print(f"{key}. {desc}")

        option = input("Select an option: ").strip()

        if option in MENU_OPTIONS:
            description, cls = MENU_OPTIONS[option]
            if option == "100":
                print("Goodbye!")
                sys.exit()
            else:
                cls.main()  # Calls the main() method of the selected class
        else:
            print("❌ Invalid option. Try again.")


if __name__ == "__main__":
    main_menu()

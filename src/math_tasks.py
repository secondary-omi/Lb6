import math


def display_constants():
    print("Число Эйлера (e):", math.e)
    print("Число Пи (pi):", math.pi)
    print("NaN:", math.nan)


def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Факториал определён только для неотрицательных чисел")
    return math.factorial(n)


def gcd(a: int, b: int) -> int:
    return math.gcd(a, b)


if __name__ == "__main__":
    display_constants()

    n = 14
    print(f"Факториал {n}:", factorial(n))

    a, b = 512, 14
    print(f"НОД {a} и {b}:", gcd(a, b))

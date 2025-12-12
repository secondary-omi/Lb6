import numpy as np


def fahrenheit_to_kelvin(f: float) -> float:
    return (f - 32.0) * (5.0 / 9.0) + 273.15


def batch_f_to_k(values):
    arr = np.asarray(values, dtype=float)
    return (arr - 32.0) * (5.0 / 9.0) + 273.15


if __name__ == "__main__":
    sample = [0, 32, 68, 100, 212]
    print("Фаренгейт (°F):", sample)
    print("Кельвин (K):", batch_f_to_k(sample))

import numpy as np
import matplotlib.pyplot as plt


def plot_f_to_k():
    f_values = np.array([0, 32, 68, 100, 212])
    k_values = (f_values - 32) * 5/9 + 273.15

    plt.figure(figsize=(7, 4))
    plt.plot(f_values, k_values, marker='o', label="F → K")
    plt.xlabel("Fahrenheit")
    plt.ylabel("Kelvin")
    plt.title("График преобразования температур F → K")
    plt.grid(True)
    plt.legend()
    plt.show()


def plot_histogram():
    data = np.random.normal(loc=0, scale=1, size=1000)

    plt.figure(figsize=(7, 4))
    plt.hist(data, bins=30)
    plt.title("Гистограмма нормального распределения")
    plt.xlabel("Значение")
    plt.ylabel("Частота")
    plt.grid(True)
    plt.show()


def plot_pie():
    values = [25, 35, 30, 10]
    labels = ["A", "B", "C", "D"]

    plt.figure(figsize=(6, 6))
    plt.pie(values, labels=labels, autopct="%1.1f%%", startangle=90)
    plt.title("Пример круговой диаграммы")
    plt.axis("equal")
    plt.show()


def plot_boxplot():
    sets = [np.random.normal(i, 1, 200) for i in range(3)]

    plt.figure(figsize=(6, 4))
    plt.boxplot(sets, labels=["Set 1", "Set 2", "Set 3"])
    plt.title("Boxplot примеров")
    plt.xlabel("Набор данных")
    plt.ylabel("Значения")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    plot_f_to_k()
    plot_histogram()
    plot_pie()
    plot_boxplot()

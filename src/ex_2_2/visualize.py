import matplotlib.pyplot as plt
import numpy as np
from data_loader import load_data
import tensorflow as tf

CLASS_NAMES = [
    "T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
    "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"
]

def visualize_predictions(model, x_test, y_test, num_samples=10):
    predictions = model.predict(x_test[:num_samples])

    plt.figure(figsize=(12, 4))
    for i in range(num_samples):
        plt.subplot(2, 5, i + 1)
        plt.imshow(x_test[i], cmap='gray')
        predicted_class = CLASS_NAMES[np.argmax(predictions[i])]
        true_class = CLASS_NAMES[y_test[i]]
        color = 'green' if predicted_class == true_class else 'red'
        plt.title(f"Предсказано: {predicted_class}\nИстина: {true_class}", color=color)
        plt.axis('off')
    plt.tight_layout()
    plt.show()

def main():
    (_, _), (x_test, y_test) = load_data()

    model_path = "src/ex_2_2/model.keras"
    model = tf.keras.models.load_model(model_path)
    print(f"Модель загружена из {model_path}")

    visualize_predictions(model, x_test, y_test, num_samples=10)

if __name__ == "__main__":
    main()

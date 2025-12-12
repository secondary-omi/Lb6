from data_loader import load_data
import tensorflow as tf
import numpy as np

CLASS_NAMES = [
    "T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
    "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"
]

def main():
    (_, _), (x_test, y_test) = load_data()

    model_path = "src/ex_2_2/model.keras"
    model = tf.keras.models.load_model(model_path)
    print(f"Модель загружена из {model_path}")

    test_loss, test_acc = model.evaluate(x_test, y_test)
    print(f"Тестовая точность: {test_acc:.4f}, тестовая потеря: {test_loss:.4f}")

    predictions = model.predict(x_test[:10])
    for i, pred in enumerate(predictions):
        predicted_class = CLASS_NAMES[np.argmax(pred)]
        true_class = CLASS_NAMES[y_test[i]]
        print(f"Пример {i+1}: предсказано — {predicted_class}, истинный класс — {true_class}")

if __name__ == "__main__":
    main()

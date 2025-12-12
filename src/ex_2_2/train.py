from data_loader import load_data
from model import build_model
import tensorflow as tf
import os

def main():
    (x_train, y_train), (x_test, y_test) = load_data()

    model = build_model()

    model.fit(x_train, y_train, epochs=5, validation_split=0.1, batch_size=64)

    save_path = os.path.join(os.path.dirname(__file__), 'model.keras')
    model.save(save_path)
    print(f"Модель сохранена в {save_path}")

    test_loss, test_acc = model.evaluate(x_test, y_test)
    print(f"Тестовая точность: {test_acc:.4f}, тестовая потеря: {test_loss:.4f}")

if __name__ == "__main__":
    main()

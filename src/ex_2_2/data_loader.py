import tensorflow as tf


def load_data():
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()

    x_train = x_train.astype("float32") / 255.0
    x_test = x_test.astype("float32") / 255.0

    x_train = x_train[..., tf.newaxis]
    x_test = x_test[..., tf.newaxis]

    return (x_train, y_train), (x_test, y_test)


FASHION_CLASSES = [
    "T-shirt/top",      # 0
    "Trouser",          # 1
    "Pullover",         # 2
    "Dress",            # 3
    "Coat",             # 4
    "Sandal",           # 5
    "Shirt",            # 6
    "Sneaker",          # 7
    "Bag",              # 8
    "Ankle boot"        # 9
]


def get_class_name(label_id: int) -> str:
    return FASHION_CLASSES[label_id]

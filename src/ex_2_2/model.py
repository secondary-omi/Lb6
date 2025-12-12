import tensorflow as tf

layers = tf.keras.layers
models = tf.keras.models


def build_model():

    model = models.Sequential([
        layers.Flatten(input_shape=(28, 28)),          # превращаем 28x28 в вектор
        layers.Dense(128, activation='relu'),          # скрытый слой
        layers.Dense(64, activation='relu'),           # ещё один скрытый слой
        layers.Dense(10, activation='softmax')         # выходной слой (10 классов)
    ])

    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )

    return model

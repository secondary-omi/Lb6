CLASS_NAMES = [
    "T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
    "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"
]

def label_to_class(label: int) -> str:
    return CLASS_NAMES[label]

def class_to_label(class_name: str) -> int:
    if class_name in CLASS_NAMES:
        return CLASS_NAMES.index(class_name)
    raise ValueError(f"Класс '{class_name}' не найден в списке CLASS_NAMES.")

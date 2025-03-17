import numpy as np
import matplotlib.pyplot as plt


def generate_symmetric_sprite(size=5):
    """Генерирует случайный симметричный спрайт."""
    half_size = size // 2 + size % 2  # Определяем половину строки с учетом нечетного размера

    # Создаем случайную половину изображения
    half_sprite = np.random.choice([0, 1], size=(size, half_size))

    # Делаем его симметричным
    sprite = np.hstack((half_sprite, np.fliplr(half_sprite[:, :size // 2])))

    return sprite


# Генерируем и выводим случайный спрайт
sprite = generate_symmetric_sprite(5)

plt.figure(figsize=(2, 2))
plt.imshow(sprite, cmap="gray_r")  # Черно-белая палитра
plt.axis("off")  # Убираем оси
plt.show()

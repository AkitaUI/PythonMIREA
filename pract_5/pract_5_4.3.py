import numpy as np
import matplotlib.pyplot as plt


def generate_symmetric_sprite(size_x=5, size_y=5):
    """Генерирует случайный симметричный спрайт"""
    half_size_x = size_x // 2 + size_x % 2  # Определяем половину строки с учетом нечетного размера

    choices = np.arange(0, 16)  # 0 и числа от 1 до 15
    probabilities = [0.5] + [0.5 / 15] * 15  # Вероятность 50% для 0 и равномерное распределение для 1-15

    half_sprite = np.random.choice(choices, size=(size_y, half_size_x), p=probabilities)
    sprite = np.hstack((half_sprite, np.fliplr(half_sprite[:, :size_x // 2])))

    return sprite


def generate_sprite_map(rows=10, cols=20, sprite_size_x=5, sprite_size_y=5, padding=5, border=2):
    """Генерирует карту спрайтов с цветами и разными видами симметрии."""
    total_size_x = cols * (sprite_size_x + padding) - padding + 2 * border
    total_size_y = rows * (sprite_size_y + padding) - padding + 2 * border
    sprite_map = np.zeros((total_size_y, total_size_x))  # Фон черный

    for i in range(rows):
        for j in range(cols):
            sprite = generate_symmetric_sprite(sprite_size_x, sprite_size_y)
            y_offset = border + i * (sprite_size_y + padding)
            x_offset = border + j * (sprite_size_x + padding)
            sprite_map[y_offset:y_offset + sprite_size_y, x_offset:x_offset + sprite_size_x] = sprite

    return sprite_map


# Палитра PICO-8
pico8_palette = [
    "#000000", "#7E2553", "#008751", "#AB5236", "#5F574F", "#C2C3C7",
    "#FFF1E8", "#FF004D", "#FFA300", "#FFEC27", "#00E436", "#29ADFF",
    "#83769C", "#FF77A8", "#FFCCAA",
]

# Генерируем и выводим карту спрайтов
sprite_map = generate_sprite_map(10, 20, 7, 6, 5, 2)

plt.figure(figsize=(10, 5))
plt.imshow(sprite_map, cmap=plt.cm.colors.ListedColormap(pico8_palette))  # Используем палитру PICO-8
plt.show()

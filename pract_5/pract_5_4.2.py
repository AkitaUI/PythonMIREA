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


def generate_sprite_map(rows=10, cols=20, sprite_size=5, padding=5, border=2):
    """Генерирует карту спрайтов с черным фоном между ними и отступом от краев."""
    total_size_x = cols * (sprite_size + padding) - padding + 2 * border
    total_size_y = rows * (sprite_size + padding) - padding + 2 * border
    sprite_map = np.zeros((total_size_y, total_size_x))  # Заполняем фон черным (0)

    for i in range(rows):
        for j in range(cols):
            sprite = generate_symmetric_sprite(sprite_size)
            y_offset = border + i * (sprite_size + padding)
            x_offset = border + j * (sprite_size + padding)
            sprite_map[y_offset:y_offset + sprite_size, x_offset:x_offset + sprite_size] = sprite

    return sprite_map


# Генерируем и выводим карту спрайтов
sprite_map = generate_sprite_map(10, 20, 5, 5, 2)

plt.figure(figsize=(10, 5))
plt.imshow(sprite_map, cmap="gray")  # Используем серую палитру, где 0 — черный
plt.axis("off")  # Убираем оси
plt.show()
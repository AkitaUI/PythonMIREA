import numpy as np
import matplotlib.pyplot as plt


# Класс для представления состояния генератора
class Seed:
    def __init__(self, w0, w1, w2):
        self.w0 = w0
        self.w1 = w1
        self.w2 = w2

    def tweak(self):
        temp = (self.w0 + self.w1 + self.w2) & 0xFFFF
        self.w0, self.w1, self.w2 = self.w1, self.w2, temp


# Набор слогов для генерации имён планет
PAIRS = "..LEXEGEZACEBISO" "USESARMAINDIREA." "ERATENBERALAVETI" "EDORQUANTEISRION"
PAIRS = PAIRS.replace('.', '')


def generate_system(seed):
    """Генерирует звёздную систему из текущего состояния seed."""
    system = {}
    system['x'] = (seed.w1 >> 8) & 0xFF
    system['y'] = (seed.w0 >> 8) & 0xFF
    system['govtype'] = (seed.w1 >> 3) & 7
    system['economy'] = (seed.w0 >> 8) & 7

    if system['govtype'] <= 1:
        system['economy'] |= 2

    system['techlev'] = ((seed.w1 >> 8) & 3) + (system['economy'] ^ 7)
    system['techlev'] += system['govtype'] >> 1
    if system['govtype'] & 1:
        system['techlev'] += 1

    system['population'] = 4 * system['techlev'] + system['economy'] + system['govtype'] + 1
    system['productivity'] = (((system['economy'] ^ 7) + 3) * (system['govtype'] + 4) * system['population'] * 8)
    system['radius'] = 256 * (((seed.w2 >> 8) & 15) + 11) + system['x']

    name_pairs = []
    for _ in range(4):
        pair = 2 * ((seed.w2 >> 8) & 31)
        name_pairs.append(PAIRS[pair:pair + 2])
        seed.tweak()

    system['name'] = ''.join(name_pairs[:3] if not (seed.w0 & 64) else name_pairs)
    return system


def generate_galaxy(seed, num_systems=256):
    """Генерирует список звёздных систем."""
    systems = []
    for _ in range(num_systems):
        systems.append(generate_system(seed))
    return systems


def plot_galaxy(systems):
    """Визуализирует сгенерированную галактику."""
    plt.figure(figsize=(20, 10))
    plt.style.use('dark_background')

    for system in systems:
        plt.scatter(system['x'], -system['y'], color='cyan', s=2)  # Разворачиваем ось Y
        plt.text(system['x'], -system['y'], f" {system['name']}", fontsize=6, color='gray')

    plt.show()


# Начальное состояние первой галактики
seed = Seed(0x5A4A, 0x0248, 0xB753)
galaxy = generate_galaxy(seed)
plot_galaxy(galaxy)

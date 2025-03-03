#5.1

def generate_groups():
    groups = []

    ivbo_main = [f"ИВБО-{i}-23" for i in [10, 11, 12, 13, 20, 21, 22]]
    groups.extend(ivbo_main)

    ikbo_first = [f"ИКБО-{i}-22" for i in [10, 24, 34]]
    ikbo_second = [f"ИКБО-{i}-23" for i in
                   [10, 11, 12, 13, 14, 15, 20, 21, 22, 41, 42, 43, 50, 51, 52, 60, 61, 62, 63, 64, 65, 66, 67, 68, 70,
                    71, 72, 73, 74, 75, 76]]
    groups.extend(ikbo_first + ikbo_second)

    imbo = [f"ИМБО-{i}-23" for i in [10, 11]]
    groups.extend(imbo)

    inbo = [f"ИНБО-{i}-23" for i in [10, 11, 12, 13, 20, 21, 22, 23, 30, 31, 32, 33]]
    groups.extend(inbo)

    return groups

print(generate_groups())

#5.2
import sys

def custom_print(*args, sep=' ', end='\n', file=sys.stdout):
    output = sep.join(map(str, args)) + end
    file.write(output)

custom_print("Hello", "world!")
custom_print("Hello", "world!", sep='-', end='...\n')

#5.3

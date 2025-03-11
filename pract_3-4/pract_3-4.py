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
def manual_utf16le_decode(b: bytes) -> str:
    if len(b) % 2 != 0:
        raise ValueError("ДА НУ НЕЛЬЗЯ")
    result = []
    for i in range(0, len(b), 2):
        low = b[i]
        high = b[i+1]
        code = (high << 8) | low
        result.append(chr(code))
    return "".join(result)


def tea_decrypt(v, k):
    v0, v1 = v[0], v[1]
    delta = 0x9E3779B9
    sum_val = 0xC6EF3720
    mask = 0xFFFFFFFF

    for _ in range(32):
        v1 = (v1 - (((v0 << 4) + k[2]) ^ (v0 + sum_val) ^ ((v0 >> 5) + k[3]))) & mask
        v0 = (v0 - (((v1 << 4) + k[0]) ^ (v1 + sum_val) ^ ((v1 >> 5) + k[1]))) & mask
        sum_val = (sum_val - delta) & mask

    return [v0, v1]

def hex_to_int_list(hex_string):
    return [int(token, 16) for token in hex_string.split()]

encrypted_hex = """
E3238557 6204A1F8 E6537611 174E5747
5D954DA8 8C2DFE97 2911CB4C 2CB7C66B
E7F185A0 C7E3FA40 42419867 374044DF
2519F07D 5A0C24D4 F4A960C5 31159418
F2768EC7 AEAF14CF 071B2C95 C9F22699
FFB06F41 2AC90051 A53F035D 830601A7
EB475702 183BAA6F 12626744 9B75A72F
8DBFBFEC 73C1A46E FFB06F41 2AC90051
97C5E4E9 B1C26A21 DD4A3463 6B71162F
8C075668 7975D565 6D95A700 7272E637
"""

encrypted_ints = hex_to_int_list(encrypted_hex)
key = [0, 4, 5, 1]

decrypted_bytes = bytearray()
for i in range(0, len(encrypted_ints), 2):
    block = encrypted_ints[i:i+2]
    dec_block = tea_decrypt(block, key)

    decrypted_bytes.extend(dec_block[0].to_bytes(4, byteorder='little'))
    decrypted_bytes.extend(dec_block[1].to_bytes(4, byteorder='little'))


decrypted_text = manual_utf16le_decode(decrypted_bytes)
print(decrypted_text)

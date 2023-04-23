import random
import string


def change_random_bit(data):
    bits = [int(bit) for bit in text_to_bits(data)]
    digitindex = random.randint(0, len(bits)-1)
    bits[digitindex] ^= 1
    changed = "".join(str(bit) for bit in bits)
    return text_from_bits(changed)


def text_to_bits(text, encoding="utf-16", errors = "surrogatepass"):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8*((len(bits)+7)//8))


def text_from_bits(bits, encoding="utf-16", errors = "surrogatepass"):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length()+7)//8, 'big').decode(encoding, errors) or '\0'


def hex_to_bin(hex):
    scale = 16
    num_of_bits = 8
    return bin(int(hex, scale))[2:].zfill(num_of_bits)


def compare_hexes(start_hex, changed_hex):
    start_hex = hex_to_bin(start_hex)
    changed_hex = hex_to_bin(changed_hex)
    compared_bits = int(start_hex, 2) ^ int(changed_hex, 2)
    sum = 0
    for digit in bin(compared_bits)[2:].zfill(len(start_hex)):
        sum += int(digit)
    return sum


def random_str(size=5, chars=string.printable):
    return ''.join(random.choice(chars) for _ in range(size))


if __name__ == '__main__':
    msg = "Щастям б'єш жук їх глицю в фон й ґедзь пріч.", "Факт ґринджол: бій псюг вщух, з'їм шче яєць."
    changed_msg = change_random_bit(msg)
    print(changed_msg)



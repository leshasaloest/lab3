from kupyna import Kupyna
from constants import PANGRAMS
from functions import change_random_bit, compare_hexes


if __name__ == '__main__':
    for pangram in PANGRAMS:
        sum256 = 0
        sum384 = 0
        sum512 = 0
        for _ in range(10):
            changed_pangram = change_random_bit(pangram)
            hash256 = Kupyna(256).hash(pangram)
            hash384 = Kupyna(384).hash(pangram)
            hash512 = Kupyna(512).hash(pangram)
            changed_hash256 = Kupyna(256).hash(changed_pangram)
            changed_hash384 = Kupyna(384).hash(changed_pangram)
            changed_hash512 = Kupyna(512).hash(changed_pangram)
            sum256 += compare_hexes(hash256, changed_hash256)
            sum384 += compare_hexes(hash384, changed_hash384)
            sum512 += compare_hexes(hash512, changed_hash512)
        print("Kupyna256", sum256/10)
        print("Kupyna384", sum384/10)
        print("Kupyna512", sum512/10)

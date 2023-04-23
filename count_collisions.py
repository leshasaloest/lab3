import numba.core.errors

from kupyna import Kupyna
from functions import random_str
import time


def collisions_counter():
    kupyna256 = Kupyna(256)
    kupyna384 = Kupyna(384)
    kupyna512 = Kupyna(512)
    totalBits = 256
    collisionBits = 5
    for hash_func in [kupyna256, kupyna384, kupyna512]:
        mask = (1 << totalBits) - (1 << totalBits - collisionBits)
        collision_test_time = 0
        for i in range(10):
            ti = time.time()
            string = random_str(20)
            count = 0
            while True:
                msg = string + ':' + str(count)
                dig = hash_func.hash(msg)
                res = int(dig, 16) & mask
                if res == 0:
                    break
                count += 1
            collision_test_time += time.time() - ti
        print(hash_func, collision_test_time / 10)
        totalBits += 128


if __name__ == '__main__':
    collisions_counter()

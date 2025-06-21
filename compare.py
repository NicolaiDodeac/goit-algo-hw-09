import time
from greedy import find_coins_greedy
from dynamic import find_min_coins

amount = 113

start = time.perf_counter()
greedy_result = find_coins_greedy(amount)
greedy_time = time.perf_counter() - start

start = time.perf_counter()
dp_result = find_min_coins(amount)
dp_time = time.perf_counter() - start
if __name__ == "__main__":
    print("Greedy:", greedy_result, f"Time: {greedy_time:.6f} sec")
    print("DP:", dp_result, f"Time: {dp_time:.6f} sec")

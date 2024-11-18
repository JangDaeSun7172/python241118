import sys
import time

# 리스트와 튜플 생성
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)

# 1. 가변성 (Mutability)
print("Before modification:")
print("List:", my_list)
print("Tuple:", my_tuple)

# 리스트는 변경 가능
my_list[0] = 10
print("\nAfter modifying the list:")
print("List:", my_list)

# 튜플은 변경 불가능
try:
    my_tuple[0] = 10
except TypeError as e:
    print("\nAttempt to modify tuple:")
    print("Error:", e)

# 2. 메모리 사용
print("\nMemory usage:")
print("List size:", sys.getsizeof(my_list), "bytes")
print("Tuple size:", sys.getsizeof(my_tuple), "bytes")

# 3. 성능 비교
large_list = list(range(1000000))
large_tuple = tuple(range(1000000))

# 리스트와 튜플에 접근하는 시간 측정
start_time = time.time()
_ = large_list[500000]
list_access_time = time.time() - start_time

start_time = time.time()
_ = large_tuple[500000]
tuple_access_time = time.time() - start_time

print("\nAccess time:")
print("List access time:", list_access_time, "seconds")
print("Tuple access time:", tuple_access_time, "seconds")



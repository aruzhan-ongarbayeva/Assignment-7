"""
💎 Exercise-1: count_substrings
Write a function "count_substrings(s: str, subs: str) -> int" that takes 
two strings 's' and 'subs' and returns the number of non-overlapping 
occurrences of the substring 'subs' in the string 's'.

Example:
count_substrings("ababab", "ab") -> 3
count_substrings("aaaaaa", "aa") -> 3
"""

def count_substrings(s: str, subs: str) -> int:
    # write your code here
    if subs == "":
        return 0
    count = 0
    i = 0
    m = len(subs)
    while True:
        j = s.find(subs, i)
        if j == -1:
            break
        count += 1
        i = j + m
    return count
print("Ex 1")
print(count_substrings("ababab", "ab"))
print(count_substrings("aaaaaa", "aa"))

"""
💎 Exercise-2: find_smallest_divisor
Write a function "find_smallest_divisor(n: int) -> int" that 
takes a positive integer 'n' and returns the smallest prime divisor of 'n'.

Example:
find_smallest_divisor(21) -> 3
find_smallest_divisor(49) -> 7
"""

def find_smallest_divisor(n: int) -> int:
    # write your code here
    if n <= 1:
        return n

    if n % 2 == 0:
        return 2

    d = 3
    while d * d <= n:
        if n % d == 0:
            return d
        d += 2

    # Исключение по простым числам
    return n

print("Ex 2")
print(find_smallest_divisor(21))
print(find_smallest_divisor(49))

"""
💎 Exercise-3: check_divisible_by_any
Write a function "check_divisible_by_any(n: int, divisors: str) -> bool" that 
takes a positive integer 'n' and a string 'divisors' containing a sequence of 
space-separated integers, and returns True if 'n' is divisible by 
any of the integers in the 'divisors' string.

Example:
check_divisible_by_any(24, "2 3 5") -> True
check_divisible_by_any(23, "2 3 5") -> False
"""

def check_divisible_by_any(n: int, divisors: str) -> bool:
    # write your code here
    nums = divisors.split()

    for d in nums:
        d = int(d)
        if d != 0 and n % d == 0:
            return True

    return False


print("Ex 3")
print(check_divisible_by_any(24, "2 3 5"))
print(check_divisible_by_any(23, "2 3 5"))

"""
💎 Exercise-4: find_nth_root
Write a function "find_nth_root(x: float, n: int) -> float" that 
takes a float 'x' and an integer 'n' and returns the 'n'-th root 
of 'x' with a precision of up to 3 decimal places.

Example:
find_nth_root(8, 3) -> 2.0
find_nth_root(81, 4) -> 3.0
"""

def find_nth_root(x: float, n: int) -> float:
    # write your code here
    if n == 0:
        raise ValueError("n must be non-zero for nth root")
    if x < 0 and n % 2 == 0:
        raise ValueError("even root of a negative number is not real")

    if x == 0:
        return 0.0
    if n == 1:
        return round(float(x), 3)

    negate = (x < 0 and n % 2 == 1)
    ax = -x if negate else x

    y = ax if ax >= 1 else 1.0

    eps = 1e-12
    max_iter = 200
    for _ in range(max_iter):
        y_prev = y
        y_pow = y ** (n - 1)
        if y_pow == 0:
            y = 1.0
            continue
        y = ((n - 1) * y + ax / y_pow) / n
        if abs(y - y_prev) <= eps:
            break

    result = -y if negate else y
    return round(float(result), 3)

print("Ex 4")
print(find_nth_root(8, 3))
print(find_nth_root(81, 4))


"""
💎 Exercise-5: collatz_sequence_length
Write a function "collatz_sequence_length(n: int) -> int" that takes a 
positive integer 'n' and returns the number of steps it takes to reach 1 
using the Collatz conjecture. The Collatz conjecture states that for 
any positive integer 'n', if 'n' is even, it should be divided by 2; 
if 'n' is odd, it should be multiplied by 3 and then add 1. Repeat this 
process until 'n' becomes 1.

Example:
collatz_sequence_length(6) -> 8
collatz_sequence_length(27) -> 111
"""

def collatz_sequence_length(n: int) -> int:
    # write your code here
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps


print("Ex 5")
print(collatz_sequence_length(6))
print(collatz_sequence_length(27))

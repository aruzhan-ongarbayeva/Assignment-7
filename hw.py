"""
Exercise-1: is_prime
Write a function "is_prime(n: int) -> bool" that takes an integer 'n'
and checks whether it is prime. Function should return a boolean value.

Example:
is_prime(7) -> True
is_prime(10) -> False
"""

def is_prime(n: int) -> bool:
    # write your code here
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

print("Ex 1")
print(is_prime(7))
print(is_prime(10))



"""
Exercise-2: nth_fibonacci
Write a function "nth_fibonacci(n: int) -> int" that 
takes an integer 'n' and returns the nth number in the Fibonacci sequence.

Example:
nth_fibonacci(6) -> 5
nth_fibonacci(9) -> 21
"""

def nth_fibonacci(n: int) -> int:
    # write your code here
    if n <= 0:
        return 0
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a

print("Ex 2")
print(nth_fibonacci(6))
print(nth_fibonacci(9))



"""
Exercise-3: factorial
Write a function "factorial(n: int) -> int" that takes an integer 'n' and returns the factorial of 'n'.

Example:
factorial(5) -> 120
factorial(6) -> 720
"""

def factorial(n: int) -> int:
    # write your code here
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print("Ex 3")
print(factorial(5))
print(factorial(6))



"""
Exercise-4: count_vowels
Write a function "count_vowels(s: str) -> int" that 
takes a string 's' and returns the number of vowels in the string.

Example:
count_vowels("hello") -> 2
count_vowels("world") -> 1
"""

def count_vowels(s: str) -> int:
    # write your code here
    vowels = "aeiouAEIOU"
    return sum(1 for ch in s if ch in vowels)

print("Ex 4")
print(count_vowels("hello"))
print(count_vowels("world"))



"""
Exercise-5: sum_of_digits
Write a function "sum_of_digits(n: int) -> int" that 
takes an integer 'n' and returns the sum of its digits.

Example:
sum_of_digits(12345) -> 15
sum_of_digits(98765) -> 35
"""

def sum_of_digits(n: int) -> int:
    # write your code here
    return sum(int(d) for d in str(abs(n)))

print("Ex 5")
print(sum_of_digits(12345))
print(sum_of_digits(98765))



"""
Exercise-6: reverse_string
Write a function "reverse_string(s: str) -> str" that takes a string 's' and returns the string reversed.

Example:
reverse_string("hello") -> "olleh"
reverse_string("world") -> "dlrow"
"""

def reverse_string(s: str) -> str:
    # write your code here
    return s[::-1]

print("Ex 6")
print(reverse_string("hello"))
print(reverse_string("world"))



"""
Exercise-7: sum_of_squares
Write a function "sum_of_squares(n: int) -> int" that takes an integer 'n' and 
returns the sum of squares of all integers from 1 to 'n'.

Example:
sum_of_squares(4) -> 30
sum_of_squares(5) -> 55
"""

def sum_of_squares(n: int) -> int:
    # write your code here
    return n * (n + 1) * (2 * n + 1) // 6

print("Ex 7")
print(sum_of_squares(4))
print(sum_of_squares(5))



"""
Exercise-8: collatz_sequence_length
Write a function "collatz_sequence_length(n: int) -> int" that takes an 
integer 'n' and returns the length of the Collatz sequence starting with 'n'.

Example:
collatz_sequence_length(6) -> 9
collatz_sequence_length(27) -> 112
"""

def collatz_sequence_length(n: int) -> int:
    # write your code here
    length = 1
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        length += 1
    return length

print("Ex 8")
print(collatz_sequence_length(6))
print(collatz_sequence_length(27))



"""
Exercise-9: is_leap_year
Write a function "is_leap_year(year: int) -> bool" that takes an 
integer 'year' and returns True if 'year' is a leap year, and False otherwise.

Example:
is_leap_year(2000) -> True
is_leap_year(1900) -> False
"""

def is_leap_year(year: int) -> bool:
    # write your code here
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)

print("Ex 9")
print(is_leap_year(2000))
print(is_leap_year(1900))



"""
Exercise-10: count_words
Write a function "count_words(s: str) -> int" that takes a string 's' and 
returns the number of words in the string. Assume words are separated by spaces.

Example:
count_words("Hello world") -> 2
count_words("This is a test") -> 4
"""

def count_words(s: str) -> int:
    # write your code here
    return len(s.split())

print("Ex 10")
print(count_words("Hello world"))
print(count_words("This is a test"))



"""
Exercise-11: is_palindrome
Write a function "is_palindrome(s: str) -> bool" that takes a string 's' and 
checks if the string is a palindrome. The function should return True if the 
string is a palindrome, and False otherwise.

Example:
is_palindrome("racecar") -> True
is_palindrome("hello") -> False
"""

def is_palindrome(s: str) -> bool:
    # write your code here
    return s == s[::-1]

print("Ex 11")
print(is_palindrome("racecar"))
print(is_palindrome("hello"))



"""
Exercise-12: sum_of_multiples
Write a function "sum_of_multiples(n: int, x: int, y: int) -> int" that 
takes three integers 'n', 'x', and 'y', and returns the sum of all the 
numbers from 1 to 'n' (inclusive) that are multiples of 'x' or 'y'.

Example:
sum_of_multiples(10, 3, 5) -> 33
sum_of_multiples(20, 7, 11) -> 168
"""

def sum_of_multiples(n: int, x: int, y: int) -> int:
    # write your code here
    return sum(i for i in range(1, n + 1) if i % x == 0 or i % y == 0)

print("Ex 12")
print(sum_of_multiples(10, 3, 5))
print(sum_of_multiples(20, 7, 11))



"""
Exercise-13: gcd
Write a function "gcd(a: int, b: int) -> int" that takes two integers 'a' and 'b', 
and returns their greatest common divisor (GCD).

Example:
gcd(56, 98) -> 14
gcd(27, 15) -> 3
"""

def gcd(a: int, b: int) -> int:
    # write your code here
    while b:
        a, b = b, a % b
    return a

print("Ex 13")
print(gcd(56, 98))
print(gcd(27, 15))



"""
Exercise-14: lcm
Write a function "lcm(a: int, b: int) -> int" that takes two integers 'a' and 'b', 
and returns their least common multiple (LCM).

Example:
lcm(5, 7) -> 35
lcm(6, 8) -> 24
"""

def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)

print("Ex 14")
print(lcm(5, 7))
print(lcm(6, 8))



"""
Exercise-15: count_characters
Write a function "count_characters(s: str, c: str) -> int" that 
takes a string 's' and a character 'c', and returns the number of occurrences of 'c' in 's'.

Example:
count_characters("hello world", "l") -> 3
count_characters("apple", "p") -> 2
"""

def count_characters(s: str, c: str) -> int:
    # write your code here
    return s.count(c)

print("Ex 15")
print(count_characters("hello world", "l"))
print(count_characters("apple", "p"))



"""
Exercise-16: digit_count
Write a function "digit_count(n: int) -> int" that takes an 
integer 'n' and returns the number of digits in 'n'.

Example:
digit_count(123) -> 3
digit_count(4567) -> 4
"""

def digit_count(n: int) -> int:
    # write your code here
    return len(str(abs(n)))

print("Ex 16")
print(digit_count(123))
print(digit_count(4567))



"""
Exercise-17: is_power_of_two
Write a function "is_power_of_two(n: int) -> bool" that takes an integer 'n' 
and returns True if 'n' is a power of 2, and False otherwise.

Example:
is_power_of_two(8) -> True
is_power_of_two(10) -> False
"""

def is_power_of_two(n: int) -> bool:
    # write your code here
    return n > 0 and (n & (n - 1)) == 0

print("Ex 17")
print(is_power_of_two(8))
print(is_power_of_two(10))



"""
Exercise-18: sum_of_cubes
Write a function "sum_of_cubes(n: int) -> int" that takes an integer 'n' 
and returns the sum of the cubes of all numbers from 1 to 'n'.

Example:
sum_of_cubes(3) -> 36
sum_of_cubes(4) -> 100
"""

def sum_of_cubes(n: int) -> int:
    # write your code here
    s = n * (n + 1) // 2
    return s * s

print("Ex 18")
print(sum_of_cubes(3))
print(sum_of_cubes(4))



"""
Exercise-19: is_perfect_square
Write a function "is_perfect_square(n: int) -> bool" that takes an 
integer 'n' and returns True if 'n' is a perfect square, and False otherwise.

Example:
is_perfect_square(9) -> True
is_perfect_square(10) -> False
"""

def is_perfect_square(n: int) -> bool:
    # write your code here
    if n < 0:
        return False
    r = int(n ** 0.5)
    return r * r == n

print("Ex 19")
print(is_perfect_square(9))
print(is_perfect_square(10))



"""
Exercise-20: is_armstrong_number
Write a function "is_armstrong_number(n: int) -> bool" that takes an 
integer 'n' and returns True if 'n' is an Armstrong number, and False otherwise.

Example:
is_armstrong_number(153) -> True
is_armstrong_number(370) -> True
"""

def is_armstrong_number(n: int) -> bool:
    # write your code here
    s = str(n)
    k = len(s)
    return sum(int(d) ** k for d in s) == n

print("Ex 20")
print(is_armstrong_number(153))
print(is_armstrong_number(370))
"""
This module contains functions related to prime numbers.
"""


def check_if_prime(n):
    """
    Checks if a given number is prime.
    :param n: The number to check.
    :return: A message indicating whether the number is prime or not.
    """
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return "The given number is not prime."
    return "The given number is prime."


if __name__ == "__main__":
    user_input = int(input("Please enter a number: "))
    print(check_if_prime(user_input))

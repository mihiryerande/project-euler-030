# Problem 30:
#     Digit Fifth Powers
#
# Description:
#     Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
#         1634 = 1^4 + 6^4 + 3^4 + 4^4
#         8208 = 8^4 + 2^4 + 0^4 + 8^4
#         9474 = 9^4 + 4^4 + 7^4 + 4^4
#     As 1 = 1^4 is not a sum it is not included.
#
#     The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
#     Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

from num2words import num2words


def calc_upper_limit(p):
    """
    Returns the upper limit (inclusive) of the set of numbers which
      could be written as the sum of the `p`th power of their digits.

    Args:
        p (int): Natural number

    Returns:
        Highest possible number which might be written as sum of `p`th power of its digits.

    Raises:
        AssertError: if incorrect args are given
    """
    # Idea:
    #     For some `n`-digit number,
    #       the maximum achievable sum is for the number (10^n - 1),
    #       meaning the number 99...9 (n times)
    #     As `n`, the number of digits, increases,
    #       the maximum achievable sum will eventually be less than
    #       the smallest `n`-digit number, (10^(n-1) - 1).
    #     Find the lowest such `n` and figure out the upper limit.

    n = 2  # Number of digits being considered
    while True:
        max_achievable_sum = n * (9 ** p)  # Sum of `p`th powers of 99...9 (n times)
        n_dig_lo = 10 ** (n - 1)
        n_dig_hi = 10 ** n - 1
        if n_dig_lo <= max_achievable_sum < n_dig_hi:
            break
        else:
            n += 1
    return max_achievable_sum


def main(p):
    """
    Returns an ordered list of the numbers that
      can be written as the sum of the `p`th power of their digits,
      as well as the sum of these numbers.
    Note that single-digit numbers (specifically 1) do not count.

    Args:
        p (int): Natural number

    Returns:
        List[int] of numbers equalling sum of `p`th power of their digits,
          and the sum of these numbers

    Raises:
        AssertError: if any incorrect args are given
    """
    assert type(p) == int and p > 0

    # First establish the upper limit
    # Lower limit will simply be 10, as single-digits aren't allowed
    upper_limit = calc_upper_limit(p)

    # Store `p`th powers for convenience
    digit_powers = [(i ** p) for i in range(10)]

    dig_pow_nums = []
    dig_pow_sum_full = 0
    for x in range(10, upper_limit+1):
        dig_pow_sum = sum(map(lambda d: digit_powers[int(d)], list(str(x))))
        if dig_pow_sum == x:
            dig_pow_nums.append(x)
            dig_pow_sum_full += x

    return dig_pow_nums, dig_pow_sum_full


if __name__ == '__main__':
    digit_power = int(input('Enter a natural number: '))
    digit_power_nums, digit_power_sum = main(digit_power)
    print('Sum of all numbers equalling sum of {} power of their digits:'.format(num2words(digit_power)))
    print('  {}'.format(digit_power_sum))
    print('Numbers producing that sum:')
    for num in digit_power_nums:
        print('  {}'.format(num))

from math import log

rt5 = 5 ** .5
phi = (1 + rt5) / 2

########Sublinear Time Solution##########

def generous_0(total_lambs):
    # the remainder correction below can't work if henchmen is 2 or less
    if total_lambs < 3: return total_lambs
    # the inverse of the formula for the geometric sum with 2 as the multiplier
    henchmen = int(log((total_lambs), 2))
    # we can still distribute lambs if our shortfall of the next
    # power of two is greater than the sum of the last two powers of two
    if total_lambs - 2 ** henchmen + 1 >= 2 ** (henchmen - 1) + 2 ** (henchmen - 2):
        return henchmen + 1
    else:
        return henchmen


def fibonacci_sum(n):
    return round(phi ** (n + 2) / rt5) - 1


def stingy_0(total_lambs):
    # the inverse of the formula for the sum of the fibonacci series at n
    henchmen = round(log(rt5 * (total_lambs + 1), phi)) - 2
    # did we overshoot?
    if fibonacci_sum(henchmen) > total_lambs:
        return henchmen - 1
    else:
        return henchmen


def answer_0(total_lambs):
    return stingy_0(total_lambs) - generous_0(total_lambs)


########Linear Time Solution##########

def fibonacci():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b


def powers_of_two():
    a = 0
    while True:
        yield 2 ** a
        a += 1


def generous(total_lambs):
    if total_lambs < 3: return total_lambs
    running_sum = 0
    for i, p in enumerate(powers_of_two()):
        if running_sum + p < total_lambs:
            running_sum += p
        else:
            if (total_lambs - running_sum) >= (2 ** (i - 2) + 2 ** (i - 1)):
                return i + 1
            else:
                return i


def stingy(total_lambs):
    running_sum = 0
    for i, f in enumerate(fibonacci()):  # start counting i = 0, b = 1
        if running_sum + f <= total_lambs:
            running_sum += f
        else:
            return i


def answer(total_lambs):
    return stingy(total_lambs) - generous(total_lambs)
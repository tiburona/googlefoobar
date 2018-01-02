def answer(M, F):
    m = int(M)
    f = int(F)

    cycles = 0
    bombs_array = [m, f]

    while True:

        if 1 in bombs_array:
            if m == 1:
                cycles += f - 1
            if f == 1:
                cycles += m - 1
            return cycles

        quotient = max(bombs_array) // min(bombs_array)

        if m == max(bombs_array):
            m -= quotient * f
        else:
            f -= quotient * m

        bombs_array = [m, f]
        cycles += quotient

        if len([b for b in bombs_array if b < 1]) > 0:
            break

    return 'impossible'
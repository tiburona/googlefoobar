
def calc_distances(pegs):
    return [pegs[i + 1] - peg for i, peg in enumerate(pegs[0:-1])]


def coeffs_in_eq_for_first_radius(distances):
    # in terms of the last radius
    zero_order_coeff = sum([distance if i % 2 == 0 else -distance for i, distance in enumerate(distances)])
    first_order_coeff = 1 if len(distances) % 2 == 0 else -1
    return [zero_order_coeff, first_order_coeff]


def first_radius(zeroth, first):
    # substitute first radius / 2 for last radius and solve
    return 2 * zeroth if first == 1 else 2 * zeroth / 3


def calc_radii(distances, initial_radius):
    radii = [initial_radius]
    for i, distance in enumerate(distances):
        next_radius = distance - radii[i]
        radii.append(next_radius)
    return radii


def invalid(distances, zeroth, first):
    return any(radius < 1 for radius in calc_radii(distances, first_radius(zeroth, first)))


def answer(pegs):
    peg_distances = calc_distances(pegs)
    zeroth, first = coeffs_in_eq_for_first_radius(peg_distances)
    if invalid(peg_distances, zeroth, first):
        return [-1, -1]
    if first == 1:
        return [2 * zeroth, 1]
    else:
        return [2 * zeroth / 3, 1] if zeroth % 3 == 0 else [2 * zeroth, 3]
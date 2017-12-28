# a solution to the_grandest_staircase_of_them_all on google foobar
# the problem given involves finding the number of staircases you can build with a given number of bricks, but a way to
# state this in more mathematically conventional terms is find the number of integer partitions of a given argument only
# using unique integers

memo = {1: [[1]], 2: [[2]]}

# A function that lists all the possible integer partitions/staircases to help me check my values below

def partitions_from_unique_integers(n):
    if n in memo.keys(): return memo[n]
    arr_to_return = []

    for h in range(1, n):
        if not n-h in memo.keys():
            memo[n-h] = partitions_from_unique_integers(n-h)
        for arr in memo[n-h]:
            if h > max(arr):
                arr_to_return.append([h] + arr)

    arr_to_return.append([n])
    memo[n] = arr_to_return
    return memo[n]

print(partitions_from_unique_integers(10))

# count_memo is a dictionary with the integer argument we're partitioning as the keys. Each of these arguments is then
# associated with another dictionary with the maximum integer in the partition as the key. The values are the counts of
# the number of partitions for each integer argument with each maximum value
count_memo = { 1: {1: 1}, 2: {2: 1} }

def num_partitions_from_unique_integers(n):
    if n in count_memo.keys(): return count_memo[n]
    count_memo[n] = { n: 1 } # every integer can have 1 partition of itself

    # loop over the integers less than n
    for h in range(1, n):
        # recursively populate count_memo
        if not n - h in count_memo:
            count_memo[n - h] = num_partitions_from_unique_integers(n - h)
        # take the difference of the current integer (h) and n
        # we're adding to the count for number of partitions of n with max h the number to add to the count is the
        # number of partitions of n - h that have a max integer less than h
        # (the max integer less than h criterion prevents duplicate integers as well as partition that are identical to
        # others, but with the orders reversed)
        for mx in count_memo[n - h]:
            cnt = count_memo[n - h][mx]
            if mx < h:
                if n not in count_memo:
                    count_memo[n] = { h: cnt }
                else:
                    if h not in count_memo[n]: count_memo[n][h] = cnt
                    else: count_memo[n][h] += cnt
    return count_memo[n]

def answer(n):
    cnt_dict = num_partitions_from_unique_integers(n)
    return sum([cnt_dict[key] for key in cnt_dict]) - 1 # the partition of itself is not a staircase; it has one level

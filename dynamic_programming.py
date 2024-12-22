def add_until_100(array):
    if not array:
        return 0
    until_100 = add_until_100(array[1:])
    if array[0] + until_100 > 100:
        return until_100
    else:
        return array[0] + until_100


def golomb(n, memo):
    if n == 1:
        return 1
    if n not in memo:
        memo[n] = 1 + golomb(n - golomb(golomb(n - 1, memo), memo), memo)
    return memo[n]


def unique_paths(rows, coloumns, memo):
    if rows == 1 or coloumns == 1:
        return 1
    if (rows, coloumns) not in memo:
        memo[(rows, coloumns)] = unique_paths(rows - 1, coloumns, memo) + unique_paths(
            rows, coloumns - 1, memo
        )
    return memo[(rows, coloumns)]

# Returns the largest A & B below K in constant time: the answer is K - 1 when (K - 1) |
# K still fits within N, otherwise it falls back to K - 2.

def bitwiseAnd(N, K):

    target = K - 1

    optimal_B = target | K
    if optimal_B <= N:
        return target
    else:
        return K - 2
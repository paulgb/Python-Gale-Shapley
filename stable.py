

def stable(rankings, A, B):
    r"""
    rankings[(a, n)] = partner that a ranked n^th

    >>> from itertools import product
    >>> A = ['1','2','3','4','5','6']
    >>> B = ['a','b','c','d','e','f']
    >>> rank = dict()
    >>> rank['1'] = (1,4,2,6,5,3)
    >>> rank['2'] = (3,1,2,4,5,6)
    >>> rank['3'] = (1,2,4,3,5,6)
    >>> rank['4'] = (4,1,2,5,3,6)
    >>> rank['5'] = (1,2,3,6,4,5)
    >>> rank['6'] = (2,1,4,3,5,6)
    >>> rank['a'] = (1,2,3,4,5,6)
    >>> rank['b'] = (2,1,4,3,5,6)
    >>> rank['c'] = (5,1,6,3,2,4)
    >>> rank['d'] = (1,3,2,5,4,6)
    >>> rank['e'] = (4,1,3,6,2,5)
    >>> rank['f'] = (2,1,4,3,6,5)
    >>> Arankings = dict(((a, rank[a][b_]), B[b_]) for (a, b_) in product(A, range(0, 6)))
    >>> Brankings = dict(((b, rank[b][a_]), A[a_]) for (b, a_) in product(B, range(0, 6)))
    >>> rankings = Arankings
    >>> rankings.update(Brankings)
    >>> stable(rankings, A, B)
    [('1', 'a'), ('2', 'b'), ('3', 'd'), ('4', 'f'), ('5', 'c'), ('6', 'e')]

    """
    partners = dict((a, (rankings[(a, 1)], 1)) for a in A)
    is_stable = False # whether the current pairing (given by `partners`) is stable
    while is_stable == False:
        is_stable = True
        for b in B:
            is_paired = False # whether b has a pair which b ranks <= to n
            for n in range(1, len(B) + 1):
                a = rankings[(b, n)]
                a_partner, a_n = partners[a]
                if a_partner == b:
                    if is_paired:
                        is_stable = False
                        partners[a] = (rankings[(a, a_n + 1)], a_n + 1)
                    else:
                        is_paired = True
    return sorted((a, b) for (a, (b, n)) in partners.items())



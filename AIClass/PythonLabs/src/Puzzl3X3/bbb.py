import numpy as np
from copy import deepcopy
from collections import defaultdict

def mhd(s, g):
    return sum((abs(s // 3 - g // 3) + abs(s % 3 - g % 3))[1:])

def coor(s):
    c = np.array(range(9))
    for x, y in enumerate(s):
        c[y] = x
    return c

def solve(board, goal):
    moves = np.array(
        [
            ('u', [0, 1, 2], -3),
            ('d', [6, 7, 8], 3),
            ('l', [0, 3, 6], -1),
            ('r', [2, 5, 8], 1)
        ],
        dtype=[
            ('move', str, 1),
            ('pos', list),
            ('delta', int)
        ]
    )

    STATE = [
        ('board', list),
        ('parent', int),
        ('gn', int),
        ('hn', int)
    ]

    PRIORITY = [
        ('pos', int),
        ('fn', int)
    ]

    previous_boards = defaultdict(bool)

    goalc = coor(goal)
    hn = mhd(coor(board), goalc)
    state = np.array([(board, -1, 0, hn)], STATE)
    priority = np.array( [(0, hn)], PRIORITY)

    while True:
        priority = np.sort(priority, kind='mergesort', order=['fn', 'pos'])
        pos = priority[0][0]
        priority = np.delete(priority, 0, 0)
        board = state[pos][0]
        gn = state[pos][2] + 1
        loc = int(np.where(board == 0)[0])

        for m in moves:
            if loc not in m['pos']:
                succ = deepcopy(board)
                delta_loc = loc + m['delta']
                succ[loc], succ[delta_loc] = succ[delta_loc], succ[loc]
                succ_t = tuple(succ)

                if previous_boards[succ_t]:
                    continue

                previous_boards[succ_t] = True

                hn = mhd(coor(succ_t), goalc)
                state = np.append(
                    state,
                    np.array([(succ, pos, gn, hn)], STATE),
                    0
                )
                priority = np.append(
                    priority,
                    np.array([(len(state) - 1, gn + hn)], PRIORITY),
                    0
                )

                if np.array_equal(succ, goal):
                    return state, len(priority)

def inversions(s):
    k = s[s != 0]
    return sum(
        len(np.array(np.where(k[i+1:] < k[i])).reshape(-1))
        for i in range(len(k) - 1)
    )

def genoptimal(state):
    optimal = np.array([], int).reshape(-1, 9)
    last = len(state) - 1
    while last != -1:
        optimal = np.insert(optimal, 0, state[last]['board'], 0)
        last = int(state[last]['parent'])
    return optimal.reshape(-1, 3, 3)

def main():
    print()
    goal = np.array([1, 2, 3, 4, 5, 6, 7, 8, 0])
    string = input('Enter board: ')
    board = np.array(list(map(int, string)))

    if sorted(string) != sorted('012345678'):
        print('incorrect input')
        return
    if inversions(board) % 2:
        print('not solvable')
        return

    state, explored = solve(board, goal)
    optimal = genoptimal(state)

    print((
        'Goal achieved!\n'
        '\n'
        'Total generated: {}\n'
        'Total explored:  {}\n'
        '\n'
        'Total optimized steps: {}\n'
        '{}\n'
        '\n'
    ).format(len(state), len(state) - explored, len(optimal) - 1, optimal))

if __name__ == '__main__':
    main()
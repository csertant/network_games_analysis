"""
Test script for rotation.
"""


def rotate(state, n, is_row):
    rowOrCol = [0, 0, 0]
    if is_row:
        rowOrCol = state[n]
        temp = rowOrCol[0]
        for i in range(2):
            rowOrCol[i] = rowOrCol[i + 1]
        rowOrCol[2] = temp
        state[n] = rowOrCol
    else:
        for i in range(3):
            rowOrCol[i] = state[i][n]
        temp = rowOrCol[0]
        for j in range(2):
            rowOrCol[j] = rowOrCol[j + 1]
        rowOrCol[2] = temp
        for k in range(3):
            state[k][n] = rowOrCol[k]
    return


def main():
    state = [[1, 1, 0], [1, 1, 0], [0, 1, 1]]

    for i in range(3):
        rotate(state, i, True)

    print(state)

    for j in range(3):
        rotate(state, j, False)

    print(state)

    state = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

    rotate(state, 2, True)
    rotate(state, 2, True)
    rotate(state, 2, True)
    print(state)


if __name__ == '__main__':
    main()

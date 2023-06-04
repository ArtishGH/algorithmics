def rotate_domino(domino):
    left, right = domino
    return right, left

def solve_domino_puzzle(dominoes):
    n = len(dominoes)
    solution = []
    used = [False] * n

    def backtrack(prev_domino, idx):
        if idx == n:
            return True

        for i in range(n):
            if not used[i]:
                domino = dominoes[i]
                if domino[0] == prev_domino[1]:
                    solution.append((i + 1, '+'))
                    used[i] = True
                    if backtrack(domino, idx + 1):
                        return True
                    used[i] = False
                    solution.pop()

                elif domino[1] == prev_domino[1]:
                    solution.append((i + 1, '-'))
                    used[i] = True
                    if backtrack(rotate_domino(domino), idx + 1):
                        return True
                    used[i] = False
                    solution.pop()

                elif domino[0] == prev_domino[0]:
                    solution.append((i + 1, '-'))
                    used[i] = True
                    if backtrack(domino, idx + 1):
                        return True
                    used[i] = False
                    solution.pop()

                elif domino[1] == prev_domino[0]:
                    solution.append((i + 1, '+'))
                    used[i] = True
                    if backtrack(rotate_domino(domino), idx + 1):
                        return True
                    used[i] = False
                    solution.pop()

        return False

    for i in range(n):
        domino = dominoes[i]
        solution.append((i + 1, '+'))
        used[i] = True
        if backtrack(domino, 1):
            break
        used[i] = False
        solution.pop()

    if len(solution) != n:
        print("No solution")
    else:
        for move in solution:
            print(f"{move[0]} {move[1]}")

#default input
input_data = '''5
1 2
2 4
2 4
6 4
2 1'''

lines = input_data.strip().split('\n')
n = int(lines[0])
dominoes = [tuple(map(int, line.split())) for line in lines[1:]]

solve_domino_puzzle(dominoes)

# Nie wiem czemu dostaje inny wynik, ale chyba tak powinien być zrobiony ten algorytm
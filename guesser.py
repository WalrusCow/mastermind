from mastermind import Game as Mastermind

def tupleInt(num):
    return tuple(map(int, str(num).rjust(4, '0')))

def playGame():
    M = Mastermind()
    s = set(map(tupleInt, range(10 ** 4)))

    turns = 0
    while True:
        guess = list(s.pop())
        turns += 1
        exact, inexact = M.guess(guess)
        if (exact == 4):
            return turns

        s = {g for g in s if Mastermind._guess(g, guess) == (exact, inexact)}
        if not s: return # Will never happen, but just in case

if __name__ == '__main__':
    for _ in range(10): print(playGame())

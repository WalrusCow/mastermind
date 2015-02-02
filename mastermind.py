from collections import Counter
from random import randrange

class Game:
    def __init__(self, maxNum=9, numSecrets=4):
        self._numSecrets = numSecrets
        self._maxNum = maxNum
        self._secret = self._genSecret()

    def _genSecret(self):
        return [randrange(0, self._maxNum + 1)
                for _ in range(self._numSecrets + 1)]

    def guess(self, guess):
        # Returns (exact, inexact)
        exact = 0
        secret = self._secret[::]
        for i, (g, s) in enumerate(zip(guess[::], self._secret)):
            if g != s: continue
            # Well, we are kinda modifying lists as we go through them
            # which is generally a bad idea...
            secret.pop(i - exact)
            guess.pop(i - exact)
            exact += 1

        secretCount = Counter(secret)
        guessCount = Counter(guess)

        inexact = sum(min(guessCount[k], secretCount[k]) for k in guessCount)
        return exact, inexact

from collections import Counter
from random import randrange

class Game:
    def __init__(self, maxNum=9, numSecrets=4, secret=None):
        self._numSecrets = numSecrets
        self._maxNum = maxNum
        if secret is None:
            self._secret = self._genSecret()
        else:
            self._secret = list(secret)

    def _genSecret(self):
        return [randrange(0, self._maxNum + 1) for _ in range(self._numSecrets)]

    def unwrapInt(self, num):
        return list(map(int, str(num).rjust(self._numSecrets, '0')))

    @staticmethod
    def _guess(secret, guess):
        # Returns (exact, inexact)
        guess = list(guess)
        secret = list(secret)

        exact = 0
        for i, (g, s) in enumerate(zip(guess[::], secret[::])):
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

    def guess(self, guess):
        # Returns (exact, inexact)
        return Game._guess(self._secret, guess)

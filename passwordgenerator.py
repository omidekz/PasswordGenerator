from random import randint as ri, sample, shuffle


class PasswordGenerator:
    smalls = list(map(chr, range(ord('a'), ord('z') + 1)))
    capitals = list(map(chr, range(ord('A'), ord('Z') + 1)))
    characters = ['@', '#', '&', '!', '$', '%', '^', '*', '(', ')', '-', '?', '.', ',', ';', ':', '[', ']', '{', '}',
                  '/',
                  '\\', '`', '~', '+', '=']
    MAX_LENGTH = 32
    MIN_LENGTH = 16
    BAD_MESSAGE = 'PLZ-gENeRAtE-PASsWORd'

    def __init__(self, min_length=MIN_LENGTH, max_length=MAX_LENGTH):
        # make a random length between min, max length
        length = ri(min_length, max_length)

        # arrange length for smalls
        self._small_length = length // 2
        length -= self._small_length

        # arrange length for capitals
        self._capital_length = (3 * length) // 4
        length -= self._capital_length

        # arrange length for characters
        self._character_length = length
        self.__password = list()
        self._str_password = PasswordGenerator.BAD_MESSAGE

    def generate(self):
        if self._str_password != PasswordGenerator.BAD_MESSAGE:
            return self._str_password
        # shuffle the list for get best randoms
        shuffle(self.smalls)
        shuffle(self.capitals)
        shuffle(self.characters)

        # select random choices from the list by sample method
        self.__password.extend(sample(PasswordGenerator.smalls, self._small_length))
        self.__password.extend(sample(PasswordGenerator.capitals, self._capital_length))
        self.__password.extend(sample(PasswordGenerator.characters, self._character_length))

        # shuffle the password list
        shuffle(self.__password)
        self._str_password = ''.join([p for p in self.__password])
        return self._str_password

    def get_password(self):
        return self._str_password

    def __str__(self):
        return self._str_password

    def __repr__(self):
        return self.get_password()


def main():
    pass


if __name__ == '__main__':
    main()

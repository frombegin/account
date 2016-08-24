import random


class Generator:
    def generate_mvcode(self, max_length=4):
        """
        :param max_length:
        :return:
        """


class RandomNumberGenerator(Generator):
    def generate_mvcode(self, max_length=4):
        return str(random.randint(10**(max_length-1), 10**max_length-1))

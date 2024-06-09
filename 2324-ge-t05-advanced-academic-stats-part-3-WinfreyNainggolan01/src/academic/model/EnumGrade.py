from enum import Enum

class EnumGrade(Enum):
    A = ("A", 4.0)
    AB = ("AB", 3.5)
    B = ("B", 3.0)
    BC = ("BC", 2.5)
    C = ("C", 2.0)
    D = ("D", 1.0)
    E = ("E", 0.0)
    T = ("None", 0.0)

    def __init__(self, letter, value):
        self._letter = letter
        self._value = value

    def value(self):
        return self._value

    def letter(self):
        return self._letter

    @staticmethod
    def get_scale(letter):
        for grade in EnumGrade:
            if grade.letter == letter:
                return grade.value
        return -1

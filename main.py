import csv

# import random
import string
from typing import List

# import itertools

# 1. Генератор випадкових слів
# def generator_word(words_len):
#     leterrs_and_digits = list(string.ascii_lowercase) + list(string.digits)
#     new_word = ''
#     while len(new_word) < words_len:
#         new_word += leterrs_and_digits[random.randint(0, len(leterrs_and_digits)-1)]
#     yield new_word
#
#
# def generator_list_of_words(words_len, amount):
#     return [next(generator_word(words_len)) for _ in range(amount)]
#
# print(generator_list_of_words(4, 4))


# 2. Генератор за допомогою itertools
# def generator_words(words_len: int, amount: int) -> List[str]:
#     # result = list(map("".join, itertools.product(
#     string.ascii_lowercase + string.digits, repeat=words_len))
#     )[0:amount]
#     return list(map("".join, itertools.product(string.ascii_lowercase + string.digits, repeat=words_len)))[0:amount]
#


# 3. Мій генератор
def generator_words(words_len: int, amount: int) -> List[str]:
    letters_and_digits: list = list(string.ascii_lowercase) + list(string.digits)
    result = []
    index = -1
    while len(result) < amount:
        try:
            index += 1
            i = 0
            while (words_len - i) != 0 and len(result) < amount:
                result.append(
                    letters_and_digits[index] * (words_len - i)
                    + letters_and_digits[index + 1] * (words_len - (words_len - i))
                )
                i += 1
        except IndexError:
            result.append(letters_and_digits[index] * words_len)
            break
    with open("genetator_data.csv", "w") as f:
        writer = csv.writer(f)
        for row in result:
            writer.writerow(row)

    return ...


def read_words(words_len: int, amount: int):
    generator_words(words_len=words_len, amount=amount)
    with open("genetator_data.csv") as f:
        return f.read()


if __name__ == "__main__":
    print(read_words(int(input("Length of words : ")), int(input("Words amount: "))))

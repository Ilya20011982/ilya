# A durak deck contains 36 cards. Each card has a suit of either clubs, diamonds, hearts, or spades
# (denoted C, D, H, S). Each card also has a value of either 6 through 10, jack, queen, king, or ace
# (denoted 6, 7, 8, 9, 10, J, Q, K, A). For scoring purposes card values are ordered as above, with 6
#     having the lowest and ace the highest value.
# Напишите программу, которая определяет, бьёт ли одна карта другую.
# Если встречаются две карты одной масти, то побеждает та, у которой выше значение;
# Если карты разных мастей, то карта, имеющая козырную масть, побеждает;
# Если карты разных мастей и нет козырных, то никто не побеждает.
# Формат ввода:
# На первой строке через пробел указываются две карты в формате <значение><масть>, а на следующей строке
# указывается козырная масть.
# Формат вывода:
# Программа должна вывести слово
# First, если первая карта бьёт вторую,
# Second, если вторая карта бьёт первую,
# Error, если ни одна из карт не может побить другую.

cards = {'6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
first_card, second_card = input().split()
trump = input()

if first_card[-1] != second_card[-1] and first_card[-1] != trump and second_card[-1] != trump:
    print('Error')
elif first_card[-1] != second_card[-1]:
    if first_card[-1] == trump:
        print('First')
    elif second_card[-1] == trump:
        print('Second')
elif first_card[-1] == second_card[-1]:
    if cards[first_card[:-1]] > cards[second_card[:-1]]:
        print('First')
    elif cards[first_card[:-1]] < cards[second_card[:-1]]:
        print('Second')
    elif cards[first_card[:-1]] == cards[second_card[:-1]]:
        print('Error')


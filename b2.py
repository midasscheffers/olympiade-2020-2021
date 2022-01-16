# mijn woorden: ["AARD", "BETERS", "CALCULATOR", "DARMEN", "ELF", "FONT", "GESTEUND", "HERHALING", "IMPASSE", "JACHT", "KON", "LICHTING", "METHODES", "NIEUW", "OVERLEVEN", "PRO", "QUA", "RIJKAARD", "STIJGENDE", "TERMIJN", "UITKERING", "VERBLIJVEN", "WURM", "VERZINNEN", "VERZOEK", "SYSTEMEN", "VERZEKERT", "COMPLEXER", "DYNAMISCH", "ZAT"]


WOORDEN = ["AARD", "BETERS", "CALCULATOR", "DARMEN", "ELF", "FONT", "GESTEUND", "HERHALING", "IMPASSE", "JACHT", "KON", "LICHTING", "METHODES", "NIEUW", "OVERLEVEN", "PRO", "QUA", "RIJKAARD", "STIJGENDE", "TERMIJN", "UITKERING", "VERBLIJVEN", "WURM", "VERZINNEN", "VERZOEK", "SYSTEMEN", "VERZEKERT", "COMPLEXER", "DYNAMISCH", "ZAT"]

ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def woorden_met_letter(l, woorden):
    temp_w = []
    for w in woorden:
        if l in w:
            temp_w.append(w)
    return temp_w


def letters_in_word(wrd):
    letters = []
    for letter in wrd:
        if letter not in letters:
            letters.append(letter)
    return letters


def list_delete_list(list1, list2):
    temp = list1[:]
    for item in list2:
        if item in list1:
            temp.remove(item)
    return temp


def score(list):
    return 100*len(list) + len("".join(list))


def minste_woorden_met_alpha(woorden, alphabet, depth, words_looked):
    temp = []
    if alphabet == [] or woorden == []:
        return (score(words_looked), words_looked)
    w_met_alpha = woorden_met_letter(alphabet[0], woorden)
    for w in w_met_alpha:
        new_alfa = list_delete_list(alphabet, letters_in_word(w))
        new_woorden = list_delete_list(woorden, [w])
        next_step = minste_woorden_met_alpha(new_woorden, new_alfa, depth+1, words_looked+[w])
        temp.append(next_step)

    return min(temp)


print(minste_woorden_met_alpha(WOORDEN, ALPHABET, 0, []))

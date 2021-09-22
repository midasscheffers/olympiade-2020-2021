

inp = input()

punten = {"1":1, "2":2, "3":3, "4":4, "5":5, "w":5}

def letter_in_word(wrd):
    letters = []
    for letter in wrd:
        letter_in_letters = False
        for i in range(len(letters)):
            if letters[i][0] == letter:
                letter_in_letters = True
        if not letter_in_letters:
            letters.append([letter, wrd.count(letter)])
    return letters


def punten_voor_str(str):
    totaal = 0
    for letter in str:
        if letter in punten:
            totaal += punten[letter]
    return totaal


def max_punten_voor_worp(worp, nog_gooien, w_w_gelegd, letters_al_gegooid):
    if worp == "" or nog_gooien == 0:
        if not w_w_gelegd:
            return -40
        return 0
    
    lis = []
    te_worp = worp[:nog_gooien]
    let_in_te_worp = letter_in_word(te_worp)
    for i in range(len(let_in_te_worp)):
        if let_in_te_worp[i][0] not in letters_al_gegooid:
            n_gooien = nog_gooien - let_in_te_worp[i][1]
            if let_in_te_worp[i][0] == "w":
                w_gelegd = True
            else:
                w_gelegd = w_w_gelegd
            let_geg = letters_al_gegooid + [let_in_te_worp[i][0]]
            lis.append(punten_voor_str(let_in_te_worp[i][0] * let_in_te_worp[i][1]) + max_punten_voor_worp(worp[nog_gooien:], n_gooien, w_gelegd, let_geg))
    if len(lis) > 0:
        max_punt = max(lis)
    else:
        max_punt = 0
    return max_punt


print(max_punten_voor_worp(inp, 8, False, []))
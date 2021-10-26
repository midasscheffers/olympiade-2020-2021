

N, M = [int(i) for i in list(input().split(" "))]

trains = []

for i in range(M):
    trains.append([i] + [int(i) for i in list(input().split(" "))])

print(trains)

def trains_in_list(wrd):
    trains = []
    for letter in wrd:
        letter_in_letters = False
        for i in range(len(trains)):
            if trains[i][0] == letter:
                letter_in_letters = True
        if not letter_in_letters:
            trains.append([letter, wrd.count(letter)])
    return trains


def overstap_mogelijkheden(station, trains):
    trains_on_station = []
    for t in trains:
        if station in range(t[1], t[2]):
            trains_on_station.append(t)
    return trains_on_station


def propagate(paths, trains, N):
    temp_paths = []
    for p in paths:
        ovm = overstap_mogelijkheden(N, trains)
        n_paths = []
        #check all possible paths and ad the ones thet meet the conditions
        for t in ovm:
            if trains[p[-1]][-1] >= N:
                if t[1] >= trains[p[-1]][1]:
                    if t[0] == p[-1]:
                        n_p = p + [t[0]]
                        n_paths.append(n_p)
                    elif not t[0] in p[:-1]:
                        n_p = p + [t[0]]
                        temp_paths.append(n_p)
                    else:
                        temp_paths.append(p)
        temp_paths.append(p)

        # print(paths, n_paths, "differ")
        # for pn in n_paths:
        #     temp_paths.append(pn)
        # print(paths, n_paths, 'is update')
        # paths.remove(p)
    return temp_paths

    

paths = []
# init paths
for t in overstap_mogelijkheden(1, trains):
    paths.append([t[0]])

print(paths)
#propagate paths

for i in range(1, N):
        paths = propagate(paths, trains, i)

# print(overstap_mogelijkheden(1, trains))

print(paths)
longest = 0
for p in paths:
    l = len(trains_in_list(p))
    if l > longest:
        longest = l

print(longest)


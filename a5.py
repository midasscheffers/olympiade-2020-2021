

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


def clean_paths(paths):
    new_paths = []
    for p in paths:
        if not p in new_paths:
            new_paths.append(p)
    return new_paths


def split_lists_in_len(list):
    ret_list = []
    for i in list:
        try:
            ret_list[len(i) - 1].append(i)
        except:
            array_difference =  len(i) - len(ret_list)
            for _ in range(array_difference):
                ret_list.append([])
            ret_list[len(i) - 1].append(i)
    return ret_list

def filter_different_endings(list_of_lists):
    endings = []
    temp = []
    for l in list_of_lists:
        if not l[-1] in endings:
            endings.append(l[-1])
            temp.append(l)
        
    return temp

def remove_overhead(paths):
    temp = []
    sorted_by_len = split_lists_in_len(paths)
    for l in sorted_by_len:
        filter_different_endings(l)
        temp.append(l[0])
    return temp


def overstap_mogelijkheden(station, trains):
    trains_on_station = []
    for t in trains:
        if station in range(t[1], t[2]):
            trains_on_station.append(t)
    return trains_on_station


def propagate(paths, trains, N):
    new_paths = []
    for p in paths:
        if trains[p[-1]][-1] >= N:
            ovm = overstap_mogelijkheden(N, trains)
            #check all possible paths and ad the ones thet meet the conditions
            for t in ovm:
                if t[1] >= trains[p[-1]][1]:
                    if not t[0] in p:
                        n_p = p + [t[0]]
                        new_paths.append(n_p)


    return paths + new_paths

    
paths = []
# init paths
for t in overstap_mogelijkheden(1, trains):
    paths.append([t[0]])

#propagate paths
for i in range(1, N):
        paths = propagate(paths, trains, i)
        # print(paths)
        paths = remove_overhead(paths)
        # print(paths)

longest = 0
for p in paths:
    l = len(trains_in_list(p))
    if l > longest:
        longest = l

print(longest)


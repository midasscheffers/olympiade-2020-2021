


# read input

N, M = [int(i) for i in list(input().split(" "))]

trains = []

for i in range(M):
    trains.append([i] + [int(i) for i in list(input().split(" "))])


def most_trains(trains):
    optimal_path = [] # path with most different trains

    return optimal_path
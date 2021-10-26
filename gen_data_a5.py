
import random as r

N, M = [int(i) for i in list(input().split(" "))]

trains = []

for i in range(M):
    r_fisrt_station = r.randint(1, N-1)
    r_second_station = r.randint(r_fisrt_station+1, N)
    print(str(r_fisrt_station) + " " + str(r_second_station))
    trains.append([i, r_fisrt_station, r_second_station])

print(trains)
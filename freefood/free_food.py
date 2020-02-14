import sys
def main():
    data = sys.stdin.readlines()
    n = 0
    event_times = []
    already_used = set()
    for i in range(len(data)):
        if i == 0: n = int(data[i])
        else:
            start_end = data[i].split()
            tup = (int(start_end[0]), int(start_end[1]))
            event_times.append(tup)
    total = 0
    for j in range(n):
        start, end = event_times[j][0], event_times[j][1]
        for day in range(start, end+1):
            if day not in already_used:
                total += 1
                already_used.add(day)
    print(total)

main()

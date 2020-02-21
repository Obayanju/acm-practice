import sys
def main():
    data = sys.stdin.readlines()
    for i in range(len(data)):
        line = data[i].split()
        time1, time2 = line[3], line[4]
        time1_li = time1.split(':')
        time1_li = [int(v) for v in time1_li]
        time2_li = time2.split(':')
        time2_li = [int(v) for v in time2_li]
        hrs, minutes = 0, 0
        if time1_li[1] > time2_li[1]:
            hrs = abs(time1_li[0]-time2_li[0])-1
            minutes = 60 - time1_li[1] + time2_li[1] 
        else:
            hrs = abs(time1_li[0]-time2_li[0])
            minutes = abs(time1_li[1]-time2_li[1])
        print(line[0], line[1], line[2], hrs, "hours", minutes , "minutes")
main()

import sys
def main():
    # d = s*t
    '''
    store speed and time in separate lists
    '''
    data = sys.stdin.readlines()
    i = 0
    size = len(data)
    while i < size-1:
        n = int(data[i])
        miles = 0
        total_time = 0
        times = [0]
        #print(n)
        for j in range(i+1, i+1+n):
           #print(j)
           s_t = data[j].split()
           speed, time = int(s_t[0]), int(s_t[1])
           #print(speed, time)
           curr_mile = speed * (abs(time-times[-1]))
           miles += curr_mile
           total_time += time 
           times.append(time)
        print(miles, "miles")
        i = i+1+n
    
main()

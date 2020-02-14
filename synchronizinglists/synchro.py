import sys

def main():
    data = sys.stdin.readlines()
    my_list = []
    i = 0
    while i < len(data)-1:
        size = int(data[i])
        li = []
        for j in range(i+1, i+(2*size+1)):
           li.append(int(data[j]))
        my_list.append(li[:])
        i = j+1
    n = 0
    for li in my_list:
        first_list, second_list = [], []
        for i in range(len(li)//2): first_list.append(li[i]) 
        for j in range(len(li)//2, len(li)): second_list.append(li[j]) 
        sorted_first_list = sorted(first_list)
        sorted_second_list = sorted(second_list)
        pair = {}
        for k in range(len(sorted_first_list)):
            pair[sorted_first_list[k]] = sorted_second_list[k]
        for num in first_list:
            print(pair[num])
        n += 1
        print('\n') if n < len(my_list) else print('')
main()

import sys

'''
how to determine class level
convert class to its actual class
pick a class and check all other classes
    loop from back on both classes
    if equal, rank alphabetically
    once we find a higher class, we have found our higher class
    if an higher class isn't found, pick the one the the higher number
    of classes
'''

def convert_class(li):
    li = li.split('-')
    out = []
    for i in range(len(li)-1):
        out.append(1)
        char = li[i+1][0]
        if char == 'l':
            out.append(0)
        elif char == 'm':
            out.append(1)
        else:
            out.append(2)

    char = li[-1][0]
    if char == 'l':
        out.append(0)
    elif char == 'm':
        out.append(1)
    else:
        out.append(2)
    return out
    
def rank_classes(li):
    out = [None]*len(li)
    size = len(li)
    for i in range(size):
        for j in range(size):
            if i != j:
                l1, l2 = li[i][1], li[j][1]
                if l1 == l2 and l1[0] < l2[0]:
                    out[j] = l1[:]
                else:
                    s1, s2 = len(l1), len(l2)
                    c1, c2 = l1, l2
                    found = False
                    while s1 >= 0 and s2 >= 0 and not found: 
                        if c1[s1] > c2[s2]:
                            out[j] = c1
                            found = True
                        elif c1[s1] < c2[s2]:
                            out[j] = c2
                            found = True
                        s1 -= 1 ; s2 -= 1

                    if not found:
                        if s1 > s2:
                            out[j] = c1
                        else:
                            out[j] = c2
    return out

def main():
    data = sys.stdin.readlines()
    k = 1 
    names = []
    classes = []
    for i in range(int(data[0])):
        n = int(data[k])
        class_pos = []
        for j in range(k+1, k+n+1):
            l = 0
            line = data[j]
            name = ''
            while line[l] != ':':  
                name += line[l]
                l += 1
            class_pos.append(l+1)
            names.append(name)
            size = len(data[j])
            classes.append((name, convert_class(data[j][l+1:size-6])))
        k = j+1
    rank_classes(classes)



main()

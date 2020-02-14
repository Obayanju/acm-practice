import sys

def main():
    '''
    primary measure -> number of problems solved
    secondary measure -> time and penalties
    score = times_right_answer + 20min for penalty_wrong_sub_that_eventually_solved
    '''
    data = sys.stdin.readlines()
    log_entry = []
    for line in data:
        line = line.split()
        if len(line) != 1:
            solved = line.pop()
            number = line.pop()
            time_taken = line.pop()
            log_entry.append((time_taken, number, solved))
    
    stack = [item[1] for item in log_entry]
    stack = list(set(stack))
    stack.sort()
    
    solved = set() 
    for entry in log_entry:
        if not entry[1] in solved and entry[2] == 'right':
            solved.add(entry[1])
    
    entered, score = set(), 0
    for entry in log_entry:
        if entry[1] in solved:
            if entry[2] == 'right':
                score += int(entry[0])
            else:
                score += 20
    
    print(len(solved), score)        

if __name__ == "__main__":
    main()

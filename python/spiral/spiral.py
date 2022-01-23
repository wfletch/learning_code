# GIven A = 4
import sys
#4 4 4 4 4 4 4
#4 3 3 3 3 3 4
#4 3 2 2 2 3 4
#4 3 2 1 2 3 4
#4 3 2 2 2 3 4
#4 3 3 3 3 3 4
#4 4 4 4 4 4 4

#3 3 3 3 3
#3 2 2 2 3 
#3 2 1 2 3 
#3 2 2 2 3
#3 3 3 3 3

A = 19
cur_val = 0
max_depth = 0 
mid_value = 0
double_mem = [[] for i in range(0,A,1)]
for i in range(0, A,1):
    max_depth = i
    cur_val = A
    mem = []
    for k in range(0, A, 1):
        if k == A-1:
            mid_value = str(cur_val)
        else:
            # print(cur_val, end=" ")
            mem.append(str(cur_val))
        if cur_val != A - max_depth:
           cur_val-=1
    for entry in mem:
        double_mem[i].append(entry)
    double_mem[i].append(mid_value)
    mem.reverse()
    for entry in mem:
        double_mem[i].append(entry)
final_mem = []
for entry in double_mem:
    final_mem.append(" ".join(entry))

double_mem = double_mem[0:-1]

double_mem.reverse()
for entry in double_mem:
    final_mem.append(" ".join(entry))

for entry in final_mem:
    print(entry)



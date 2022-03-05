import sys
import threading


def ackerman(m,n):
    # Base Case
    if  m ==  0:
        return n+1
    elif n == 0:
        return ackerman(m-1, 1)
    else:
        return ackerman(m-1, ackerman(m,n-1))


if __name__ == "__main__":
    threading.stack_size(67108864)
    sys.setrecursionlimit(2 ** 20)
    thread = threading.Thread(target=ackerman(4,1))
    thread.start()
    #print(ackerman(1,1))
    #print(ackerman(2,1))
    #print(ackerman(3,1))
    #print(ackerman(4,1))
    #print(ackerman(1,2))
    #print(ackerman(2,2))
    #print(ackerman(3,2))
 #   print(ackerman(4,2))


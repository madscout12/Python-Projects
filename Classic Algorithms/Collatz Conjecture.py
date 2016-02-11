import sys

def collatz(N):
    if(N < 1):
        print "Enter a positive integer"
        return

    num_steps = 0
    print "You entered:" + str(N) + "\n"
    while(N > 1):
        if((N-1)/2 == N/2):
            N = 3*N + 1
        else:
            N = N/2
        num_steps += 1
        print ".." + str(N)

    print "\nIt took " + str(num_steps) + " steps to get to one."
    return


if __name__ == "__main__":
    try:
        collatz(int(sys.argv[1]))
    except IndexError:
        print "Enter a command line argument."

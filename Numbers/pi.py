import sys, math

def pi_N(N):
    i = 1
    pi = 0.0
    try:
        while(i < N):
            curr_sum = (1.0/(math.pow(16,i))*((4.0/(8*i+1))-(2.0/(8*i+4))-(1.0/(8*i+5))-(1.0/(8*i+6))))
            pi += 16 * curr_sum
            print pi
            i += 1
    except TypeError:
        print "Please enter an integer as an argument!"
        return

if __name__ == "__main__":
    try:
        pi_N(sys.argv[1])

    except IndexError:
        print "Please enter an integer as an argument."

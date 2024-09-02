def karatsuba(x, y):
    """
    Implementation of Karatsuba's algorithm for integer multiplication
    """
    
    if x < 10 & y < 10:
        return x * y
    
    ## step 1
    n_x = len(str(x))
    n_y = len(str(y))

    x = str(x)
    y = str(y)

    ac = int(x[0:n_x//2]) *  int(y[0:n_y//2])
    bd = int(x[n_x//2:len(x)]) * int(y[n_y//2:len(y)])
    s3 = (int(x[0:n_x//2]) + int(x[n_x//2:len(x)])) * (int(y[0:n_y//2]) + int(y[n_y//2:len(y)]))
    s4 = s3 - s2 - ac
    s5 = (s1 * 10**n_x) + s2 + (s4 * 10**(n_x//2))

    return(s5)

def main():
    print(karatsuba(563534, 142367))

if __name__ == '__main__':
    main()
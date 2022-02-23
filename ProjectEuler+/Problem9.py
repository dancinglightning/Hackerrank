#!/bin/python3

import sys

def pythagoreanTriplets(limits) :
    c, m = 0, 2
    x = -1
 
    while c < limits :
         
        for n in range(1, m) :
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n
 
            if c >= limits :
                break
                
            if a + b + c == limits:
                x = max(a*b*c, x)
            
        m = m + 1

    return x

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(pythagoreanTriplets(n))

    
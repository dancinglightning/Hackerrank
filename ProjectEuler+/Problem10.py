#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    l = [x for x in range(n+1)]
    z = int(n**0.5)
    for i in range(2, z+1):
        if l[i]!=0:
            for j in range(i, (n//i) + 1):
                l[i*j] = 0
                
    print(sum(l)-1)
            

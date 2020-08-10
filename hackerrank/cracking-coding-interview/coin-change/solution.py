#!/bin/python

import sys

def make_change(coins, n, m, s, sub):
    count = 0    
    for i in range(s, m):
        c = coins[i]
        if c == n:
            count += 1            
            break
        elif c > n:
            break        
        if sub[n-c][i] != -1:
            count += sub[n-c][i]
        else:
            count += make_change(coins, n-c, m, i, sub)            
    sub[n][s] = count
    return count
        
# n,m = raw_input().strip().split(' ')
# n,m = [int(n),int(m)]
# coins = map(int,raw_input().strip().split(' '))
# coins.sort()
# sub = [[-1 for _ in range(0,m)] for _ in xrange(0,n+1)]
# print make_change(coins, n, m, 0, sub)
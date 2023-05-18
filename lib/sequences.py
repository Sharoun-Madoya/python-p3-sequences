#!/usr/bin/env python3

def print_fibonacci(length):
    series = []
    u = 0
    v = 1
    while len(series) < length:
        series.append(u)
        u, v = v, u+v
    print(series)
    


#!/usr/bin/env python3
# File: lib/sequences.py

def print_fibonacci(length):
    if length == 0:
        print("[]")
        return
    elif length == 1:
        print("[0]")
        return
    
    fib = [0, 1]
    
    for i in range(2, length):
        fib.append(fib[-1] + fib[-2])
    
    print(fib)

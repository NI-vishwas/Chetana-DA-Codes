#!/usr/bin/env python3
# Author: Vishwas Singh
# Email: vishwasks.reach@gmail.com
# Script to using time module as a decorator

import time


def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args,**kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"function '{func.__name__}' executed in {execution_time:.6f} seconds")
        return result
    return wrapper

@timer_decorator
def loop_printer():
    print("waiting started")
    for i in range(1000):
        print(i)

    print(f"Waiting done....")


if __name__ == '__main__':
    loop_printer()

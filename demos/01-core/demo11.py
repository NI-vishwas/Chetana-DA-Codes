#!/usr/bin/env python3
#
# Author: Vishwas Singh
# Email: vishwasks.reach@gmail.com
# Script to take n numbers from the user until -999 is entered and
# print the sum, average, min & max
#


# Take the numbers from the user
# Calculate sum, average, min & max
def calculate(num_lst):
    total = sum(num_lst)
    average = total / len(num_lst)
    min_val = min(num_lst)
    max_val = max(num_lst)

    return total, average, min_val, max_val

def main():
    num_lst = []
    # Since we do not know how many numbers are there
    while True:
        num = int(input("Enter a number: "))
        if num == -999:
            break
        else:
            num_lst.append(num)

    total, avg, min_val, max_val = calculate(num_lst)
    print(f"For the list of numbers {num_lst}")
    print(f"Sum is {total}")
    print(f"Average Value is {avg:.2f}")
    print(f"Maximum Value in the list is: {max_val}")
    print(f"Minimum value in the list is: {min_val}")


if __name__ == '__main__':
    main()

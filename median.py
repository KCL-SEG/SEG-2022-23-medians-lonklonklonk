"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""
while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        numbers.sort()
        if(len(numbers) % 2 == 0):
            index = int(len(numbers)/2)
            median = (numbers[index-1]+numbers[index])/2.0
            print(median)
        else:
            print(numbers[int(len(numbers)/2)])
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break



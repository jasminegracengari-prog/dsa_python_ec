import random

def sort(values):
    num_of_elements = len(values)
    for current_index in range(1, num_of_elements):
        print("Outer loop")
        current_value = values[current_index]
        while values[current_index - 1] > current_value and current_index > 0:
            temp = values[current_index - 1]
            values[current_index - 1] = values[current_index]
            values[current_index] = temp

            print(f"Values {values}")

            current_index = current_index - 1
    return values

def getValues():
    unsortedvalues = random.sample(range(10, 50), 5)
    unsortedvalues = [8,7,6,5, 4, 3, 2, 1]
    print(f" {unsortedvalues}")
    result = sort(unsortedvalues)
    print(f" {result}")

getValues()
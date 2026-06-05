import random

def sort(values):
    num_of_elements = len(values)
    for outer_loop in range(num_of_elements):
        print("Outer loop")
        for index in range(num_of_elements - 1 - outer_loop):
            print(f"Values {values}")
            if values[index] > values[index + 1]: # if true
                # values[index], values[index + 1] = values[index + 1], values[index]
                temp = values[index]
                values[index] = values[index + 1]
                values[index + 1] = temp

    return values

def getValues():
    unsortedvalues = random.sample(range(10, 50), 5)
    # unsortedvalues = [5, 4, 3, 2, 1]
    print(f" {unsortedvalues}")
    result = sort(unsortedvalues)
    print(f" {result}")

getValues()
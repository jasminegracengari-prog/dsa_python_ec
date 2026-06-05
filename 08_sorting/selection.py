import random

def sort(values):
    num_of_elements = len(values)
    for outer_loop in range(num_of_elements):
        minimum_index = outer_loop
        for inner_loop in range(outer_loop + 1, num_of_elements):
            if values[inner_loop] < values[minimum_index]:
                minimum_index = inner_loop
                print(f"Current min {values[minimum_index]}")

        temp = values[outer_loop]
        values[outer_loop] = values[minimum_index]
        values[minimum_index] = temp
        print(f"swap {values} ")

def getValues():
    unsortedvalues = random.sample(range(10, 50), 5)
    unsortedvalues = [8,7,6,5, 4, 3, 2, 1]
    print(f" {unsortedvalues}")
    result = sort(unsortedvalues)
    print(f" {result}")

getValues()
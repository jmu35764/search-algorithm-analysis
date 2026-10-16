from algorithms import (iterative_binary_search, recursive_binary_search, sequential_search)


def main():
    #*****************************************************************
    #******Look in Tests folder for more tests regarding Phase 1******
    #*****************************************************************

    print("Code is running...")
    #Create the list for the tests
    values = [3, 5, 8, 12, 14, 18, 21]

    #Sort the values before running the algorithms
    values.sort()
    present_target = 12
    absent_target = 9

    index = recursive_binary_search(values, present_target, 0, len(values) - 1)
    
    print(f"{index}")
    print(f"Recursive Binary Search: Target {present_target} found at index {index}")

if __name__ == "__main__":
    main()


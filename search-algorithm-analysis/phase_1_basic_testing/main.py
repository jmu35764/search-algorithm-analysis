from algorithms import (iterative_binary_search, recursive_binary_search, sequential_search)

print("Test")

def main():

    print("Code is running...")
    values = [3, 5, 8, 12, 14, 18, 21]
    values.sort()
    present_target = 12
    absent_target = 9

    index = recursive_binary_search(values, present_target, 0, len(values) - 1)
    
    print(f"{index}")

if __name__ == "__main__":
    main()


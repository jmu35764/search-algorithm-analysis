import unittest
import random
import time
import statistics
from algorithms import (iterative_binary_search, recursive_binary_search, sequential_search)

def main():

    data_sizes = [5_000, 50_000, 100_000, 150_000, 1_000_000]
    number_of_trials = 10

    # Create lists to store the elapsed times for each search algorithm
    ibs_times = []
    rbs_times = []
    ss_times = []

    # First loop for each data size, second loop for the number of trials
    for size in data_sizes:
        for _ in range(number_of_trials):  
            values = sorted(random.randint(1, 1_000_000) for _ in range(size))
            if random.random() < 0.5:
                target = random.choice(values)
            else:
                target = 1_000_001  # Ensure the target is not present in the list
          
            start = 0
            start = time.perf_counter()
            index = recursive_binary_search(values, target, 0, len(values) - 1)
            elapsed_microseconds = (time.perf_counter() - start) * 1_000_000 # Set elapsed time in microseconds
            rbs_times.append(elapsed_microseconds) # Add the elapsed time to the list of times for recursive binary search
                
                
                          
                
            start = 0
            start = time.perf_counter()
            index = iterative_binary_search(values, target)
            elapsed_microseconds = (time.perf_counter() - start) * 1_000_000
            ibs_times.append(elapsed_microseconds) # Add the elapsed time to the list of times for iterative binary search   
                 

            start = 0
            start = time.perf_counter()
            index = sequential_search(values, target)
            elapsed_microseconds = (time.perf_counter() - start) * 1_000_000 
            ss_times.append(elapsed_microseconds) # Add the elapsed time to the list of times for sequential search

        print(f"Data Size: {size}")
        #Retrieve the median of the elapsed times for each search algorithm and print them
        print(f"Recursive Binary Search Median (microseconds): {statistics.median(rbs_times):.2f} \n")
        print(f"Iterative Binary Search Median (microseconds): {statistics.median(ibs_times):.2f} \n")
        print(f"Sequential Search Median (microseconds): {statistics.median(ss_times):.2f} \n")

        # Clear the lists of elapsed times for the next data size
        ibs_times.clear()
        rbs_times.clear()
        ss_times.clear()

if __name__ == "__main__":
    main()

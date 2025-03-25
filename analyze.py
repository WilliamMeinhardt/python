
import time
import os

def read_numbers_from_file(file_path):
    with open(file_path, 'r') as file:
        return [int(line.strip()) for line in file if line.strip().isdigit()]

def analyze_numbers(numbers):
    total = sum(numbers)
    avg = total / len(numbers)
    max_num = max(numbers)
    min_num = min(numbers)
    return {"sum": total, "avg": avg, "max": max_num, "min": min_num}

def measure_performance(file_path):
    start_time = time.time()
    numbers = read_numbers_from_file(file_path)
    results = analyze_numbers(numbers)
    end_time = time.time()
    
    print(f"Results for {os.path.basename(file_path)}")
    print(results)
    print(f"Execution time: {end_time - start_time:.6f} seconds")


file_path = 'LargeTestList.txt'
measure_performance(file_path)
import csv
from requirement_guard import compare_string
count = 0
total = 0

def count_correct_elements(file_path):
    global count
    global total
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            element = row[0] 
            total = total + 1
            if compare_string(element) is None:
                count = count + 1    
                print(element)
    return (total - count) / total

file_path = 'resources/historical_typosquatting.csv'

if __name__ == "__main__":
    print(count_correct_elements(file_path))


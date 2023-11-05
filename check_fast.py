import csv
from fast_typoguard import check_typo 
from fast_typoguard import check_substring
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
            if check_typo(element)[0] is None:
                count = count + 1    
                print(element)
    return( str(((total - count) / total )* 100) + "%")

file_path = 'resources/historical_typosquatting.csv'

if __name__ == "__main__":
    print(count_correct_elements(file_path))


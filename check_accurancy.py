# check every row of the origional depenency name and wether they are reguarded as typo or not
import csv
from requirement_guard import compareString

#define test data
file_path = "resources/data_test.csv"
test_data = []
with open(file_path, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        test_data.append(tuple(row))

print(test_data)

# Calculate accuracy
num_correct = 0
for correct, misspelled in test_data:
    print(misspelled)
    print(correct)
    corrected = compareString(misspelled)
    print(corrected)
    if correct in corrected:
        num_correct += 1

accuracy = num_correct / len(test_data)

print(f"Accuracy: {accuracy}")

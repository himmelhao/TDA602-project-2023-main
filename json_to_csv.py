import json
import csv

# json file
json_file = open('resources/top-pypi-packages-30-days.min.json')
# load json data
data = json.load(json_file)
# Extract rows from JSON
rows = data["rows"]
# Define CSV file path
csv_file_path = 'resources/data.csv'
# Write data to CSV file
with open(csv_file_path, "w", newline="") as csvfile:
    # Create CSV writer
    writer = csv.writer(csvfile)
    # Write rows
    for i, row in enumerate(rows):
        writer.writerow([row["project"]])

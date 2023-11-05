import csv


def add_to_whitelist(package_name):
    with open('resources/data.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([package_name])

def main():
    package_name = input("Enter the package name to add to the whitelist: ")
    add_to_whitelist(package_name)
    print("Package name added to the whitelist.")


if __name__ == '__main__':
    main()

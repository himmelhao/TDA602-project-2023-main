import csv
import sys
from pkg_resources import Requirement
from termcolor import colored
from typos import typos
from scan_folder import find_requirements_txt

false_list = []


def scan_files(file_path):
    with open(file_path, 'r') as file:
        packages = [Requirement(
            line.strip()).name for line in file.readlines()]
    # start_time = time.time()
    # print(packages)
    # print(f"Time used parsing: {time.time() - start_time} seconds")
    total_typo_list = []
    for word in packages:
        typo_list = compare_string(word)
        total_typo_list.append(typo_list)
    # endtime = time.time()
    # print(f"Time used: {endtime - start_time} seconds")
    return total_typo_list


def get_list():
    lines = []
    with open('resources/data.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            lines.append(row[0])
    return lines


def same_import(string, words):
    return string in words


def generate_typos(word):
    length = len(word)
    # swapping letters
    for i in range(length - 1):
        typo = list(word)
        typo[i], typo[i + 1] = typo[i + 1], typo[i]
        yield ''.join(typo), 'Swapped letters'

    # an repeated letter
    for i in range(length):
        for char in word:
            typo = word[:i] + char + word[i]
            yield typo, 'Repeated letter'

    # delete a letter
    for i in range(length):
        typo = word[:i] + word[i + 1:]
        yield typo, 'Deleted letter'

    # common typos
    for i in range(length):
        if word[i] in typos:
            for char in typos[word[i]]:
                typo = word[:i] + char + word[i+1:]
                yield typo, 'Common typos'

    # swapping words
    a = word.split('-')
    for i in range(len(a) - 1):
        a[i], a[i + 1] = a[i + 1], a[i]
        typo = '-'.join(a)
        yield typo, 'Swapped words'

    typo = '-'.join(a)


def generate_typos_combinations(word):
    typos = generate_typos(word)
    for typo, error in typos:
        yield typo, error
        for typo2, error2 in generate_typos(typo):
            combined_error = error + ' + ' + error2
            yield typo2, combined_error


def compare_string(string):
    suitable_matches = []
    lines = get_list()

    for word in lines:
        if abs(len(word) - len(string)) < 3:
            suitable_matches.append(word)

    match_list = []
    for word in suitable_matches:
        match_found = False
        if same_import(string, suitable_matches):
            continue
        else:
            for typo, desc in generate_typos_combinations(word):
                if string == typo:
                    match_found = True
                    break
            if match_found:
                match_list.append((word, desc))

    if match_list:
        output = f" Input {string} may have a type error:\n"
        for typo, desc in match_list:
            output += f"{desc}, it might should be {typo}\n"
        print(output)
        false_list.append(string)
        return None
    else:
        return string


def print_results():
    if false_list:
        print(' Please check the spelling of these packages')
        for item in false_list:
            print(colored(item, 'red'))
    else:
        print(colored('All packages are correct', 'green'))


def main():
    if len(sys.argv) < 2:
        print("Please provide the file or directory path as a command-line argument.")
        sys.exit(1)

    path = sys.argv[1]
    file_path = find_requirements_txt(path)
    scan_files(file_path)
    print_results()


if __name__ == "__main__":
    main()

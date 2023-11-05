import csv
from hypothesis import given, settings, strategies as st
from requirement_guard import compareString
from genarate_typo import generate_typo


@settings(deadline=5000)
@given(st.just("resources/test.csv"))
def test_typo_checker(csv_file):
    with open(csv_file, 'r', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)
    for row in rows:
        word = row[0]
        typo_list = compareString(generate_typo(word))
        assert word in typo_list


if __name__ == '__main__':
    test_typo_checker()

import os


def find_requirements_txt(folder):
    for root, dirs, files in os.walk(folder):
        if "requirements.txt" in files:
            return os.path.join(root, "requirements.txt")
    return None

# download the package and check dependency before that
from package_checker import get_dependencies
import subprocess
from fast_typoguard import check_typo
import sys


def run_installation(package):
    # Run the installation command
    command = ['pip', 'install', package]
    subprocess.run(command)


def check_continue_installation(package):
    # Check if the user wants to continue with the installation
    continue_install = input(
        "Do you want to continue with the installation? (y/n): ")
    if continue_install.lower() == 'y':
        run_installation(package)
    else:
        print("Installation cancelle d.")


def install_check(package):
    dependencies = get_dependencies(package)
    typos = check_typo(package)
    if typos[0] is None:
        for dependency in dependencies:
            if check_typo(dependency)[0] is not None:
                check_continue_installation(dependency)
            else:
                run_installation(dependency)
    else:
        print(f"The package '{package}' might have a typo.")
        check_continue_installation


def main():
    if len(sys.argv) >= 2:
        command = sys.argv[1] + " " + sys.argv[2]
        if command == "pip install":
            package_name = sys.argv[3:]
            result = ' '.join(package_name)
            install_check(result)
        else:
            print("Please enter a valid command.")
    else:
        print("Please enter a package name.")


if __name__ == '__main__':
    main()

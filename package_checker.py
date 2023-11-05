# Gets all transitive dependencies of a single given package
# code from papaer "Defending against package typosquatting"

import requests
import re

extra_re = re.compile('^.*;.*extra\s*==.*$')

allowed_chars = set(
    'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')


def get_dependencies(package):
    dependencies = set()
    todo = [package]

    while len(todo) != 0:
        package_name = todo.pop(0)

        r = requests.get('https://pypi.org/pypi/{}/json'.format(package_name))

        if r.status_code != 200:
            print('Metadata request for {} returned status code {}'.format(
                package_name, r.status_code))
        else:
            try:
                metadata = r.json()
                deps = metadata['info']['requires_dist']
                dependencies.add(package_name)
                if deps is None:
                    continue

                for d_name in deps:
                    if extra_re.match(d_name) is not None:
                        continue

                    for i, char in enumerate(d_name):
                        if char not in allowed_chars:
                            d_name = d_name[:i]
                            break

                    if d_name not in dependencies and d_name not in todo:
                        todo.append(d_name)

            except:
                print('Unhandled exception when processing {}'.format(package_name))

    return list(dependencies)

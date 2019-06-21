"""
This module is a launcher of our fuzzer
To run fuzzer, use 'python3 run.py' command
"""

from modules.py_parser import fetch_parsed_data
from modules.fuzzer import fuzz
import urllib3
import sys
import time


def main():
    """
    Make console input/output, open/make file log.txt, specify fuzzer for user, call fetch_parsed_data() to fetch parsed
    data and fuzz() to fuzz
    :return: none
    """
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    start_time = time.time()

    file = open('log.txt', 'w')
    console_stdout = sys.stdout

    print('Starting...')
    data = {}
    while True:
        path = input('Full path to main RAML doc\n')
        try:
            print('Parsing RAML...')
            data, sensor = fetch_parsed_data(path)
            out = sensor.stdout.read(1)
            if int(out):
                pass
            else:
                print('Wrong path!')
                raise ValueError
        except ValueError:
            pass
        else:
            print('Finished')
            break
    domain = input('Full domain name with protocol\n')
    specification = ''
    specification_codes = []
    ans = input('Want to specify errors? (y/n)\n')
    if ans in ['y', 'Y']:
        while True:
            ans = input('Want to show some errors or not to show? (s/ns)\n')
            if ans in ['s', 'S']:
                specification = 'sc'
                break
            elif ans in ['ns', 'NS', 'nS', 'Ns']:
                specification = 'hc'
                break
            else:
                pass
        while True:
            ans = input('Want to enter your own list or use described in RAML? (l/d)\n')
            if ans in ['l', 'L']:
                try:
                    specification_codes = list(map(int, input('Specify codes, splitting with spaces\n').split()))
                except ValueError:
                    print('Wrong format')
                else:
                    break
            elif ans in ['d', 'D']:
                break
    elif ans in ['n', 'N']:
        pass
    else:
        pass

    print('Fuzzing...')
    sys.stdout = file
    fuzz(data, specification, specification_codes, domain)
    sys.stdout = console_stdout
    print('Done! Check out log.txt file')
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    main()

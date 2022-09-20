import sys
from jobs.import_files import run


def main():
    if len(sys.argv[1]) < 2:
        print('Invalid args numbers')
    elif sys.argv[1] == 'import_files':
        run()


if __name__ == '__main__':
    main()

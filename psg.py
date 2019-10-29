try:
    from .passwordgeneratorclass import PasswordGenerator
except:
    from passwordgeneratorclass import PasswordGenerator
import argparse


def main():
    parser = argparse.ArgumentParser(description='Password Generator')
    parser.add_argument('--max', type=int,
                        help='Max length of password (default={})'.format(PasswordGenerator.MAX_LENGTH), default=-1)
    parser.add_argument('--min', type=int,
                        help='Min length of password (default={})'.format(PasswordGenerator.MIN_LENGTH), default=-1)
    parser.add_argument('--len', type=int, help='Fix length of password (default=random between [min, max])',
                        default=-1)

    args = parser.parse_args()

    minl = PasswordGenerator.MIN_LENGTH if args.min == -1 else args.min
    maxl = PasswordGenerator.MAX_LENGTH if args.max == -1 else args.max

    if args.len != -1:
        minl, maxl = args.len, args.len
    password = PasswordGenerator(min_length=minl, max_length=maxl).generate()
    print(password)


if __name__ == '__main__':
    main()

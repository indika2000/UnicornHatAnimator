__author__ = 'Indy'

import json


def main():

    with open('server.json') as jj:
        print(jj)
        print(type(jj))

        s = json.load(jj)
        print(s)
        print(type(s))

        d = json.dumps(s)
        print(d)
        print(type(d))

if __name__ == '__main__':
    main()
#!/usr/bin/python3

import argparse

"""
Application Name
by Olof Sjödin <me@olofsjodin.se>

GPL v3
"""

def main():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("--example", dest="example", action="store_true")

    args = parser.parse_args()

    args.example

if __name__ == "__main__":
    main()

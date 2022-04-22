#!/usr/bin/env python

import argparse
import csv
from clearOutDir import clearOutDir
from writeToSankey import writeToSankey

parser = argparse.ArgumentParser()

parser.add_argument("-f", "--file", dest="file", help="CSV file")
args = parser.parse_args()

def main():
    if args.file:
        file_name = args.file        
        clearOutDir()

        with open(file_name, mode="r") as file:
            csv_file = csv.DictReader(file)

            for row in csv_file:
                writeToSankey(row)
    return

if __name__ == "__main__":
    main()
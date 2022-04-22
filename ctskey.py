#!/usr/bin/env python

import argparse
import csv
from clearOutDir import clearOutDir
from writeToSankey import writeToSankey

ylw_underline = "\033[4;33m"
ylw = "\033[0;33m"
w = "\033[0;37m"

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

        
        print(f"💎 {ylw}ctskey owes credit to the makers of SankeyMATIC. Consider donating to them!")
        print("\t🔗 https://sankeymatic.com/about")
        print(f"{w}Created sankey.skmt in the out directory. ")
    return

if __name__ == "__main__":
    main()
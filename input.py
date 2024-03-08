import sys
import os
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input_file", help="input file name")
args = parser.parse_args()
input_file = args.input_file
if not os.path.isfile(input_file):
    print(f"File path {input_file} does not exist. Exiting...")
    sys.exit()
with open(input_file, "r") as f:
    lines = f.readlines()
lines = [line.strip() for line in lines if line.strip()]
print(lines)
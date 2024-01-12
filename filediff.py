#!/usr/bin/python3
import argparse

# set up arguments
parser = argparse.ArgumentParser(description='Compare lines of new-file to old-file and ouput new lines (non-duplicates) of new-file.')
parser.add_argument('f_new', metavar='new-file', help='new file to compare')
parser.add_argument('f_old', metavar='old-file', help='old file to compare')
args = parser.parse_args()

def added_lines():
    with open(args.f_new, 'r') as file_new:
        with open(args.f_old, 'r') as file_old:
            different = set(file_new).difference(file_old)
    different.discard('\n')
    return different

def removed_lines():
    with open(args.f_new, 'r') as file_new:
        with open(args.f_old, 'r') as file_old:
            different = set(file_old).difference(file_new)
    different.discard('\n')
    return different

#print added lines
added_entries = added_lines()
removed_entries = removed_lines()
for line in added_entries:
    print("[+] " + line.strip())
for line in removed_entries:
    print("[-] " + line.strip())

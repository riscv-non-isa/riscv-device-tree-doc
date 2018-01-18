#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-2.0+
# Copyright (C) 2017-2018 Jonathan Neuschäfer

import sys, os, subprocess

# Scan statistics
class Stats:
    def __init__(self, our_dir, linux_dir, ignorelist=[]):
        self.our_dir = our_dir
        self.linux_dir = linux_dir
        self.ignorelist = ignorelist
        self.files_match = []
        self.files_mismatch = []
        self.files_missing_in_linux = []
        self.files_ignored = []
        self.files_ignored_but_present = []

    def good(self):
        return len(self.files_missing_in_linux) == 0 and \
                len(self.files_mismatch) == 0

    def print_summary(self):
        print("\nStatistics:")
        if len(self.files_match) > 0:
            print("  Matching               : %d" % len(self.files_match))
        if len(self.files_missing_in_linux) > 0:
            print("  Missing in Linux       : %d" % len(self.files_missing_in_linux))
        if len(self.files_ignored) > 0:
            print("  Ignored                : %d" % len(self.files_ignored))
        if len(self.files_ignored_but_present) > 0:
            print("  Ignored but present    : %d" % len(self.files_ignored_but_present))
        if len(self.files_mismatch) > 0:
            print("  Content mismatch       : %d" % len(self.files_mismatch))

    def match(self, filename):
        self.files_match.append(filename)

    def missing_in_linux(self, filename):
        if filename in self.ignorelist:
            self.files_ignored.append(filename)
        else:
            print("%s: File exists here but not in Linux" % filename)
            self.files_missing_in_linux.append(filename)

    def ignored_but_present(self, filename):
        print(("%s: Ignored but present in Linux. " +
               "Consider removing it from not-in-linux.txt") % filename)

    def mismatch(self, filename):
        print("%s: Content mismatch" % filename)
        self.files_mismatch.append(filename)

        subprocess.run(["diff", "-u",
            self.our_dir + filename, self.linux_dir + filename])


# Generate all file names under the given path, recursively
def file_tree_walk(path):
    skip = len(path)
    for root, dirs, filelist in os.walk(path):
        for f in filelist:
            # Ignore editor temp files, etc.
            if f[0] == '.':
                continue

            yield os.path.normpath(root + '/' + f)[skip:]

# Ensure that there is exactly one slash at the end of a path
def add_slash(path):
    return os.path.normpath(path) + '/'

# Load the not-in-linux.txt ignore list file.
#   path: The path of that file
def load_ignorelist(path):
    try:
        f = open(path)
        text = f.read()
    except FileNotFoundError:
        return []

    # Empty lines and lines starting with a '#' comment character are ignored
    return [ line for line in text.splitlines() if
            line != '' and line[0] != '#' ]

def main():
    if len(sys.argv) != 3:
        print(repr(sys.argv))
        usage(sys.argv[0])
        sys.exit(1)

    our_dir = add_slash(sys.argv[1])
    linux_dir = add_slash(sys.argv[2])

    ignorelist = load_ignorelist(our_dir + "/not-in-linux.txt")

    stats = Stats(our_dir, linux_dir, ignorelist)

    for filename in file_tree_walk(our_dir):
        our_f = open(our_dir + filename)

        try:
            linux_f = open(linux_dir + filename)
        except FileNotFoundError:
            stats.missing_in_linux(filename)
            continue

        if filename in ignorelist:
            stats.ignored_but_present(filename)

        our_data = our_f.read()
        linux_data = linux_f.read()

        if our_data != linux_data:
            stats.mismatch(filename)
        else:
            stats.match(filename)

    stats.print_summary()

    if not stats.good():
        sys.exit(1)


def usage(program):
    print("This program checks the RISC-V device tree bindings repository")
    print("against the device tree bindings in the Linux source tree.")
    print("")
    print("Usage: %s OUR-BINDINGS LINUX-BINDINGS" % sys.argv[0])
    print("")
    print("   OUR-BINDINGS: \"Our\" bindings directory")
    print(" LINUX-BINDINGS: Linux's bindings directory (Documentation/devicetree/bindings)")

if __name__ == "__main__":
    main()

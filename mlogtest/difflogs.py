#!/usr/bin/env python
"""Diff MongoDB log files."""

import argparse
import logging
import os
from glob import glob

# from mtools.util.logevent import LogEvent

# difflogs version
VERSION = "0.1.0"


def compare_logs(loga, logb, output):
    """Compare two log files."""
    logging.debug("Comparing: " + loga + " and " + logb)
    try:
        with open(logb, 'r') as file1:
            with open(loga, 'r') as file2:
                same = set(file1).difference(file2)
    except Exception as e:
        logging.error(e)
        exit()
    header = """\n================================\n%s
================================\n""" % os.path.basename(logb)
    if output == "stdout":
        print(header)
        if len(same) == 0:
            print("No difference.")
        else:
            for line in same:
                print(line)
    else:
        try:
            with open(os.path.abspath(output), 'a') as f:
                f.write(header)
                if len(same) == 0:
                    f.write("\nNo difference.\n")
                else:
                    for line in same:
                        f.write(line)
        except Exception as e:
            logging.error(e)
    return


def process_files(base, new, output):
    """Process log files."""
    vera = os.path.abspath(base)
    base = os.path.basename(vera)
    verb = os.path.abspath(new)
    new = os.path.basename(verb)
    versions = "Base version: %s\nNew version: %s" % (base, new)
    print(versions)
    if output == "stdout":
        pass
    else:
        output = os.path.abspath(output)
        try:
            with open(output, 'w') as f:
                f.write(versions)
        except OSError:
            pass

    logs = glob(os.path.join(vera + "/MTEST-*"))
    logging.debug('logs: ' + str(logs))
    for log in logs:
        filename = os.path.basename(log)
        loga = os.path.join(vera, filename)
        logb = os.path.join(verb, filename)
        compare_logs(loga, logb, output)
    return


def enable_logging(debug):
    """Log levels: DEBUG, INFO, WARNING, ERROR."""
    if debug is True:
        logging.basicConfig(level=logging.DEBUG,
                            format='%(levelname)s %(message)s')
    else:
        logging.basicConfig(level=logging.INFO,
                            format='%(message)s')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Diff MongoDB log versions.")
    parser.add_argument("base", help="""source directory containing base log
                        files to diff against""")
    parser.add_argument("new", help="""source directory containing new log
                        files to diff""")
    parser.add_argument("-o", "--output", default="stdout",
                        help="""output file for diff report (Default:
                        stdout)""")
    parser.add_argument("-d", "--debug", action="store_true",
                        help="enable debug output")
    parser.add_argument("-v", "--version", action="version", version=VERSION)
    args = parser.parse_args()
    enable_logging(args.debug)
    process_files(args.base, args.new, args.output)

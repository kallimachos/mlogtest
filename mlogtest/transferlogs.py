#!/usr/bin/env python
"""Copy full log, conf file, and log snippets for each MongoDB version."""

import argparse
import logging
import os
import re
from glob import glob
from shutil import copy

# transferlogs version
VERSION = "0.1.0"


def grep(filename, pattern):
    """Search a file for a pattern. Return an array of matching lines."""
    result = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                if re.search(pattern, line):
                    result.append(line)
            return result
    except Exception as e:
        print(e)
        exit()


def process_version(filename, outdir):
    """Process log   for MongoDB version and add files to output directory."""
    commands = ["MTEST-insert", "MTEST-bulkinsert", "MTEST-query",
                "MTEST-update", "MTEST-delete"]
    logging.debug("Commands: " + str(commands))
    noext = os.path.splitext(filename)[0]
    logging.debug("noext: " + noext)
    conf = noext + ".conf"
    logging.debug("conf: " + conf)
    version = os.path.basename(noext)[7:]
    logging.debug("version: " + version)
    base = "v" + os.path.splitext(version)[0]
    logging.debug("base: " + base)
    dest = os.path.join(outdir, base, version)
    logging.debug("dest: " + dest)

    # Create destination directory and copy full log and conf files there
    try:
        if not os.path.isdir(dest):
            os.makedirs(dest)
        copy(filename, dest)
        copy(conf, dest)
    except Exception as e:
        logging.error(e)
        exit()

    # Split log into separate files according to commands.
    try:
        for command in commands:
            snippet = grep(filename, command)
            logging.debug("snippet: " + str(snippet))
            snippetpath = os.path.join(dest, command)
            logging.debug("snippetpath: " + snippetpath)
            with open(snippetpath, 'w') as f:
                for line in snippet:
                    line = re.sub(r'\s\d*ms$', '', line)[29:]
                    f.write(line)
    except Exception as e:
        logging.error(e)
    logging.info(version + " complete.")
    return


def process_files(indir, outdir):
    """Find log files, process, and write to output directory."""
    inpath = os.path.abspath(indir)
    logging.info("Source directory: " + inpath)
    outpath = os.path.abspath(outdir)
    logging.info("Output directory: " + outpath)
    logs = glob(os.path.join(inpath + "/mongod-*.log"))
    for log in logs:
        process_version(log, outpath)
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
    parser = argparse.ArgumentParser(description="""Copy full log, conf file,
                                     and log snippets for each MongoDB
                                     version""")
    parser.add_argument("-i", "--input", default=".",
                        help="""source directory containing log files (Default:
                        current directory)""")
    parser.add_argument("-o", "--output", default=".",
                        help="""output directory where translogs creates
                        version directories (Default: current directory)""")
    parser.add_argument("-d", "--debug", action="store_true",
                        help="enable debug output")
    parser.add_argument("-v", "--version", action="version", version=VERSION)
    args = parser.parse_args()
    enable_logging(args.debug)
    process_files(args.input, args.output)

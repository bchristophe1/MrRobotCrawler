#!/usr/bin/env python3
# -*-coding:Utf-8 -*

# Author: Beny - 30/07/2015
# Usage: MrRobotCrawler.py -u <http://www.test.com>
# Detail: This Script Scan and read the robots.txt File of a website

import getopt
import sys
import requests

__author__ = 'benji'
__version__ = '1.0'


def main(argv):

    # Initalize URL variable at null by default
    url = ""

    # processing args

    try:
        opts, args = getopt.getopt(argv, "hu:",["url="])
    except getopt.GetoptError:
        print("\nusage: " + sys.argv[0] + " -u http://www.site.com\n")
        sys.exit(2)
    #if there is no args
    if len(sys.argv)<2:
        print("\nusage: " + sys.argv[0] + " -u http://www.site.com\n")
    else:
        for opt, arg in opts:
            if opt == "-h":
                print("\nusage: " + sys.argv[0] + " -u http://www.site.com\n")
                sys.exit()
            elif opt in ("-u", "--url"):
                url = str(arg) + "/robots.txt"
                print(url)

if __name__ == "__main__":
    main(sys.argv[1:])

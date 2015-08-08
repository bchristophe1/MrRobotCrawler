#!/usr/bin/env python3
# -*-coding:Utf-8 -*

# Author: Beny - 30/07/2015
# Usage: MrRobotCrawler.py -u <http://www.test.com>
# Detail: This Script Scan and read the robots.txt File of a website

import getopt
import sys
import os
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

__author__ = 'benji'
__version__ = '1.0'


def main(argv):

    # Initalize URL variable at null by default
    url = ""

    # Processing Args

    try:
        opts, args = getopt.getopt(argv, "h:u:",["url="])
    except getopt.GetoptError:
        print("\nusage: " + sys.argv[0] + " -u http://www.site.com\n")
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-h":
            print("\nusage: " + sys.argv[0] + " -u http://www.site.com\n")
            sys.exit()
        elif opt in ("-u", "--url"):
            url = str(arg) + "/robots.txt"
            os.system('clear')
            print("\033[95m[+] Your url is : " + url + "\033[00m")
        else:
            print("\nusage: " + sys.argv[0] + " -u http://www.site.com\n")
            sys.exit()

    # Processing Request
    try:
        req = Request(url)
        try:
            response = urlopen(req)
        except HTTPError as e:
            print('\033[91mError code:', e.code)
            print("\033[00m")
        except URLError as e:
            print('\033[91mReason: ', e.reason)
            print("\033[00m")
        else:
            print(response)
    except ValueError as e:
        print('\033[91mError url is incorrect or malformed, please begin your url with http:// \033[00m')




if __name__ == "__main__":
    main(sys.argv[1:])

import urllib
import sys
import time
import csv
import re
import os



LOCATION_URL="http://nok.fxexchangerate.com/"


regex2="(\S*\d+\s\w+\s\=\s[^\s]*.*[NOK])<br/>"
m2 = re.compile(regex2)
foundfirst=False
foundsecond=False
fromto=["USD","GBP","EUR","SGD","JPY"]
now = time.strftime("%c")
for currency in fromto:
        response = urllib.urlopen(LOCATION_URL+ currency + ".xml")
        lines = response.readlines()
        output_string=""

        # Build the output from the web query as a string
        for line in lines:
                #print("Current line: "+line)
                mymatch2 = m2.search(line)
                if mymatch2:
                        value=mymatch2.group(1)
                        if not foundfirst:
                                foundfirst=True
                                output_string=output_string + " " + "Convert:"  + value + "\n"
                                continue
                        else:
                                foundsecond=True
                                output_string=output_string + " " + "Convert:" + value + "\n"
                                break

        sys.stdout.write(now)
        sys.stdout.write(output_string)
        time.sleep(1)

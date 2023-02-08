#!/usr/bin/python3

import re #regular expression
import subprocess

SPEED = 50

# redirecting xinput list output to xinput-out.txt file
with open('xinput-out.txt', "w") as outfile:
    result_code = subprocess.run(["xinput", "list"], stdout=outfile)

line = ""
with open('xinput-out.txt') as f:
    # search for Touchpad in every line on the xinput-out.txt file
    pattern = ' Touchpad '
    # read line until found 'Touchpad'
    line = f.readline()
    while line:
        result = re.findall(pattern, line)
        # if found, exit loop
        if result:
            break
        
        line = f.readline()

# if line != "", search for id and launch command to set speed
if (line):
    pattern = 'id=(\d+)'
    result = re.findall(pattern, line)

    # this command can vary on your touchpad type
    result_code = subprocess.run(["xinput", "--set-prop", str(result[0]), "libinput Scrolling Pixel Distance", str(SPEED)])

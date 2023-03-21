# set-touchpad-scrolling-speed
With this simple Python code I managed to set my two finger scrolling speed preference in Pop OS! every time I log into my pc.

## Requirements
You only need Python3 and xinput installed on your linux machine.
To check if these programs are installed just type `xinput --verion` and `python3 --version`.

## How to modify the two finger scrolling speed with xinput commands
If you want to try what speed works for you, simply follow this indication:
1. Type `xinput list`, look for Touchpad and save its id.
2. Type `sudo xinput list-props <your-touchpad-id>` and look for "libinput Scrolling Pixel Distance". The number to the right of it shows the scrolling speed: the higher the number, the lower the speed.
3. To change this value, type `sudo xinput --set-prop <your-touchpad-id> "libinput Scrolling Pixel Distance" <your-value>`

Unfortunately this change is not permanent, so I had fun writing this script! If you don't want to follow this tutorial you can still search the internet for another solution.

## How to run the script at startup
When you have found the value that works for you, go ahead and open the .py file to change the value of the variable SPEED. Replace the value 50 with your value.

First you need to clone this respository wherever you want, then go to the menu and look for 'Startup Application' and open it: it will open a window where you can add a startup application.
In this window, click Add, write a name, optionally a description and more importantly in the command section browse to the folder previously cloned and select the python file.
Click Save and you are done!
Now your OS will automatically run this script at the start of your pc.

## Note
There are different types of touchpads, for example Synaptic Touchpad. In this case the procedure is the same but you also have to change the xinput command in the very last line of the .py file.

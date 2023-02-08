# set-touchpad-scrolling-speed
With this simple Python code I managed to set my two finger scrolling speed preference in Pop OS! every time I log into my pc.

## Requirements
You only need Python3 and xinput installed on your linux machine.
To check if this programs are installed just type `xinput --verion` and `pythoon3 --version`.

## How to modify the two finger scrolling speed with xinput commands
If you want to try what speed works for you, simply follow this indication:
1. Type `xinput list` in your terminal, look for Touchpad and save its id.
2. Type `sudo list-props <your-touchpad-id>` and look for "libinput Scrolling Pixel Distance". The number at its right is, in simple, the scrolling speed: higher the number, slower the speed.
3. To change this value you can type `sudo xinput --set-prop <your-touchpad-id> "libinput Scrolling Pixel Distance" <your-value>`

Unfortunately this changes are not permanent, so I had fun writing this script! If you don't want to follow this tutorial you can still search on the internet for other solution.

When you have found the value that works for you, go ahead and open the .py file to change the value of the variable SPEED. Replace the value 50 with your value.

## How to run the script at startup
First you need to clone this respository wherever you want, then go to the menu and look for 'Startup Application' and open it: it will open a window where you can manage startup application.
Once you open it, click add and insert a name, a description and more importantly in the command section browse to the folder previously cloned and select the python file.
Click save and you are done!
Now your os will automatically run this script at the start of your pc.

## Note
There are different type of touchpad, for exemple Synaptic Touchpad. In this cases the procedur is the same but you also have to change the xinput command in the very last line of the .py file.
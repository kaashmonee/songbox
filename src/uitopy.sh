# this script converts a .ui file to a .py file
printf "Please enter name: "
read -r name
pyuic4 -x $name.ui -o $name.py

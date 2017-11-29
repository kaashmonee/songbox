# this script converts a .ui file to a .py file
echo "Please enter name: "
read name
pyuic4 -x $name.ui -o $name.py

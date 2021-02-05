
#!/bin/bash

# Set color
Color_Off='\033[0m'       # Text Reset
Purple='\033[0;35m'       # Purple


####################################################################
#                           INSTALL PIP                            #
####################################################################

echo "$Purple Install pip $Color_Off"

sudo apt update
sudo apt install python3-pip
pip3 --version

####################################################################
#                INSTALL PYTHON REQUIREMENTS                       #
####################################################################

echo "$Purple Install Python Requirements $Color_Off"

python3 -m pip install -r srcs/requirements.txt


####################################################################
#                         RUN PYTHON SCRIPT                        #
####################################################################

echo "$Purple Run Python Script $Color_Off"

python3 endpoint_discovery.py

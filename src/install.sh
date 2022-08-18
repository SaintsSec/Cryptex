#!/bin/bash
# installer for Cryptex
# created by : AlexKollar and Mart
# DO NOT FUCK WITH THIS SCRIPT

# color variables
# red="\e[0;91m"
# green="\e[0;92m"
# blue="\e[0;94m"
# bold="\e[1m"
# reset="\e[0m"

LOCATION = $PWD/src/main.py
python3 LOCATION
touch $HOME/.local/bin/cryptex
echo "#!/bin/bash" > $HOME/.local/bin/cryptex
echo "python3 $LOCATION" >> $HOME/.local/bin/cryptex
chmod u+x $HOME/.local/bin/cryptex
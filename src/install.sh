#!/bin/bash
# installer for Cryptex
# created by : Soulsender and C0SM0
# DO NOT FUCK WITH THIS SCRIPT

# color variables
red="\e[0;91m"
green="\e[0;92m"
blue="\e[0;94m"
bold="\e[1m"
reset="\e[0m"

function alias_workflow {
    # set up alias workflow
    echo -e "${blue}[*] Setting up alias...${reset}"

    # check if it already exists in bashrc
    if ! cat ~/.bashrc | grep "CRYPTEX_PATH" > /dev/null; then
        # Do it in one command instead of repeating yourself.
        echo "
        export CRYPTEX_PATH=\"~/.CryptexOOP\"
        alias cryptexoop=\"python3 ~/.CryptexOOP/src/main.py\"
        " >> ~/.bashrc
    fi

    #check if it already exists in zshrc
    if ! cat ~/.zshrc | grep "CRYPTEX_PATH" > /dev/null; then
        # Do it in one command instead of repeating yourself.
        echo "
        export CRYPTEX_PATH=\"~/.CryptexOOP\"
        alias cryptexoop=\"python3 ~/.CryptexOOP/src/main.py\"
        " >> ~/.zshrc
    fi

    echo -e "${green}[+] Completed${reset}"

    # clean up
    echo -e "${green}[+] Installation Successful"
    echo -e "[+] Please Restart your terminal"
    echo -e "[+] type 'cryptexoop' launch Cryptex${reset}"
    bash
}

# check if run with sudo
if [ "$EUID" -ne 0 ]; then
    continue
else
    echo -e "${red}Do not run as root. The script will prompt you for root access.${reset}"
    exit 0
fi

# arguments
while [ -n "$1" ]
do
case "$1" in
--help) 
  echo "
        SUPPORTED DISTROS:
        - Debian
            - Parrot
            - Ubuntu
            - Kali
        - Arch
        - Void
  "
  exit 0
;;

--unsupported-distro)
    # call alias workflow function
    alias_workflow
;;

esac
shift
done

# check for valid distro (Parrot, Ubuntu, Void, Debian, Arch)
distro=`sudo cat /etc/issue | awk '{print $1;}'`

# staging
# echo -e "${blue}[*] Staging process...${reset}"
# mkdir ~/.Cryptex
# cd ..
# mv Cryptex/* ~/.Cryptex
# rm -rf Cryptex
# cd ~/.Cryptex
# echo -e "${green}[+] Complete${reset}"

# staging for testing
echo -e "${blue}[*] Staging process...${reset}"
mkdir ~/.CryptexOOP
cd ..
cp CryptexOOP/* ~/.CryptexOOP -r
cd ~/.CryptexOOP
echo -e "${green}[+] Completed${reset}"

if [[ "$distro" == "Debian" ]] || [[ "$distro" == "Parrot" ]] || [[ "$distro" == "Ubuntu" ]] || [[ "$distro" == "Linux" ]] || [[ "$distro" == "Kali" ]]; then
    # installing tools for debian
    echo -e "${blue}[*] Installing tools...${reset}"
    sudo apt update
    sudo apt-get install python3
    sudo apt-get install python3-pip python-dev
    pip install qrcode
    pip install Cryptography
    pip install googletrans==3.1.0a0
    pip install colorama
    pip install pillow
    pip install numpy
    echo -e "${green}[+] Completed${reset}"

elif [[ "$distro" == "Void" ]]; then
    # installing tools for void
    echo -e "${blue}[*] Installing tools...${reset}"
    sudo xbps-install -S python3
    pip install qrcode
    pip install Cryptography
    pip install googletrans==3.1.0a0
    pip install colorama
    echo -e "${green}[+] Completed${reset}"

elif [[ "$arch" = "Arch" ]]; then
    # installing tools for arch
    echo -e "${blue}[*] Installing tools...${reset}"
    sudo pacman -Syu
    sudo pacman -S python python-pip
    python3 -m pip install qrcode
    python3 -m pip install Cryptography
    python3 -m pip install googletrans==3.1.0a0
    python3 -m pip install colorama
    echo -e "${green}[+] Completed${reset}"

else
    echo -e "${red}[!] Unknown distro, please see documentation for unknown distros.${reset}"
    exit 0
fi

# call alias workflow
alias_workflow

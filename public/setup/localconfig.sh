#!/bin/bash

# Check if script is run as root
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root"
   exit 1
fi

# Define ASCII banner
banner="
////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////
////             _____                                  ////
////            / ___/___  ______   _____  _____        ////
////            \__ \/ _ \/ ___/ | / / _ \/ ___/        ////
////           ___/ /  __/ /   | |/ /  __/ /            ////
////          /____/\___/_/_  _|___/\_/___/_____        ////
////          / ____/ __ \/ | / / ____/  _/ ____/       ////
////         / /   / / / /  |/ / /_   / // / __         //// 
////        / /___/ /_/ / /|  / __/ _/ // /_/ /         ////
////       /_____/\____/_/ |_/_/   /___/\____/          ////
////                                                    ////
////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////
"

echo "$banner"

# Detect operating system
if [ -f "/etc/redhat-release" ]; then
  # Get distribution name from /etc/redhat-release
  distro=$(cat /etc/redhat-release | awk '{print $1}')
  case $distro in
    CentOS|RHEL)
      # Link files and directories to /etc/nginx
      echo "Detected $distro, linking files and directories"
      if [ -d "/etc/nginx" ]; then
        # Ask for permission before deleting existing files and directories
        read -p "Do you want to delete existing files and directories in /etc/nginx? (y/n)" -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
          rm -rf /etc/nginx/*
        fi
      else
        # Create directory if it doesn't exist
        mkdir /etc/nginx
      fi
      ln -s $(pwd)/nginx/* /etc/nginx/
      echo "Files and directories linked to /etc/nginx"
      ;;
    *)
      echo "Unsupported distribution: $distro"
      exit 1
      ;;
  esac
elif [ -f "/etc/arch-release" ]; then
  # Link files and directories to /etc/nginx
  echo "Detected Arch Linux, linking files and directories"
  if [ -d "/etc/nginx" ]; then
    # Ask for permission before deleting existing files and directories
    read -p "Do you want to delete existing files and directories in /etc/nginx? (y/n)" -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
      rm -rf /etc/nginx/*
    fi
  else
    # Create directory if it doesn't exist
    mkdir /etc/nginx
  fi
  ln -s $(pwd)/nginx/* /etc/nginx/
  echo "Files and directories linked to /etc/nginx"
elif [ -f "/etc/lsb-release" ]; then
  # Get distribution name using lsb_release command
  distro=$(lsb_release -si)
  case $distro in
    Ubuntu)
      # Do nothing
      echo "Detected Ubuntu, no additional actions required"
      ;;
    *)
      echo "Unsupported distribution: $distro"
      exit 1
      ;;
  esac
else
  echo "Unable to determine distribution"
  exit 1
fi

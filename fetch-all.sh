#!/bin/bash
ml=$1;

# create a channel/group list for automatic fetch, named channel.txt
# only include username

for channel in $(cat channel.txt)
do

echo -e "      "
echo -e "\e[34m-----------------------\e[0m\e[36m$channel\e[0m\e[34m-----------------------\e[0m"

python3 tg-fetcher.py -c $channel -m $ml;

done

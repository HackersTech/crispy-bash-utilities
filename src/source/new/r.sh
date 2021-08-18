#!/bin/bash
if [ "$(uname -a | grep -c Android)" == 1 ]
then
bash k.sh
cd $HOME 
cd crispy-bash-utilities
cd src
cd source
cd new
bash rr.sh
else 
echo ""
bash rr.sh
fi

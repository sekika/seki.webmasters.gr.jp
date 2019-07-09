#!/bin/sh
export LANG=ja_JP.utf8
echo "passme.html\nALL\n\n" | passme html > /dev/null
cp /home/seki/etc/output/passme.html passme.html

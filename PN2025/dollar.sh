#!/usr/bin/bash

yen="$1"
dollar=$(( yen / 158 ))
echo "およそ${dollar}ドルです"

#!/bin/bash

input="/home/marcman/dev/odoo/list"

while read -r line
do
	echo "$line"
	echo "$line" | python "solution.py"
done < "$input"

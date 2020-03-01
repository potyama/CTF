#!/bin/sh
for((i=0;i<23;i++))
do
    echo "$i"
    python b64.py $i
done


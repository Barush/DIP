#!/usr/bin/env bash

insert_freq=2
from="../data/lists/all830.csv"
into="../data/lists/spz_true.csv"
newfile="../data/lists/spz/dataset1-1.csv"

tmp=`cat $from`
cnt=1
cp $into $newfile

while read line
do 
	#echo $line
	#line="ahoj"
	sed -i "$((cnt*insert_freq))i $line" $newfile
	cnt=$((cnt+1))
done <$from
echo $(((cnt - 2)*insert_freq))
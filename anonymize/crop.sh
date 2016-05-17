#!/usr/bin/env bash

#identify --version
if [ $1 = "" ]; then 
	imgpath="../img"
else
	imgpath=$1
fi

ls $imgpath

files=`ls $imgpath`
#files="out_002187.jpg out_003240.jpg"
mkdir $imgpath/crops

for img in $files
do
	img_cut=`echo ${img%.*}`
	cp $imgpath/$img subspace.jpg
	mogrify -crop 12288x1575+0+3108 subspace.jpg
	for i_vert in {0..36}
	do
		for i_hor in {0..6}
		do
			filename=$imgpath/crops/$img_cut+section$i_vert-$i_hor.jpg
			cp subspace.jpg $filename
			mogrify -crop 332x225+$((332*i_vert))+$((225*i_hor)) $filename
			#rm $img_section_$i_vert+$i_hor.jpg
		done
	done
done

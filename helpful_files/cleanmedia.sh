#!/usr/bin/bash

# Prepare our file destiations:
PICS=~/Downloads/Media/PICS
MP3=~/Downloads/Media/MP3
WAV=~/Downloads/Media/WAV
VIDS=~/Downloads/Media/VIDS
PDF=~/Downloads/DOCS/PDFs
CSV=~/Downloads/DOCS/CSV
DOC=~/Downloads/DOCS/DOCX
TXT=~/Downloads/DOCS/TXT
MOBI=~/Downloads/DOCS/MOBI
XLX=~/Downloads/DOCS/XLSX
ZIP=~/Downloads/ZIPS

# Change into our appropriate directory
cd ~/

# Start moving files:
mv *jpg *jpeg *png $PICS
mv *mp3 $MP3
mv *wav $WAV
mv *pdf $PDF
mv *csv $CSV
mv *doc *docx $DOC
mv *txt $TXT
mv *mkv *mp4 $VIDS

rm -f mono_crash*

cd ~/Downloads
mv *jpg *jpeg *png $PICS
mv *mp3 $MP3
mv *wav $WAV
mv *pdf $PDF
mv *csv $CSV
mv *doc *docx $DOC
mv *txt $TXT
mv *zip $ZIP
mv *mobi *epub $MOBI
mv *xls* *xlx* $XLX
#!/bin/sh
mkdir -p public
cp -r main public/main
cp -r studfinder public/studfinder
cp -r metaldetector public/metaldetector
cp -r protractor public/protractor
cp -r tcgvault public/tcgvault
cp -r volumebooster public/volumebooster
cp -r limify public/limify
cp -r colorzy public/colorzy
cp -r decibelmeter public/decibelmeter
cp -r dartsscorer public/dartsscorer
cp -r styles public/styles
cp -r scripts public/scripts
for dir in public/main public/tcgvault public/studfinder public/metaldetector public/volumebooster public/protractor public/limify public/colorzy public/decibelmeter public/dartsscorer; do
  [ -f "$dir/index.html" ] && mv "$dir/index.html" "$dir/home.html"
done

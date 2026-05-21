#!/bin/sh
mkdir -p public
cp -r main public/main
cp -r studfinder public/studfinder
cp -r protractor public/protractor
cp -r tcgvault public/tcgvault
cp -r volumebooster public/volumebooster
cp -r limify public/limify
cp -r coloringpage public/coloringpage
cp -r styles public/styles
cp -r scripts public/scripts
for dir in public/main public/tcgvault public/studfinder public/volumebooster public/protractor public/limify public/coloringpage; do
  [ -f "$dir/index.html" ] && mv "$dir/index.html" "$dir/home.html"
done

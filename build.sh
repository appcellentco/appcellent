#!/bin/sh
mkdir -p public
cp -r main public/main
cp -r studfinder public/studfinder
cp -r tcgvault public/tcgvault
cp -r styles public/styles
cp -r scripts public/scripts
mv public/main/index.html public/main/home.html
mv public/tcgvault/index.html public/tcgvault/home.html
mv public/studfinder/index.html public/studfinder/home.html

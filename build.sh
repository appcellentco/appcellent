#!/bin/sh
mkdir -p public
cp -r main public/main
cp -r studfinder public/studfinder
cp -r tcgvault public/tcgvault
cp -r styles public/styles
cp -r scripts public/scripts
for dir in public/main public/tcgvault public/studfinder; do
  [ -f "$dir/index.html" ] && mv "$dir/index.html" "$dir/home.html"
done

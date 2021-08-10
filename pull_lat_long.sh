#!/usr/bin/env bash

if [[ ! -f gps ]]; then
  gcc gpsconvert.c -o gps
fi

for fname in data/*; do

  short_name=$(echo "${fname}" | cut -d '/' -f 2)
  result=$(./exif/Image-ExifTool-12.29/exiftool ${fname})

  lat=$(echo "${result}" | grep "GPS Latitude  " | cut -d ":" -f 2 | ./gps)
  long=$(echo "${result}" | grep "GPS Longitude  " | cut -d ':' -f 2 | ./gps)

  echo "${short_name},${lat},${long}"

done

/*
Copyright © 2021 Alexander L. Hayes
MIT License

Super simple program to parse a "degree, minute, second, hemisphere" string
(like the ones output by ExifTool) and convert them into float coordinates.

Usage
-----

gcc gpsconvert.c -o gps
echo " 39 deg 9' 56.95\" N" | ./gps
*/

#include <stdio.h>
#include <math.h>

int main() {
  float deg, min, sec;
  char hem;

  scanf(" %f deg %f' %f\" %c", &deg, &min, &sec, &hem);

  min = min / 60;
  sec = sec / 60 / 60;
  deg = deg + min + sec;

  if (hem == 'N' || hem == 'E') {}
  else if (hem == 'S' || hem == 'W') {
    deg = deg * -1;
  }

  printf("%f\n", deg);

  return 0;
}

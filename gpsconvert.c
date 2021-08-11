/*
Copyright © 2021 Alexander L. Hayes
MIT License

Super simple program to parse a "degree, minute, second, hemisphere" string
(like the ones output by ExifTool) and convert them into float coordinates.

Usage
-----

```
gcc gpsconvert.c -o gps
echo " 39 deg 9' 56.95\" N" | ./gps
```

Passing any additional input will ignore stdin and run unittests instead:

```
gcc gpsconvert.c -o gps
./gps test
```
*/

#include <stdio.h>


/// Convert a string representing latitude or longitude coordinates into a
/// floating point representation.
///
/// Notes
/// -----
///
/// Float may not be an appropriate type here since degrees/minutes/seconds
/// should translate into something that can be stored with far less precision.
float convert(char input_string[])
{
  float deg, min, sec;
  char hem;

  sscanf(input_string, " %f deg %f' %f\" %c", &deg, &min, &sec, &hem);

  min = min / 60;
  sec = sec / 60 / 60;
  deg = deg + min + sec;

  if (hem == 'S' || hem == 'W') {
    deg = deg * -1;
  }

  return deg;
}

int _tester(char input_data[], float expected)
{
  float result = convert(input_data);
  return result == expected;
}

int _test_1() { return _tester(" 39 deg 9\' 56.95\" N", 39.165821); }
int _test_2() { return _tester(" 45 deg 25\' 47.90\" W", -45.429974); }

int unittest()
{
  typedef int (*IntFunc)(void);
  IntFunc functions[2] = { _test_1, _test_2 };

  int i = 0;
  int UNITTEST_SIZE = sizeof(functions)/sizeof(functions[0]);
  int return_bit = 0;

  while (i < UNITTEST_SIZE) {

    if ((*functions[i]) () == 0) {
      printf("%d ", i);
      return_bit = 1;
    } else {
      printf(". ");
    }

    i++;
  }
  printf("\n");

  return return_bit;
}


int main(int argc, char *argv[])
{
  if (argc > 1) {
    printf("Unit Testing:\n");
    return unittest();
  }

  char input_data[30];
  fgets(input_data, 30, stdin);

  printf("%f\n", convert(input_data));

  return 0;
}

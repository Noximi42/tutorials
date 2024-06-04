#include <cmath>
#include <iostream>

double pointBeforeLast = NAN;
double pointLast = NAN;

bool detectPoint(double value) {
  bool localMinimumDetected = false;

  if (pointBeforeLast == NAN) {
    pointBeforeLast = value;
    return false;
  }

  if (pointLast == NAN) {
    pointLast = value;
    return false;
  }

  if (pointBeforeLast > pointLast && pointLast < value) {
    localMinimumDetected = true;
  }

  pointBeforeLast = pointLast;
  pointLast = value;

  return localMinimumDetected;
}

int main() {
  int values[] = {1, 2, 3, 4, 3, 4, 5};
  int length = sizeof(values) / sizeof(int);

  for (int i = 0; i < length; i++) {
    bool minDetected = detectPoint(values[i]);
    if (minDetected) {
      std::cout << "Local Minimum at: (" << i - 1 << "," << values[i - 1] << ")"
                << std::endl;
    }
  }

  return 0;
}

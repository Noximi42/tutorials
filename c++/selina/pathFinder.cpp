#include <stdio.h>

int pathCount = 0;

void PrintPath(
    // DO NOT MODIFY THIS FUNC
    int grid[9][9], int path[17], int pathLength, int target) {

  int sum = 0;
  for (int i = 0; i < pathLength; i++) {
    int row = path[i] / 9;
    int col = path[i] % 9;
    sum += grid[row][col];
    printf("(%d,%d)=%d", row, col, grid[row][col]);
    if (i < pathLength - 1)
      printf("->");
  }
  printf(" => %d", sum);
  printf("\n");
}

void FindPath(int grid[9][9], // the grid
              int row,        // current row
              int col,        // current column
              int target,     // target sum to achieve
              int currentSum, // current sum along the path
              int path[17],   // array to store path (as 1D indices)
              int pathLength  // current length of path
) {
  // Your code here
  // Do not forget to call PrintPath in this function.

  if (currentSum > target) {
    return;
  }

  if (pathLength == 17 && currentSum == target) {
    PrintPath(grid, path, pathLength, target);
    pathCount++;
    return;
  }

  pathLength++;

  if (row < 8) {
    int newRow = row + 1;
    int newCurrentSum = currentSum + grid[newRow][col];

    int newPath[17];
    for (int i = 0; i < pathLength - 1; i++) {
      newPath[i] = path[i];
    }
    newPath[pathLength - 1] = newRow * 9 + col;
    
    FindPath(grid, newRow, col, target, newCurrentSum, newPath, pathLength);
  }

  if (col < 8) {
    int newCol = col + 1;
    int newCurrentSum = currentSum + grid[row][newCol];

    int newPath[17];
    for (int i = 0; i < pathLength - 1; i++) {
      newPath[i] = path[i];
    }
    newPath[pathLength - 1] = row * 9 + newCol;

    FindPath(grid, row, newCol, target, newCurrentSum, newPath, pathLength);
  }
}

int main() {
  int grid[9][9] = {{2, 4, 1, 3, 5, 3, 2, 1, 4}, {1, 5, 2, 4, 1, 2, 3, 4, 2},
                    {3, 1, 4, 2, 3, 4, 1, 5, 2}, {2, 3, 1, 4, 2, 1, 3, 2, 4},
                    {4, 2, 3, 1, 4, 3, 2, 4, 1}, {1, 4, 2, 3, 1, 4, 2, 1, 3},
                    {3, 1, 4, 2, 3, 1, 4, 2, 1}, {2, 3, 1, 4, 2, 3, 1, 3, 2},
                    {1, 2, 3, 1, 4, 2, 3, 1, 2}};

  int path[17] = {0}; // store indices of current path (1D)

  int target = 33; // target sum to find
  FindPath(grid, 0, 0, target, grid[0][0], path, 1);

  printf("%d paths found\n", pathCount);
  return 0;
}

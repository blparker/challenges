#include <stdio.h>
#include <string.h>
#include <unistd.h>

int main(int argc, char *argv[], char **envp) {
  printf("HELLO\n");
  const int CASES = 4;

  int data[CASES][4];
  memset(data, 0, CASES * 4 * sizeof(int));

  for (int i = 0; i < CASES; i++) {
    printf("%d", i);
    for (int j = 0; j < 4; j++) {
      data[i][j] = 0;
    }
  }

}


#include <stdio.h>

int main(int argc, char *argv[], char **envp) {
  int coin = atoi(argv[1]);
  int result = run(coin);
  printf("%d\n", result);
}

int run(int coin) {
  if(coin == 0) {
    return 1;
  }

  return run(coin / 2) +
         run(coin / 3) +
         run(coin / 4);
}


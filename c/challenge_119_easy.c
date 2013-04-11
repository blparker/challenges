#include <stdio.h>

int main(int argc, char *argv[], char **envp) {
  float number = atof(argv[1]);

  /*printf("Enter decimal number: ");
  scanf("%d", &number);
  printf("The number you typed was %d\n", number);*/
  printf("You entered %f\n", number);

  return;
}

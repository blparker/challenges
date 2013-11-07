#include <stdio.h>
#include <string.h>
#include <unistd.h>

int main(int argc, char *argv[], char **envp) {
  char *str = "2d20";

  int len = strlen(str);
  for (int i = 0; i < len; i++) {
    printf("%c\n", str[i]);
  }

  printf("%s\n", str);
  char *splat[] = split();
}

char* split(char *str) {
  char *test[] = {
    "2", "d", "20"
  };
  return test;
}

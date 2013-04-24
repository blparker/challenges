package main

import (
  "fmt"
  "os"
  "strconv"
)

func main() {
  args := os.Args;
  coin, err := strconv.Atoi(args[1])
  if err != nil {
    os.Exit(2)
  }
  res := run(coin)
  fmt.Println(res)
}

func run(coin int) int {
  if coin == 0 {
    return 1
  }

  return run(coin / 2) +
         run(coin / 3) +
         run(coin / 4)
}


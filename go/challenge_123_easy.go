package main

import (
  "fmt"
  "os"
  "bufio"
  "io"
  "strings"
)

func main() {
  args := os.Args
  file := args[1]
  //mode := args[2]

  fi, err := os.Open(file)
  if err != nil { panic(err) }

  defer func() {
    if err := fi.Close(); err != nil {
      panic(err)
    }
  }()

  reader := bufio.NewReader(fi)

  for {
    line, err := reader.ReadString('\n')
    if err != nil && err != io.EOF {
      panic(err)
    }

    line = strings.Replace(strings.Replace(line, "\r", "", -1), "\n", "", -1)

    if err == io.EOF {
      break
    }

    fmt.Println(line)
  }
}


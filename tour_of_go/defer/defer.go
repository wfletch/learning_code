package main

import "fmt"

func main() {
	name := "Warren"
	defer fmt.Println(name)
	name = "Julia"
	fmt.Println(name)
}

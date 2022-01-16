package main

import "fmt"

func main() {
	name := "Warren"
	defer fmt.Println(name)
	name = "Julia"
	defer fmt.Println(name)
	name = "Lauren"
	defer fmt.Println(name)
}

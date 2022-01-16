package main

import "fmt"

func add(x int, y int) int {
	return x + y
}
func swap(x, y string) (string, string) {
	return y, x
}
func main() {
	fmt.Println(add(7, 8))
	fmt.Println(swap("Fletcher", "Warren"))
}

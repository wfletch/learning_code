package main

import "fmt"

type Pair struct {
	X int
	Y int
}

func main() {
	i, j := 42, 43
	p := &i         // Pointer!
	fmt.Println(*p) // Read the value at p
	*p = 21 * j
	fmt.Println(i)

	point := Pair{1, 2}
	fmt.Println(point.X)
}

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
	pair_pointer := &point
	pair_pointer.Y = 7
	fmt.Printf("%d %d", point.X, point.Y)
	for i := 0; i == 10; i++ {
		x := Pair{}
		x.X = 3
	}
}

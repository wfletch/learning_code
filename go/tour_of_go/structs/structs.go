package main

import "fmt"

type Vertex struct {
	X int
	Y int
}

func main() {
	v := Vertex{1, 2}
	v.X = 400
	p := &v
	p.X = 1e9
	a := Vertex{}
	b := Vertex{X: -1}
	c := &Vertex{1, 2}
	fmt.Println(a, b, *c)
	fmt.Println(v.X)
}

package main

import "fmt"

var c, python, java bool = true, false, false

func main() {
	var i, j = false, "No!"
	fmt.Println("vim-go")
	fmt.Println(i, j, c, python, java)
	var l int
	var b bool
	var s string
	var c complex128
	k := "test"

	fmt.Println("%v %v %v %q\ngolan", l, b, s, c)
	fmt.Println(k)
}

package main

import "fmt"

func main() {
	var array [4]string
	for i := 0; i < len(array); i++ {
		array[i] = fmt.Sprint(i)
	}
	fmt.Println(array)

}

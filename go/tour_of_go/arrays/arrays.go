package main

import "fmt"

func main() {
	var array [4]string
	for i := 0; i < len(array); i++ {
		array[i] = fmt.Sprint(i)
	}
	var names [10]string
	names[0] = "Warren"
	names[1] = "Fletcher"
	names[2] = "Hamilton"
	names[3] = "Meow"
	fmt.Println(array)
	fmt.Println(names)

}

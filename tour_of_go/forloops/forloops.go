package main

import "fmt"

func main() {
	sum := 0
	for i := 0; i < 10; i++ {
		sum += i
	}
	pre_var := 0
	for pre_var < 1000 {
		pre_var += 1
		fmt.Printf("Current Value Of Pre Var is: %d \n", pre_var)
	}
	fmt.Printf("The Sum is:\t %v", sum)
}

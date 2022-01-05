package main

import (
	"fmt"
	"math"
)

func sqrt(x float64) float64 {
	error_margin := 1e-3
	guess := 1.0
	for {
		result := math.Pow(guess, 2)
		if math.Abs(x-result) <= error_margin {
			return guess
		} else {
			if result > x {
				guess -= 0.0001
			} else {
				guess += 0.0001
			}
		}
	}
}

func main() {
	fmt.Println(sqrt(5))
}

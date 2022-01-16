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
				guess -= error_margin / 10
			} else {
				guess += error_margin / 10
			}
		}
	}
}

func main() {
	fmt.Printf("%f.", sqrt(42))

}

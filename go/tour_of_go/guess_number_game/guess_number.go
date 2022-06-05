package main

import (
	"fmt"
)

func main() {
	fmt.Println("Enter lower Bound:")
	lower_bound := 0
	fmt.Scanln(&lower_bound)
	fmt.Println("Enter upper Bound:")
	upper_bound := 0
	fmt.Scanln(&upper_bound)
	if lower_bound == upper_bound {
		fmt.Printf("Your Number is: %d", lower_bound)
		return
	}
	if lower_bound > upper_bound {
		fmt.Printf("Your Upper Bound is lower than your Lower Bound")
		return
	}
	// Game is Valid!
	guess_count := 1
	for {
		guess := lower_bound + int((upper_bound-lower_bound)/2)
		for {
			fmt.Printf("I guess... %d \n", guess)
			fmt.Println("Am I (c)orrect, too (l)ow, or too (h)igh")
			user_input := ""
			fmt.Scanln(&user_input)
			if string(user_input) == "c" {
				fmt.Printf("It took me %d guesses", guess_count)
				return
			}
			if string(user_input) == "l" {
				lower_bound = guess
				break
			}
			if string(user_input) == "h" {
				upper_bound = guess
				break
			}
		}
		guess_count += 1
	}

}

package main

import (
	"fmt"
	"runtime"
)

func main() {
	fmt.Println("This Version of Go is running on ")
	switch os := runtime.GOOS; os {
	case "darwin":
		fmt.Println("OS X.")
	case "linux":
		fmt.Println("Linux")
	default:
		fmt.Printf("%s \n", os)

	}

}

package main

import (
	"fmt"
	"time"
)

func main() {
	done := make(chan bool)
	start := time.Now()
	for i := 0; i < 5; i++ {
		go func(x int) {
			time.Sleep(time.Duration(x+1) * time.Second)
			done <- true
		}(i)
	}
	for i := 0; i < 5; i++ {
		<-done
	}
	fmt.Printf("done %v\n", time.Since(start))
}

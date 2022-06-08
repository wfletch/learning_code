package main

import (
	"fmt"
	"time"
)

func main() {
	c := make(chan bool)
	// Channels are synchronous.
	// Someone needs to receive after a send!
	go func() {
		time.Sleep(1 * time.Second)
		<-c
		println("Finished Receving!")
	}()
	start := time.Now()
	c <- true // This is us Sending! We are going to block until the other goroutine receives the date.
	fmt.Printf("Send took %v\n", time.Since(start))
}

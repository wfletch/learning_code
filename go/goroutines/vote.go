package main

import (
	"math/rand"
	"sync"
	"time"
)

func main() {
	rand.Seed(time.Now().UnixNano())
	count := 0
	finished := 0
	var mu sync.Mutex
	cond := sync.NewCond(&mu)
	for i := 0; i < 10; i++ {
		go func() {
			vote := requestVote()
			mu.Lock()
			defer mu.Unlock()
			if vote {
				count++
			}
			finished++
			cond.Broadcast() // Wake's up whoever is waiting on this condition variable
		}()
	}
	// This is a design pattern
	mu.Lock()
	for count < 5 && finished != 10 { // While this loop is false, we wait for the broadcast, which will wake us up.
		cond.Wait() // Waits on this condition variable!
	}
	if count >= 5 {
		println("Received 5+ votes!")
	} else {
		println("lost")
	}
	mu.Unlock()
}
func requestVote() bool {
	return true
}

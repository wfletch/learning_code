package main

import (
	"sync"
	"time"
)

var mu sync.Mutex
var done bool

func main() {
	time.Sleep(1 * time.Second)
	println("started")
	go periodic()
	time.Sleep(5 * time.Second)
	mu.Lock()
	done = true
	mu.Unlock()
	println("Cancelled")
	time.Sleep(3 * time.Second)
}

func periodic() {
	for {
		println("tick")
		time.Sleep(1 * time.Second)
		mu.Lock()
		// This is to secure the variable
		if done {
			mu.Unlock()
			return
		}
		mu.Unlock()
	}
}

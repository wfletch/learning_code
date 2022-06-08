package main

import "sync"

func sendRPC(x int) {
	println(x)
}
func main() {
	var a string
	var wg sync.WaitGroup
	for i := 0; i < 500000; i++ {
		wg.Add(1)
		go func(x int) { // This is defined as a closure
			sendRPC(x)
			wg.Done()
		}(i)
	}
	wg.Wait()
	println(a)
}

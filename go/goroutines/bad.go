package main

import "sync"

func sendRPC(x int) {
	println(x)
}
func main() {
	var a string
	var wg sync.WaitGroup
	for i := 0; i < 5; i++ {
		wg.Add(1)
		go func() { // This is defined as a closure
			sendRPC(i)
			wg.Done()
		}()
	}
	wg.Wait()
	println(a)
}

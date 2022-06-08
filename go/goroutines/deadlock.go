package main

func main() {
	c := make(chan bool, 20) //Ok, now things get a little interesting
	c <- true
	<-c
	// So, buffered channels.
	// We can add content but we will only block once the capacity of the buffer has been reached,
	// Interesting use case. But it would make sense for aggregation and forwarding.
}

package main

import "testing"

func TestHelloWorld(t *testing.T) {
	got := Hello("Warren")
	want := "Hello, Warren"

	if got != want {
		t.Errorf("Got %q want %q", got, want)
	}
}

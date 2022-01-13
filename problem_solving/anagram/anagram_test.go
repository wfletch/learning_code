package main

import "testing"

func TestCheckAnagram(t *testing.T) {
	got := CheckAnagram("Warren")
	want := true

	if got != want {
		t.Errorf("got %t want %t", got, want)
	}
}

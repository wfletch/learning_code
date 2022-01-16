package main

import "testing"

func assertTestingResult(t testing.TB, want, got int) {
	if want != got {
		t.Errorf("expected '%d' but got '%d'", want, got)
	}
}
func TestHelloWorld(t *testing.T) {
	t.Run("Adding Two Numbers (2,4)", func(t *testing.T) {
		want := 6
		got := add(2, 4)
		assertTestingResult(t, want, got)
	})
	t.Run("Adding Two Negative Numbers", func(t *testing.T) {
		want := -3
		got := add(-1, -2)
		assertTestingResult(t, want, got)
	})
	// t.Fatal("not implemented")
}

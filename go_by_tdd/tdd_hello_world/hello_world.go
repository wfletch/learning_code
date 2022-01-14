package main

import "fmt"

func Hello(name string, lang string) string {
	prefix := "Hello, "
	if name == "" {
		name = "World"
	}
	if lang == "Spanish" {
		prefix = "Hola, "
	}
	return prefix + name
}

func main() {
	fmt.Println(Hello("Warren", ""))
}

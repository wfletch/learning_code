package main

import "fmt"

const englishHelloPrefix = "Hello, "
const spanish = "Spanish"
const french = "French"
const spanishHelloPrefix = "Hola, "
const frenchHelloPrefix = "Bonjour, "

func getLanguagePrefix(lang string) (prefix string) {
	switch lang {
	case spanish:
		prefix = spanishHelloPrefix
	case french:
		prefix = frenchHelloPrefix
	default:
		prefix = englishHelloPrefix
	}
	return
}
func Hello(name string, lang string) string {
	if name == "" {
		name = "World"
	}
	return getLanguagePrefix(lang) + name
}

func main() {
	fmt.Println(Hello("Warren", ""))
}

package main

import "fmt"

func main() {
	s := make([]int, 3, 5)

	fmt.Println(s, len(s))

	a := append(s, 4)
    a[0] = 1; // this is stupid
	fmt.Println(s, len(s), cap(s), a, len(a), cap(a))
}

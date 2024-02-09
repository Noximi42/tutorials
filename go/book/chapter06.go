package main

import "fmt"

func main() {
	s := []int{1, 2, 3, 4, 5, 6, 9, 25}
	fmt.Println(sum(s))

    fmt.Println(half(1))
	fmt.Println(half(2))
	
    fmt.Println(max(s...))

	nextOdd := makeOddGenerator()
	fmt.Println(nextOdd())
	fmt.Println(nextOdd())
	fmt.Println(nextOdd())
	fmt.Println(nextOdd())

	fmt.Println(fibo(1))
	fmt.Println(fibo(2))
	fmt.Println(fibo(3))
	fmt.Println(fibo(4))
	fmt.Println(fibo(5))
	fmt.Println(fibo(6))

	pan()

	v1 := 5
	v2 := 7
	swap(&v1, &v2)
	fmt.Println(v1, v2)
}

func swap(v1 *int, v2 *int) {
    *v1 = *v1 + *v2
    *v2 = *v1 - *v2
    *v1 = *v1 - *v2
}

func pan() {
	defer func() {
		r := recover()
		fmt.Println(r)
	}()

	panic("heeeelp!!!")
}

func fibo(n int) int {
	if n <= 1 {
		return 1
	}
	return fibo(n-1) + fibo(n-2)
}

func sum(s []int) int {
	r := 0
	for _, value := range s {
		r += value
	}

	return r
}

func half(v int) (int, bool) {
	return v / 2, v%2 == 0
}

func max(values ...int) int {
	m := 0
	for _, value := range values {
		if value > m {
			m = value
		}
	}
	return m
}

func makeOddGenerator() func() uint {
	odd := uint(1)
	return func() (ret uint) {
		ret = odd
		odd += 2
		return
	}
}

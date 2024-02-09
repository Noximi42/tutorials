package main

import (
	"fmt"
	"math"
)

type Shape interface {
	Area() float64
	Perimeter() float64
}

type Circle struct {
	x, y, r float64
}

func (c *Circle) Area() float64 {
	return math.Pi * c.r * c.r
}

func (c *Circle) Perimeter() float64 {
	return 2 * math.Pi * c.r
}

type Rectangle struct {
	x, y float64
}

func (r *Rectangle) Area() float64 {
	return r.x * r.y
}

func (r *Rectangle) Perimeter() float64 {
	return 2*r.x + 2*r.x
}

func main() {
	c1 := Circle{x: 1, y: 2, r: 3}
	c2 := Circle{x: 2, y: 3, r: 4}
	r1 := Rectangle{x: 2, y: 3}

	fmt.Println(c1.Area())
	fmt.Println(c2.Area())
	fmt.Println(r1.Area())
	fmt.Println(TotalArea(&c1, &c2, &r1))

	fmt.Println()
	fmt.Println(c1.Perimeter())
	fmt.Println(c2.Perimeter())
	fmt.Println(r1.Perimeter())
	fmt.Println(TotalPerimeter(&c1, &c2, &r1))
}

func TotalArea(shapes ...Shape) float64 {
	total := 0.0
	for _, s := range shapes {
		total += s.Area()
	}
	return total
}

func TotalPerimeter(shapes ...Shape) float64 {
	total := 0.0
	for _, s := range shapes {
		total += s.Perimeter()
	}
	return total
}

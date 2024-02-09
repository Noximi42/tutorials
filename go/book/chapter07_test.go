package main

import "testing"

type TestPairs struct {
	c    Circle
	area float64
}

var tests = []TestPairs{
	{c: Circle{x: 1, y: 2, r: 3}, area: 3},
	{c: Circle{x: 2, y: 3, r: 4}, area: 5},
}

func TestTotalArea(t *testing.T) {
	for _, pair := range tests {
		area := TotalArea(&pair.c)
		if area != pair.area {
			t.Error(
				"For", pair.c,
				"expected", pair.area,
				"got", area,
			)
		}

	}
}

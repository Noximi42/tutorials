package main

type Person interface {
	oldEnough() bool
}

type Young struct {
	age int
}

type Old struct {
	age int
}

func (a *Young) oldEnough() bool {
	return a.age >= 18
}

func (o *Old) oldEnough() bool {
	return o.age >= 70
}

type Human struct {
	Young
    Old
}

func main() {
	var h Human

    h.Young.age = 15
    h.oldEnough()
}

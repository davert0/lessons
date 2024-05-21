package lesson7

import (
	"fmt"
	"time"
)

type GoogleSheetCell interface {
	ExtractData()
}

type DateCell struct {
	value time.Time
}

func (d *DateCell) ExtractData() {
	fmt.Println(d.value.Format("02.01.2006 15:04:05"))
}

type StringCell struct {
	value string
}

func (s *StringCell) ExtractData() {
	fmt.Println(s.value)
}

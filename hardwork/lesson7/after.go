package lesson7

import (
	"fmt"
	"time"
)

type (
	GoogleSheetCell_ interface {
		Accept(v Visitor) error
	}

	Visitor interface {
		VisitDateCell(cell *DateCell_) error
		VisitStringCell(cell *StringCell_) error
	}

	DateCell_ struct {
		value time.Time
	}

	StringCell_ struct {
		value string
	}
)

func (d *DateCell_) Accept(v Visitor) error {
	return v.VisitDateCell(d)
}

func (s *StringCell_) Accept(v Visitor) error {
	return v.VisitStringCell(s)
}

type CellDataExtractorVisitor struct{}

func (c *CellDataExtractorVisitor) VisitDateCell(cell *DateCell_) error {
	fmt.Println(cell.value.Format("02.01.2006 15:04:05"))
	return nil
}

func (c CellDataExtractorVisitor) VisitStringCell(cell *StringCell_) error {
	fmt.Println(cell.value)
	return nil
}

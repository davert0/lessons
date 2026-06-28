package main

import (
	"os"
)

// Порядковый номер - 11
// Номер задачи - 2
// Краткое название - слияние блум фильтров
// Сложность временная O(N) - проход по N фильтрам, пространственная O(1) - один результирующий
// Рефлексия - слияние через побитовое "или", вероятность ложноположительных растет, так как больше
// выставленных единичек
func Merge(filters ...*BloomFilter) *BloomFilter {
	if len(filters) == 0 {
		return &BloomFilter{}
	}

	size := filters[0].filter_len
	for _, f := range filters {
		if f.filter_len != size {
			return nil
		}
	}

	merged := &BloomFilter{
		filter_len: size,
	}

	for _, f := range filters {
		merged.filter |= f.filter
	}

	return merged
}

// Порядковый номер - 11
// Номер задачи - 3
// Краткое название - фильтр блюма с удалением
// Сложность Add/Remove/IsValue - O(k), k - число хэш-функций; пространственная O(M), M - размер фильтра
// Рефлексия - счетчик нужен, чтобы при удалении колизионных битов не удалить биты другого значения, тем самым не допустить
// ложноотрицательные срабатывания
type CountingBloomFilter struct {
	counters   []int
	filter_len int
}

func NewCountingBloomFilter(filter_len int) *CountingBloomFilter {
	return &CountingBloomFilter{
		counters:   make([]int, filter_len),
		filter_len: filter_len,
	}
}

func (f *CountingBloomFilter) hashes(s string) (int, int) {
	bf := BloomFilter{filter_len: f.filter_len}
	return bf.Hash1(s), bf.Hash2(s)
}

func (f *CountingBloomFilter) Add(s string) {
	h1, h2 := f.hashes(s)
	f.counters[h1]++
	f.counters[h2]++
}

func (f *CountingBloomFilter) IsValue(s string) bool {
	h1, h2 := f.hashes(s)
	return f.counters[h1] > 0 && f.counters[h2] > 0
}

func (f *CountingBloomFilter) Remove(s string) bool {
	if !f.IsValue(s) {
		return false
	}
	h1, h2 := f.hashes(s)
	f.counters[h1]--
	f.counters[h2]--
	return true
}

// Порядковый номер - 11
// Номер задачи - 4
// Краткое название - попытка восстановления исходного множества по конфигурации фильтра
// Рефлексия - честно говоря, не особо понимаю, как из маски восстановить исходное множество, ведь мы всегда теряем
// исходное значение при проставлении его в фильтр
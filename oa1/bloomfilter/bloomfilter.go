package bloomfilter

type BloomFilter interface {
	// команды

	//Постусловие - элмент добавлен в фильтр
	Add(v string)

	// Запросы

	IsValue(v string) bool
}

type BloomFilterImpl struct {
	filterLen uint
	filter    uint64
}

func NewBloomFilter(fLen uint) BloomFilter {
	return &BloomFilterImpl{
		filterLen: fLen,
		filter:    0,
	}
}

func (bf *BloomFilterImpl) hash1(str1 string) uint {
	var result uint = 0
	for _, c := range str1 {
		code := uint(c)
		result = (result*17 + code) % bf.filterLen
	}
	return result
}

func (bf *BloomFilterImpl) hash2(str1 string) uint {
	var result uint = 0
	for _, c := range str1 {
		code := uint(c)
		result = (result*223 + code) % bf.filterLen
	}
	return result
}

func (bf *BloomFilterImpl) Add(str1 string) {
	hash1 := uint64(1) << bf.hash1(str1)
	hash2 := uint64(1) << bf.hash2(str1)
	bf.filter = bf.filter | hash1
	bf.filter = bf.filter | hash2
}

func (bf *BloomFilterImpl) IsValue(str1 string) bool {
	hash1 := uint64(1) << bf.hash1(str1)
	hash2 := uint64(1) << bf.hash2(str1)
	return (bf.filter|hash1) == bf.filter && (bf.filter|hash2) == bf.filter
}

from heap import Heap

def test_create_heap_with_7_nodes():
    test_arr = [1, 2, 6, 4, 8, 5, 3]

    heap = Heap().MakeHeap(test_arr, 2)

    assert [8, 6, 5, 1, 4, 2, 3] == heap
package main

import (
	"errors"
	"os"
	"reflect"
)

type Node struct {
	prev  *Node
	next  *Node
	value int
}

type LinkedList2 struct {
	head *Node
	tail *Node
}

func (l *LinkedList2) AddInTail(item Node) {
	if l.head == nil {
		l.head = &item
		l.head.next = nil
		l.head.prev = nil
	} else {
		l.tail.next = &item
		item.prev = l.tail
	}

	l.tail = &item
	l.tail.next = nil
}

func (l *LinkedList2) Count() int {
	count := 0
	node := l.head
	for node != nil {
		count += 1
		node = node.next
	}
	return count
}

// error не nil, если узел не найден
func (l *LinkedList2) Find(n int) (Node, error) {
	node := l.head
	for node != nil {
		if node.value == n {
			return *node, nil
		}
		node = node.next
	}
	return Node{}, errors.New("node not found")
}

func (l *LinkedList2) FindAll(n int) []Node {
	var nodes []Node
	node := l.head
	for node != nil {
		if node.value == n {
			nodes = append(nodes, *node)
		}
		node = node.next
	}
	return nodes
}

func (l *LinkedList2) Delete(n int, all bool) {
	current := l.head
	for current != nil {
		if current.value == n {
			if current.prev != nil {
				current.prev.next = current.next
			} else {
				l.head = current.next
			}
			if current.next != nil {
				current.next.prev = current.prev
			} else {
				l.tail = current.prev
			}
			if !all {
				return
			}
		}
		current = current.next
	}
}

func (l *LinkedList2) Insert(after *Node, add Node) {
	if after == nil {
		add.next = l.head
		add.prev = nil
		if l.head != nil {
			l.head.prev = &add
		}
		l.head = &add
		if l.tail == nil {
			l.tail = &add
		}
		return
	}

	add.prev = after
	add.next = after.next
	after.next = &add

	if add.next != nil {
		add.next.prev = &add
	} else {
		l.tail = &add
	}
}

func (l *LinkedList2) InsertFirst(first Node) {
	node := l.head
	if node == nil {
		l.head = &first
		l.tail = &first
		return
	}

	l.head = &first
	first.next = node
	node.prev = &first
}

func (l *LinkedList2) Clean() {
	l.head = nil
	l.tail = nil
}

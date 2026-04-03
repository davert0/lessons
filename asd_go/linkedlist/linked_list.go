package main

import (
	"errors"
	"os"
	"reflect"
)

type Node struct {
	next  *Node
	value int
}

type LinkedList struct {
	head *Node
	tail *Node
}

func (l *LinkedList) AddInTail(item Node) {
	if l.head == nil {
		l.head = &item
	} else {
		l.tail.next = &item
	}

	l.tail = &item
}

func (l *LinkedList) Count() int {
	count := 0
	node := l.head
	for node != nil {
		count++
		node = node.next
	}
	return count
}

func (l *LinkedList) Find(n int) (Node, error) {
	node := l.head
	for node != nil {
		if node.value == n {
			return *node, nil
		}
		node = node.next
	}
	return Node{}, errors.New("node not found")
}

func (l *LinkedList) FindAll(n int) []Node {
	var nodes []Node
	curr := l.head
	for curr != nil {
		if curr.value == n {
			nodes = append(nodes, *curr)
		}
		curr = curr.next
	}
	return nodes
}

func (l *LinkedList) Delete(n int, all bool) {
	if all {
		l.deleteAll(n)
		return
	}

	l.deleteFirst(n)
}

func (l *LinkedList) Insert(after *Node, add Node) {
	if l.head == nil {
		l.head = &add
		l.tail = &add
		add.next = nil
		return
	}
	add.next = after.next
	after.next = &add
	if l.tail == after {
		l.tail = &add
	}
}

func (l *LinkedList) InsertFirst(first Node) {
	first.next = l.head
	l.head = &first
	if l.tail == nil {
		l.tail = &first
	}
}

func (l *LinkedList) Clean() {
	l.head = nil
	l.tail = nil
}

func (l *LinkedList) deleteFirst(n int) {
	if l.head == nil {
		return
	}
	if l.head.value == n {
		l.head = l.head.next
		if l.head == nil {
			l.tail = nil
		}
		return
	}
	prev := l.head
	curr := prev.next
	for curr != nil {
		if curr.value == n {
			prev.next = curr.next
			if curr == l.tail {
				l.tail = prev
			}
			return
		}
		prev = curr
		curr = curr.next
	}
}

func (l *LinkedList) deleteAll(n int) {
	for l.head != nil && l.head.value == n {
		l.head = l.head.next
	}
	if l.head == nil {
		l.tail = nil
		return
	}
	prev := l.head
	curr := prev.next
	for curr != nil {
		if curr.value == n {
			prev.next = curr.next
			if curr == l.tail {
				l.tail = prev
			}
			curr = prev.next
		} else {
			prev = curr
			curr = curr.next
		}
	}
}

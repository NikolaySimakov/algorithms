package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func diff(sum int, nxt int) (int, int) {
	if sum >= 10 {
		nxt = 1
		sum -= 10
	} else {
		nxt = 0
	}

	return sum, nxt
}

func newListNode(val int) *ListNode {
	l := ListNode{
		Val:  val,
		Next: nil,
	}
	return &l
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {

	head := newListNode(0)
	tail := head
	nxt := 0

	for l1 != nil && l2 != nil {
		s := l1.Val + l2.Val + nxt
		s, nxt = diff(s, nxt)

		tail.Next = newListNode(s)
		tail = tail.Next
		l1 = l1.Next
		l2 = l2.Next
	}

	var l *ListNode

	if l1 != nil {
		l = l1
	} else if l2 != nil {
		l = l2
	}

	for l != nil {
		s := l.Val + nxt
		s, nxt = diff(s, nxt)
		tail.Next = newListNode(s)
		tail = tail.Next
		l = l.Next
	}

	if nxt == 1 {
		tail.Next = newListNode(1)
	}

	return head.Next
}

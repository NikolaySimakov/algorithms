package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func setDefault() ListNode {
	ln := ListNode{}
	ln.Val = 0
	return ln
}

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {

	dummy := setDefault()
	tail := dummy

	for list1.Next != nil && list2.Next != nil {
		if list1.Val >= list2.Val {
			tail.Next = list2
			list2.Val = list2.Next.Val
			list2.Next = list2.Next.Next
		} else {
			tail.Next = list1
			list1.Val = list1.Next.Val
			list1.Next = list1.Next.Next
		}
	}

	if list1.Next == nil {
		for list2.Next != nil {
			tail.Next = list2
			list2.Val = list2.Next.Val
			list2.Next = list2.Next.Next
		}
	} else {
		for list1.Next != nil {
			tail.Next = list1
			list1.Val = list1.Next.Val
			list1.Next = list1.Next.Next
		}
	}

	return dummy.Next
}

func main() {
	a := setDefault()
	b := setDefault()

	fmt.Println(mergeTwoLists(a, b))

}

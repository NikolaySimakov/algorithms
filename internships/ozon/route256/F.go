package main

import (
	"encoding/json"
	"fmt"
)

type Category struct {
	ID     int
	Name   string
	Parent int
	Next   []*Category
}

func buildTree(categories []*Category) []*Category {
	categoryMap := make(map[int]*Category)

	for _, category := range categories {
		categoryMap[category.ID] = category
	}

	var root *Category

	for _, category := range categories {
		if category.Parent == 0 {
			root = category
		} else {
			parent := categoryMap[category.Parent]
			parent.Next = append(parent.Next, category)
		}
	}

	return []*Category{root}
}

func main() {
	var n int
	fmt.Scan(&n)

	categories := make([]*Category, n)
	for i := 0; i < n; i++ {
		category := &Category{}
		fmt.Scan(&category.ID, &category.Name, &category.Parent)
		categories[i] = category
	}

	tree := buildTree(categories)

	jsonTree, _ := json.Marshal(tree)
	fmt.Println(string(jsonTree))
}

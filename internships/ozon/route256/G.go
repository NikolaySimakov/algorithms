package main

import (
	"fmt"
	"sort"
)

type Card struct {
	Value string
	Suit  string
}

func main() {
	var n int
	fmt.Scan(&n)

	hands := make([][]Card, n)
	for i := 0; i < n; i++ {
		var m int
		fmt.Scan(&m)

		hand := make([]Card, m)
		for j := 0; j < m; j++ {
			var value, suit string
			fmt.Scan(&value, &suit)
			card := Card{Value: value, Suit: suit}
			hand[j] = card
		}
		hands[i] = hand
	}

	table := make([]Card, 1)
	fmt.Scan(&table[0].Value, &table[0].Suit)

	winners := findWinners(hands, table)
	fmt.Println(len(winners))
	for _, winner := range winners {
		fmt.Println(winner.Value + " " + winner.Suit)
	}
}

func findWinners(hands [][]Card, table []Card) []Card {
	maxComb := ""
	winners := make([]Card, 0)

	for _, hand := range hands {
		comb := getCombination(hand, table)
		if comb == maxComb {
			winners = append(winners, hand[0])
		} else if comb > maxComb {
			maxComb = comb
			winners = []Card{hand[0]}
		}
	}

	return winners
}

func getCombination(hand []Card, table []Card) string {
	cards := append(hand, table...)
	sort.Slice(cards, func(i, j int) bool {
		return getValueRank(cards[i].Value) > getValueRank(cards[j].Value)
	})

	if isSet(cards) {
		return "Set with value " + cards[0].Value
	} else if isPair(cards) {
		return "Pair with value " + cards[0].Value
	} else {
		return "Highest card " + cards[0].Value
	}
}

func isSet(cards []Card) bool {
	for i := 0; i < len(cards)-2; i++ {
		if cards[i].Value == cards[i+1].Value && cards[i].Value == cards[i+2].Value {
			return true
		}
	}
	return false
}

func isPair(cards []Card) bool {
	for i := 0; i < len(cards)-1; i++ {
		if cards[i].Value == cards[i+1].Value {
			return true
		}
	}
	return false
}

func getValueRank(value string) int {
	rank := map[string]int{
		"2":  2,
		"3":  3,
		"4":  4,
		"5":  5,
		"6":  6,
		"7":  7,
		"8":  8,
		"9":  9,
		"10": 10,
		"J":  11,
		"Q":  12,
		"K":  13,
		"A":  14,
	}
	return rank[value]
}

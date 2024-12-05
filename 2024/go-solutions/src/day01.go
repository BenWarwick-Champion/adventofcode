package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"
	"strconv"
	"strings"
)

// readLines reads a whole file into memory
// and returns a slice of its lines.
func readLines(path string) ([]string, error) {
	file, err := os.Open(path)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	return lines, scanner.Err()
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func part1(lines []string) int {
	list1 := []int{}
	list2 := []int{}

	for _, line := range lines {
		parts := strings.Split(line, "   ")
		a, _ := strconv.Atoi(parts[0])
		b, _ := strconv.Atoi(parts[1])

		list1 = append(list1, a)
		list2 = append(list2, b)
	}

	slices.Sort(list1)
	slices.Sort(list2)

	total := 0
	for i, a := range list1 {
		diff := abs(a - list2[i])
		total += diff
	}
	return total
}

func part2(lines []string) int {
	list1 := []int{}
	list2 := []int{}

	for _, line := range lines {
		parts := strings.Split(line, "   ")
		a, _ := strconv.Atoi(parts[0])
		b, _ := strconv.Atoi(parts[1])

		list1 = append(list1, a)
		list2 = append(list2, b)
	}

	m := make(map[int]int)
	for _, a := range list2 {
		m[a] += 1
	}

	total := 0
	for _, a := range list1 {
		total += m[a] * a
	}

	return total
}

func main() {
	lines, err := readLines("input/day01.txt")
	if err != nil {
		fmt.Println("File reading error", err)
		return
	}

	// Part 1
	fmt.Println("Part 1")
	fmt.Println(part1(lines))

	// Part 2
	fmt.Println("Part 2")
	fmt.Println(part2(lines))
}

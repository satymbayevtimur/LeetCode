func twoSum(nums []int, target int) []int {
    indices := make(map[int]int)

    for i, num := range nums {
        difference := target - num

        if index, ok := indices[difference]; ok {
            return []int{index, i}
        }

        indices[num] = i
    }

    return nil
}

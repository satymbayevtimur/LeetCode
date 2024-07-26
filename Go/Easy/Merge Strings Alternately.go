func mergeAlternately(word1 string, word2 string) string {
    var result []byte
    i, j := 0, 0
    length1, length2 := len(word1), len(word2)

    for i < length1 && j < length2 {
        result = append(result, word1[i])
        result = append(result, word2[j])
        i++
        j++
    }

    for i < length1 {
        result = append(result, word1[i])
        i++
    }

    for j < length2 {
        result = append(result, word2[j])
        j++
    }

    return string(result)
}

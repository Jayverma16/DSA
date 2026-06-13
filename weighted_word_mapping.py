# 3838. Weighted Word Mapping
reverse = {25 - i: chr(ord('a') + i) for i in range(26)}
non_reverse = {chr(ord('a') + i): i for i in range(26)}
class Solution:
    def mapWordWeights(self, words: list[str], weights: list[int]) -> str:
        answer = ""
        for word in words:
            answer += reverse[(sum([weights[non_reverse[letter]] for letter in word]) % 26)]
        return answer
        
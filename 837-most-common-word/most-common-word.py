class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # Convert to lowercase
        paragraph = paragraph.lower()

        # Replace punctuation with spaces
        for ch in "!?',;.":
            paragraph = paragraph.replace(ch, " ")

        banned_set = set(banned)
        count = Counter()

        # Count valid words
        for word in paragraph.split():
            if word not in banned_set:
                count[word] += 1

        # Return the most frequent word
        return max(count, key=count.get)
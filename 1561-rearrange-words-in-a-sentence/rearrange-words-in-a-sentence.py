class Solution:
    def arrangeWords(self, text: str) -> str:
        text = text[0].lower() + text[1:]
        
        words = text.split()
        words.sort(key=len)
        
        words[0] = words[0].capitalize()
        
        return " ".join(words)
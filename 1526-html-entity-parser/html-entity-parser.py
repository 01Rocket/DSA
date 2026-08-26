class Solution:
    def entityParser(self, text: str) -> str:
        entities = {
        "&quot;": '"',
        "&apos;": "'",
        "&amp;": "&",
        "&gt;": ">",
        "&lt;": "<",
        "&frasl;": "/"
        }

        result = []
        i = 0

        while i < len(text):
            if text[i] == '&':
                found = False

                for entity, character in entities.items():
                    if text.startswith(entity, i):
                        result.append(character)
                        i += len(entity)
                        found = True
                        break

                if found:
                    continue

            result.append(text[i])
            i += 1

        return ''.join(result)
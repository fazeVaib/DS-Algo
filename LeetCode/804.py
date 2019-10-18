class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        d = dict(zip("abcdefghijklmnopqrstuvwxyz", 
        [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
                                                    "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]))

        lcodes = []
        for word in words:
            temp = ''.join([d[l] for l in word])
            lcodes.append(temp)

        return len(set(lcodes))

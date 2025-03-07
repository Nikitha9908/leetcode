class Solution:
    def fullJustify(self, words, maxWidth):
        res = []  # Final result list
        line, line_length = [], 0  # Store words for current line

        i = 0
        while i < len(words):
            word = words[i]
            if line_length + len(line) + len(word) > maxWidth:
                # Distribute spaces
                for j in range(maxWidth - line_length):
                    line[j % (len(line) - 1 or 1)] += ' '  # Distribute spaces left to right
                res.append(''.join(line))
                line, line_length = [], 0  # Reset for new line
            
            line.append(word)
            line_length += len(word)
            i += 1

        # Last line (left-justified)
        res.append(' '.join(line).ljust(maxWidth))

        return res

# Example test cases
sol = Solution()
print(sol.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
print(sol.fullJustify(["What","must","be","acknowledgment","shall","be"], 16))
print(sol.fullJustify(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20))

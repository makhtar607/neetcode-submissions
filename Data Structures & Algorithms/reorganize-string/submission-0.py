from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:  # Added 'self' here
        counts = {}
        for char in s:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
        print(counts)

        max_char = ""
        max_count = 0
        
        for char, count in counts.items():
            if count >= max_count:
                max_count = count
                max_char = char
                print(max_char, max_count)

        if max_count > (len(s) + 1) // 2:
            return ""

        solution = [""]*len(s)
        index = 0

        for _ in range(max_count):
            solution[index] = max_char
            index += 2
        del counts[max_char]
        print(len(s))
        for char, count in counts.items():
            for _ in range(count):
                print(index)
                if index >= len(solution):
                    index = 1
                solution[index] = char
                index += 2    



            print(solution)

        return "".join(solution)


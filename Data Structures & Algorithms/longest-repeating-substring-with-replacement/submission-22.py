class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        most_characters = 0
        left = 0
        character_count = defaultdict(int)

        for right in range(len(s)):
            character_count[s[right]] += 1
            most_characters = max(most_characters, character_count[s[right]])

            while right - left + 1 > most_characters + k:
                character_count[s[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1)
        
        return longest
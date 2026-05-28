class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        t_char_count = defaultdict(int)
        window_char_count = defaultdict(int)

        # Count characters needed from t
        for c in t:
            t_char_count[c] += 1

        left = 0
        minimum = ""

        for right in range(len(s)):
            # Expand window by adding incoming character
            window_char_count[s[right]] += 1

            # Check if current window contains all characters of t
            while all(t_char_count[c] <= window_char_count[c] for c in t_char_count):
                current_window = s[left:right + 1]
                if not minimum or len(current_window) < len(minimum):
                    minimum = current_window

                # Shrink window from the left
                window_char_count[s[left]] -= 1
                left += 1

        return minimum
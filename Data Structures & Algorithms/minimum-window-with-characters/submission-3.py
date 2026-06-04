class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        t_char_count = defaultdict(int)
        window_char_count = defaultdict(int)

        for c in t:
            t_char_count[c] += 1

        have, need = 0, len(t_char_count)

        left = 0
        min_window = [-1, -1]
        min_length = float("infinity")

        for right in range(len(s)):
            incoming_char = s[right]
            window_char_count[incoming_char] += 1

            # Check if this character satisfies a requirement from t
            if incoming_char in t_char_count and window_char_count[incoming_char] == t_char_count[incoming_char]:
                have += 1

            # Shrink window from left while all requirements are satisfied
            while have == need:
                current_window_size = right - left + 1

                # Update minimum window if current is smaller
                if current_window_size < min_length:
                    min_window = [left, right]
                    min_length = current_window_size

                # Remove outgoing character from window
                outgoing_char = s[left]
                window_char_count[outgoing_char] -= 1

                # Check if removing this character breaks a requirement
                if outgoing_char in t_char_count and window_char_count[outgoing_char] < t_char_count[outgoing_char]:
                    have -= 1

                left += 1

        left, right = min_window
        return s[left: right + 1] if min_length != float("infinity") else ""
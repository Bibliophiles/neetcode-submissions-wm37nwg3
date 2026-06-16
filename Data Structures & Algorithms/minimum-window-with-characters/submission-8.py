class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        t_char_count = defaultdict(int)
        window_char_count = defaultdict(int)

        for char in t:
            t_char_count[char] += 1

        have, need = 0, len(t_char_count)

        min_window = [-1, -1]
        len_min_window = float("infinity") #sorry, infinity is not a small number but a very large number
        left = 0 

        for right in range(len(s)):
            incoming_char = s[right]
            window_char_count[incoming_char] += 1

            if incoming_char in t_char_count and t_char_count[incoming_char] == window_char_count[incoming_char]:
                have += 1

            while have == need:
                current_win_size = right - left + 1
                if current_win_size < len_min_window:
                    min_window = [left, right + 1]
                    len_min_window = current_win_size

                outgoing_char = s[left]
                window_char_count[outgoing_char] -= 1
                left += 1

                if outgoing_char in t_char_count and window_char_count[outgoing_char] < t_char_count[outgoing_char]:
                    have -= 1
                
                
        left, right = min_window
        return s[left : right] if len_min_window != float("infinity") else ""







from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        
        # Create frequency maps for s1 and the first window of s2
        s1_counts = Counter(s1)
        window_counts = Counter(s2[:n1])
        
        # Check the first window
        if s1_counts == window_counts:
            return True
            
        # Slide the window across s2
        for i in range(n1, n2):
            # Add the new character to the window
            window_counts[s2[i]] += 1
            # Remove the oldest character from the window
            old_char = s2[i - n1]
            window_counts[old_char] -= 1
            
            # Remove the key if count drops to 0 to keep dictionaries comparable
            if window_counts[old_char] == 0:
                del window_counts[old_char]
                
            # Compare current window with s1
            if s1_counts == window_counts:
                return True
                
        return False
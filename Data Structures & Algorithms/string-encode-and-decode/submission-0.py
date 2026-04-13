class Solution:
    def encode(self, strs: List[str]) -> str:
        output = ""
        for string in strs:
            n = len(string)
            output += f'#{n}#{string}'
        return output

    def decode(self, s: str) -> List[str]:
        output = []

        def extract_word(s, start_index):
            i = 1
            length_as_str = ''
            while s[start_index + i] != '#':
                length_as_str += s[start_index + i]
                i += 1
            length = int(length_as_str)
            # We need to move past the second # 
            start_index = start_index + i +1
            end_index   = start_index + length -1
            return start_index, end_index
        
        index = 0
        while index < len(s):
            index, end_index = extract_word(s, index)
            output.append(s[index:end_index+1])
            index = end_index+1

        return output


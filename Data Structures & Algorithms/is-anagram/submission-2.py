class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        length_t = len(t)
        length_s = len(s)

        if length_t != length_s:
            return False

        t_dict = {}
        t_set = set(t)
        for char in t_set:
            t_dict[char] = t.count(char)
        s_dict = {}
        s_set = set(s)
        for char in s_set:
            s_dict[char] = s.count(char)
        if s_dict != t_dict:
            return False
            
        return True



            

        # char_list = list(t)

        # for char in s:
        #     if char not in char_list:
        #         return False
        #     char_list.remove(char)
        # return True

        


        

        

        
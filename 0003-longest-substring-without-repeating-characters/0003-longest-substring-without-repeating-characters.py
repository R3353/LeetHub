import heapq

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #note: s contains english letters, digits, symbols, and spaces.
        #i think what i'll do is iter through s and then add each unique substring to a defaultdict of lists structure where key = substring length : value = substring. 
        #i am using a dictionary because it will be easier to store a substring with its corresponding length and compare a list of substrings' lengths and find the max.
        #edge cases: doesn't matter if two substrings have equal length because they are both the max len of substrings. therefore, i use defaultdict of lists.
        #never mind i think i will just use a heap... it doesnt matter that i store the substring. however, i must keep track of where i am in the substring.
        # ----
        #INSTEAD: i will keep a heap of substring lengths.
        #i keep track of a substring in a temporary string (stored in a for loop as i iterate through a string). as i iterate through s, i check if the temp string contains s. if not, add s to the end of the temp string. if yes, add the length of temp string to the heap of string lengths. then i move on.
        
        #update: my approach wasnt the most efficient. sliding door is more efficient.
        #it would basically do the same thing as my old approach -- just more immediate and doesn't store more than it needs to.
        #l,r sliding window vars; keep a max var. reassign if there is a greater max. ; return max

        chars = Counter() #because 
        left = right = 0 #keeping track of indices

        #setting up right window.
        res = 0 #return val
        while right < len(s): #and it's ok to account for just `right` because it's safe to assume, depending on how carefully we code this, `left` will always stay left of `right`.
            r = s[right] #create r pointer on `s` using `right` index value.
            chars[r] += 1

            while chars[r] > 1:
                l = s[left]
                chars[l] -= 1 #because we are not looking at the prev l character anymore.
                left += 1 #move l once to right

            res = max(res, right - left + 1) #max of stored result and length of window

            right += 1
        return res

    #there is a more optimal soln than this. i just dont get it. so i'll stick with this bc it's more intuitive to me as i learn the general sliding window structure / array patterns.
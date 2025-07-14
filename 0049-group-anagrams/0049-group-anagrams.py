from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #defaultdict(list) to initialize lists for each key. append words to list. 
        #key = sorted words
        dict = defaultdict(list)
        for s in strs:
            dict[tuple(sorted(s))].append(s) #turn sorted(s) into a tuple because LISTS ARENT HASHABLE.
        return list(dict.values())


        #the more efficient soln sums up the ascii value of each word and the keys are those sums. and its more efficient because we dont have to sort the words. it just adds which has a O(1) runtime.
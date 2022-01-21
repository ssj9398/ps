## 그룹 애너그램

import collections
from typing import List

def groupAnagrams(strs: List[str]):
    anagrams = collections.defaultdict(list)

    for word in strs:
        anagrams[''.join(sorted(word))].append(word)
    print(list(anagrams.values()))
    return list(anagrams.values())


groupAnagrams(["ate", "nat", "bat", "eat", "tea", "tan"])
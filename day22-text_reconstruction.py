""" Day 22. Split a string into any of its possible reconstructions. Medium

"""

from typing import List, Optional


class TextReconstructor():
    def __init__(self, word_list: List[str]):
        self.words = set(word_list)
        self.max_word_len = max(len(word) for word in self.words)
        print(f"Got a word list of size {len(self.words)} unique elements, max word lenght of {self.max_word_len}")
        self.text = None
        self.result = []  # list of strings

    def reconstruct(self, text: str) -> Optional[List[str]]:
        self.text = text
        print("Reconstructing text:", self.text)
        self.result = []  # reset the result
        self.text_len = len(text)

        found_solution = self._reconstruct_step(0, self.text_len)
        
        return self.result if found_solution else None

    def _reconstruct_step(self, start_idx: int, end_idx: int) -> bool:
        # recursive
        if start_idx == end_idx:
            return True

        for start_idx in range(start_idx, end_idx):
            for end_idx in range(start_idx + 1, end_idx + 1):
                if self.text[start_idx:end_idx] in self.words:
                    # found a word, continue from there
                    #print("Found and added to result:", self.text[start_idx:end_idx])
                    self.result.append(self.text[start_idx:end_idx])
                    # recurse deeper
                    found_solution = self._reconstruct_step(start_idx=end_idx, end_idx=self.text_len)
                    if found_solution:
                        return True
                    else:
                        self.result.pop()
    
        return False
        

# Unit tests
TEST_WORDS_1 = ['bed', 'bath', 'bedbath', 'and', 'beyond']
TEST_WORDS_2 = ['the', 'quick', 'brown', 'fox']

TEST_STR_1 = "bedbathandbeyond"
TEST_STR_2 = "thequickbrownfox"

reconstructor1 = TextReconstructor(TEST_WORDS_1)
reco1 = reconstructor1.reconstruct(TEST_STR_1)
assert reco1 is not None
print(reco1)
assert reconstructor1.reconstruct(TEST_STR_2) is None

reconstructor2 = TextReconstructor(TEST_WORDS_2)
assert reconstructor2.reconstruct(TEST_STR_1) is None
reco2 = reconstructor2.reconstruct(TEST_STR_2)
assert reco2 is not None
print(reco2)

class WordDictionary:

    def __init__(self):
        self.l = []

    def addWord(self, word: str) -> None:
        self.l.append(word)

    def search(self, word: str) -> bool:
        
        # query 
        if '.' in word:
            match = False
            
            for w in self.l:
                if len(w) != len(word):
                    continue
                else:
                    match = True
                    
                    for i in range(len(word)):
                        if word[i]=='.':
                            continue
                        elif word[i]!=w[i]:
                            match = False
                    if match:
                        return match
                
            return match
        
        elif word in self.l:
            return True
        else:
            return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
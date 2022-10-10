class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def add(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

    def remove(self, word) -> None:
        # TrieNode
        cur = self
        # list[(TrieNode, str)]]
        keys = []
        for c in word:
            keys.append((cur, c))
            cur = cur.children[c]

        for n, k in reversed(keys):
            t = n.children[k]
            if len(t.children) == 0:
                del n.children[k]
            else:
                return

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for w in words:
            root.add(w)

        ROWS, COLS = len(board), len(board[0])

        res, visit = set(), set()

        def dfs(r, c, node, word):

            if (r < 0 or c < 0 or 
                r == ROWS or c == COLS or
                (r,c) in visit or board[r][c] not in node.children):
                return 
            
            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            
            if node.isWord:
                res.add(word)
                root.remove(word)

            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r, c-1, node, word)

            visit.remove((r,c))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        
        return list(res)
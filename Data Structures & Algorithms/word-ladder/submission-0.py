class Solution:
    def preprocessing(self,wordList,beginWord):
        myDict=defaultdict(list)
        n=len(beginWord)

        for wrd in wordList:
            for i in range(n):
                key=wrd[:i]+"_"+wrd[i+1:]
                myDict[key].append(wrd)
        return myDict

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        n=len(beginWord)
        myDict=self.preprocessing(wordList,beginWord)
        seen=set()
        queue=deque([(1,beginWord),])

        while queue:
            count,wrd=queue.popleft()

            if wrd==endWord:
                return count 

            for i in range(n):
                key=wrd[:i]+"_"+wrd[i+1:]

                for adj_wrd in myDict[key]:
                    if adj_wrd not in seen:
                        seen.add(adj_wrd)
                        queue.append((count+1,adj_wrd))
                myDict[key]=[]

        return 0

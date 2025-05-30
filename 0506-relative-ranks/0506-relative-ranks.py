class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # U
        # - score: distinct, size n, score[i] is score of ith athlete,
        # - 1st place has highest score - "Gold Medal", then "Silver Medal", "Bronze Medal"
        # - 4th place and so on: their rank is their placement number (i.e., the xth place athlete's rank is "x").
        # - Return array answer[] of size n, answer[i] is the rank of the ith athlete.
        # - ex: score = [5,4,3,2,1] -> ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
        # - highest score == lowest index of rank
        # => sort in decreasing order, the index after sorted is the rank; keep the relative position before sorting

        # M1: sort array
        # P:
        # - convert score=[10,3,8] into [(10,1), (3,2), (8,3), (9,4), (4,5)], as we want to keep track 
        #   of each athlete's original position so we can assign ranks in the correct order later.
        # - sort by first key descending => sortedScore = [(10,1), (9,4), (8,3), (4,5), (3,2)]
        # - positions = [1,4,3,5,2] (2nd keys from tuples)
        #   (1st place is at position 1, 2nd place is at position 4, so on ...) 
        #   => i means rank,positions[i] is position of that rank
        # - for i,pos in enumerate(positions): output[pos] = i

        # formated_score = []
        # for i,s in enumerate(score):
        #     formated_score.append((s, i))
        # formated_score = sorted(formated_score, reverse=True) # or: formated_score.sort(reverse=True)
        # positions = [pos for (_,pos) in formated_score]
        
        # output = [0] * len(positions)
        # for i,pos in enumerate(positions): 
        #     output[pos] = str(i+1)
        # first3 = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        # for i in range(min(3, len(score))):
        #     output[output.index(str(i+1))] = first3[i]
        # return output


        #----------
        # M2: max heap (nlogn)
        # popuplate a max_heap with (score, index) tuples; then pop the heap and use that to populate the result list
        max_h = []
        for i,s in enumerate(score):
            heappush(max_h,(-s,i))
        result = [""] * len(score)
        top3_title = ["Bronze Medal","Silver Medal","Gold Medal"]
        rank_count = 3
        while max_h:
            max_score,i = heappop(max_h)
            if len(top3_title) > 0:
                title = top3_title.pop()
                result[i] = title
            else:
                rank_count += 1
                result[i] = str(rank_count)
        # print(result)
        return result
            

        




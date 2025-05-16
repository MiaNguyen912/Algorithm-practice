class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # string s is happy if: only contains 'a', 'b', and 'c'; does not contain "aaa", "bbb", or "ccc"
        # Given 3 integers a, b, and c, return one possible longest possible happy string or "".
        # A substring is a contiguous sequence of characters within a string.
        # 0 <= a, b, c <= 100, a + b + c > 0
         
        # Plan: try to use the most frequent letter as much as possible
        # => let output = ""
        #   if c is most frequent: add "cc" to output, c-=2
        #   then, if most frequent is a: add "aa", a -= 2
        #   if the most frequent letter is same as output[-1]: add the second frequent one 1 time (ex: "a")
        #   but if there's no second frequent one, return output
        # O(nlogn)

        # max_h = []
        # if a>0:
        #     heappush(max_h, (-a, "a"))
        # if b>0:
        #     heappush(max_h, (-b, "b"))
        # if c>0:
        #     heappush(max_h, (-c, "c"))
        # output = ""
        # last_char = ""
        # while True:
        #     if max_h:
        #         most_freq, letter = heappop(max_h)
        #     if letter != last_char:
        #         if abs(most_freq) == 1: # add 1 letter to output; no need to push back to heap
        #             output += letter
        #         else:
        #             output += letter*2
        #         if abs(most_freq) > 2: # else: we used it up -> no need to push back to heap
        #             heappush(max_h, (most_freq+2, letter))
        #         last_char = letter
        #     else: 
        #         if not max_h:
        #             return output
        #         second_freq, second_letter = heappop(max_h)
        #         if second_freq == 0:
        #             return output
        #         output += second_letter
        #         last_char = second_letter
        #         if abs(second_freq)>1: # else: we used it up -> no need to push back to heap
        #             heappush(max_h, (second_freq+1, second_letter))
        #         heappush(max_h, (most_freq, letter)) # add back the most frequent letter

        # M2: add 1 most frequence letter at each iteration, use 2 vars to keep track of the last 2 added one to make sure no "aaa","bbb","ccc" is added -> this method is similar to the above one but we'd need to handle less edge cases
        # O(n)
        output = ""
        max_h = []
        if a>0: # populate the max heap and try to pre-add some letter to ouput 
            heappush(max_h, [-a, 'a'])
        if b>0:
            heappush(max_h, [-b, 'b'])
        if c>0:
            heappush(max_h, [-c, 'c'])
        if len(max_h) == 0: 
            return "" # no happy string
        prevprev, prev = '', '' # the last 2 chars
        while max_h:
            most_frequent = heappop(max_h)
            if most_frequent[1] == prev == prevprev:
                if not max_h: # if nothing else to pop -> return
                    return output
                second_frequent = heappop(max_h)
                output += second_frequent[1]
                heappush(max_h, most_frequent) # add back most_frequent
                if -second_frequent[0]-1 > 0:
                    heappush(max_h, [-(-second_frequent[0]-1), second_frequent[1]]) # add back second_frequent
            else:
                output += most_frequent[1]
                if -most_frequent[0]-1 > 0:
                    heappush(max_h, [-(-most_frequent[0]-1), most_frequent[1]]) # add back most_frequent
            prevprev,prev = prev,output[-1]
        return output





        
            
        
        
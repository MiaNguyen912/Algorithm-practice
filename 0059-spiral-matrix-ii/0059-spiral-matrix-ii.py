class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0]*n for _ in range(n)]
        dir = [[0,1], [1,0], [0,-1], [-1,0]]
        dir_i = 0
        top,right,bot,left = 0,n-1,n-1,0
        i,j = 0,0
        curr_val = 1
        
        while curr_val <= n**2:
            # write curr_val to result
            result[i][j] = curr_val 
            curr_val += 1

            # update position
            dx, dy = dir[dir_i]
            ni, nj = i + dx, j + dy

            if not(top<=ni<=bot and left<=nj<=right): # if positon is not valid, turn to diff direction
                dir_i = (dir_i + 1) % 4 # update direction
                if dir_i == 0: # go to the right -> cut left wall
                    left += 1
                elif dir_i == 1:
                    top += 1
                elif dir_i == 2:
                    right -= 1
                else:
                    bot -=1

                # recompute the new step after turning
                dx, dy = dir[dir_i]
                ni, nj = i + dx, j + dy

            # update position
            i, j = ni, nj
        
        return result



            
                
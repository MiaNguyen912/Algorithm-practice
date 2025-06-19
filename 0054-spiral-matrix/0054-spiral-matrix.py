class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dir = [[0,1],[1,0],[0,-1],[-1,0]]
        d_index = 0
        i,j = 0,0
        output = [matrix[0][0]]
        top,right,bot,left = 0, len(matrix[0]), len(matrix), 0
        total_items = right*bot


        while len(output)<total_items:
            # print(output)
            dx,dy = dir[d_index]
            ni,nj = i+dx, j+dy
            if top <= ni < bot and left <= nj < right:
                output.append(matrix[ni][nj])
                i,j = ni,nj
            else: # cut wall
                d_index = (d_index + 1) % 4
                if d_index == 0: # new dir is to the right -> old dir is upward -> cut left
                    left += 1
                elif d_index == 1:
                    top += 1
                elif d_index == 2:
                    right -= 1
                else:
                    bot -=1
        # print(output)
        return output


        
        # print(output)
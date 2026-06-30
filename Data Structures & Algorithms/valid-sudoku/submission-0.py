class Solution:
    def fillDigit(self, digit):
        pass

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        box = [0] * 9
        column_box = [0] * 9
        sub_box_1 = [0] * 9
        sub_box_2 = [0] * 9
        sub_box_3 = [0] * 9
        
        for i in range(len(board)):
            for j in range(len(board)):     
                
                # check row wise
                if board[i][j] != '.':
                    if box[int(board[i][j]) - 1] >= 1:
                        return False

                    box[int(board[i][j]) - 1] += 1

                    # check subboxes
                    if j + 1 <= 3:
                        if sub_box_1[int(board[i][j]) - 1] >= 1:
                            return False
                
                        sub_box_1[int(board[i][j]) - 1] += 1
                
                    if 4 <= j + 1 <= 6:
                        if sub_box_2[int(board[i][j]) - 1] >= 1:
                            return False
                
                        sub_box_2[int(board[i][j]) - 1] += 1
                
                    if j + 1 >= 7:
                        if sub_box_3[int(board[i][j]) - 1] >= 1:
                            return False
                
                        sub_box_3[int(board[i][j]) - 1] += 1
                
                # check column wise
                if board[j][i] != '.':
                    if column_box[int(board[j][i]) - 1] >= 1:
                        return False

                    column_box[int(board[j][i]) - 1] += 1
                
            if (i + 1) % 3 == 0:
                sub_box_1 = [0] * 9
                sub_box_2 = [0] * 9
                sub_box_3 = [0] * 9
            
            box = [0] * 9
            column_box = [0] * 9

        return True
        
class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        //row
        for(int row = 0; row < 9; row++){
            unordered_set<int>seen;
            for(int i = 0; i < 9; i++){
                if(board[row][i] == '.') continue;
                if(seen.count(board[row][i])) return false;
                seen.insert(board[row][i]);
            }
        }
        //column
        for(int col = 0; col < 9; col++){
            unordered_set<int>seen;
            for(int i = 0; i < 9; i++){
                if(board[i][col] == '.') continue;
                if(seen.count(board[i][col])) return false;
                seen.insert(board[i][col]);
            }
        }
        //square
        for(int square = 0; square < 9; square++){
            unordered_set<int>seen;
            for(int i = 0; i < 3; i++){
                for(int j = 0; j < 3; j++){
                    int row = (square / 3) * 3 + i;
                    int col = (square % 3) * 3 + j;
                    if(board[row][col] == '.') continue;
                    if(seen.count(board[row][col])) return false;
                    seen.insert(board[row][col]);
                }
            }
        }
        return true;
    }
};

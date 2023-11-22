
def islands_count(M, N, mtrx) -> int:
    if M==0 and N==0:
        return 0
    matrix = mtrx.copy()
    islands = 0

    for i in range(M):
        for j in range(N):
            if matrix [i][j] == "1":
                _dfs(matrix, i, j, M, N)
                islands +=1
    return islands


def _dfs(matrix, i, j, M, N):
    stack = [(i, j)]
    while len(stack)>0:
        i, j = stack[0]
        if i<0 or j<0 or i>=M or j>=N or matrix[i][j] != "1" or matrix[i][j] == '*' :
            stack = stack[1:]
            continue
        matrix[i][j] = '*'
        stack.extend([(i+1, j), (i-1, j), (i, j+1), (i, j-1)])
        stack = stack[1:]



if __name__ == "__main__":
    
    test_case1 = [["1","1","0","0","1"],
                  ["1","1","0","1","0"],
                  ["0","0","1","0","0"],
                  ["0","1","0","1","1"]]
    
    test_case2 = [["0","1","0"],
                  ["0","0","0"],
                  ["0","1","1"]]
        
    test_case3 = [["0","0","0","1"],
                  ["0","0","1","0"],
                  ["0","1","0","0"]]
    
    test_case4 = [["0","0","0","1"],
                  ["0","0","1","1"],
                  ["0","1","0","1"]]
    
    
    res1 = islands_count(len(test_case1), len(test_case1[0]), test_case1)
    print(f"Expected 6 Result {res1}")
    
    res2 = islands_count(len(test_case2), len(test_case2[0]), test_case2)
    print(f"Expected 2 Result {res2}")
    
    res3 = islands_count(len(test_case3), len(test_case3[0]), test_case3)
    print(f"Expected 3 Result {res3}")
    
    res4 = islands_count(len(test_case4), len(test_case4[0]), test_case4)
    print(f"Expected 2 Result {res4}")
    
    
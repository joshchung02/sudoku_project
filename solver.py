count = 0

def read_sudoku(file_name):
    """
    Reads the file (.txt) which should be a sudoku with each row being seperated by
    a new line and each column being seperated by spaces.
    Takes each number and puts it in a 9x9 matrix of ints.
    Returns the matrix.
    """
    sudoku = []
    f = open(file_name)
    for line in f:
        str_row = line.split()   # Splits by spaces
        row = []
        for num in str_row:
            row.append(int(num))
        sudoku.append(row)
    f.close()
    return sudoku

def print_sudoku(sudoku):
    """
    Prints the sudoku nicely.
    Returns None.
    """
    board = "--+-+-+-+-+-+-+-+--\n"
    for i in range(len(sudoku)):
        board += "|"
        for j in range(len(sudoku)):
            board += str(sudoku[i][j])
            board += "|"
        board += "\n"
        board += "--+-+-+-+-+-+-+-+--\n"
    print(board)

def solve_sudoku(sudoku):
    """
    Uses RECURSION to solve the sudoku.
    Base case: Sudoku is solved (#1) or impossible (#2), return True or False respectively.
    Recursive case: Find blank space, try a number, check if valid. If valid, set
    space to that number and recurse. If no values are valid (1-9), set to 0.

    Ex:
                        Starting w/ 1 = invalid         2,5 is valid            jk 2,5 = invalid
    000 100 110 120 130 ... 190 ---> 100 ---> 200 210 220 ... 250 --> 251 252 ... 259 --> 250 --> 260 ...

    """
    global count
    count += 1
    row, col = find_blank(sudoku)

    # Base case #1:
    if row == -1 and col == -1:
        return True
    
    # Recursive case:
    for num in range(1, 10):
        if is_valid(sudoku, row, col, num):
            sudoku[row][col] = num
            if solve_sudoku(sudoku):
                return True
    sudoku[row][col] = 0

    # Base case #2:
    return False

def find_blank(sudoku):
    """
    Finds the next blank (element = 0) in the sudoku.
    Returns row, col indices if available
    Returns -1, -1 if there are no blanks left
    """
    for i in range(9):     # Note: row-major order
        for j in range(9):
            if sudoku[i][j] == 0:
                return i, j
    return -1, -1

def is_valid(sudoku, row, col, num):
    """
    Checks the row, column, and box to see if the given num is valid.
    Returns True if valid, False if invalid
    """
    #Row:
    for elem in sudoku[row]:
        if num == elem:
            return False
    
    #Col:
    for r in sudoku:
        if num == r[col]:
            return False

    #Box:
    row_min = (row // 3) * 3
    col_min = (col // 3) * 3
    for i in range(row_min, row_min + 3):
        for j in range(col_min, col_min + 3):
            if num == sudoku[i][j]:
                return False

    #Valid!
    return True

def main():
    print("Difficulties:")
    print("1. Easy  2. Medium  3. Hard  4. Very Hard  5. Impossible")
    sudoku_num = input("Choose a number: ")
    print()

    file_name = "sudoku" + sudoku_num + ".txt"
    sudoku = read_sudoku(file_name)

    print("Unsolved:")
    print_sudoku(sudoku)

    if solve_sudoku(sudoku):
        print("Solved:")
        print_sudoku(sudoku)
        global count
        print("Recursions: "+ str(count))
        print()
    else:
        print("Unsolvable")

if __name__=="__main__":
    main()

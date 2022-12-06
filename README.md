# Sudoku Project
- Built in May 23, 2021

## Algorithm Involved
- Recursive backtracking algorithm
- In current empty space, try the next valid number, then move on to next empty space with a recursive call. If we reach an empty space with no valid numbers left, effectively "undo" by returning from current recursive call.

## Sample run
Run the following command in terminal:

```
python3 solver.py
```

You will be prompted to select a difficulty. Choose a number and hit enter:

```
Difficulties:
1. Easy  2. Medium  3. Hard  4. Very Hard  5. Impossible
Choose a number: 1
```

Easy was chosen for this run. The output is as follows:
```
Unsolved:
--+-+-+-+-+-+-+-+--
|0|0|3|0|4|2|0|9|0|
--+-+-+-+-+-+-+-+--
|0|9|0|0|6|0|5|0|0|
--+-+-+-+-+-+-+-+--
|5|0|0|0|0|0|0|1|0|
--+-+-+-+-+-+-+-+--
|0|0|1|7|0|0|2|8|5|
--+-+-+-+-+-+-+-+--
|0|0|8|0|0|0|1|0|0|
--+-+-+-+-+-+-+-+--
|3|2|9|0|0|8|7|0|0|
--+-+-+-+-+-+-+-+--
|0|3|0|0|0|0|0|0|1|
--+-+-+-+-+-+-+-+--
|0|0|5|0|9|0|0|2|0|
--+-+-+-+-+-+-+-+--
|0|8|0|2|1|0|6|0|0|
--+-+-+-+-+-+-+-+--

Solved:
--+-+-+-+-+-+-+-+--
|6|1|3|5|4|2|8|9|7|
--+-+-+-+-+-+-+-+--
|8|9|7|3|6|1|5|4|2|
--+-+-+-+-+-+-+-+--
|5|4|2|9|8|7|3|1|6|
--+-+-+-+-+-+-+-+--
|4|6|1|7|3|9|2|8|5|
--+-+-+-+-+-+-+-+--
|7|5|8|4|2|6|1|3|9|
--+-+-+-+-+-+-+-+--
|3|2|9|1|5|8|7|6|4|
--+-+-+-+-+-+-+-+--
|2|3|6|8|7|4|9|5|1|
--+-+-+-+-+-+-+-+--
|1|7|5|6|9|3|4|2|8|
--+-+-+-+-+-+-+-+--
|9|8|4|2|1|5|6|7|3|
--+-+-+-+-+-+-+-+--

Recursions: 1362
```

## Inputting your own sudoku
- This has not been implemented very well, but it is possible if you would like to try.

### Steps:
1. Edit one of the txt files to contain your sudoku.
2. Each row is separated by a new line, and column by a space.
3. Valid numbers are 0-9, where 0 is a blank space.
4. Run the program with your file. The option number corresponds to the file name's number.

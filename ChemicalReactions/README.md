A scientist John Doe was given a cell and a list of chemicals that are present in the environment at the beginning.
He already knows what reactions could happen in the cell.
You should help him to understand which chemicals could appear in the cell.

Input Format

The first line contains initial chemicals separated by spaces.
There is always at least one initial chemical.
Each chemical is represented by a random positive integer that fits in 4-byte integer type.
Each of the following lines describes a reaction, one per line.
Each reaction is presented as two lists of integers separated by '->': the list of chemicals, separated by '+',
that is needed to perform a reaction and the list of chemicals, separated by '+',
that are produced as a result of the reaction. Each chemical could be present in each reaction maximum 2 times:
one time at the left part and the other time at the right part (for example, a catalyst could appear in both parts).

Output Format

The sole line of the output should contain the unordered list of all chemicals that could appear in the cell
at any moment of time.

Sample Input 1

4
4+6->1
2->3+5
4->6
6+4->5

Sample Output 1:

1 4 5 6
# This is a recursive solution to the Towers of Hanoi problem.
# The Towers of Hanoi problem is a classic problem in computer science that involves moving a stack of disks from one peg to another peg, using a third peg as an auxiliary.
# The problem is defined as follows:
# - There are three pegs, A, B, and C.
# - There are n disks of different sizes, stacked in decreasing order of size on peg A.
# - The goal is to move all the disks from peg A to peg C, using peg B as an auxiliary, such that no disk is ever placed on top of a smaller disk.

# How to deduce a recursive solution ?
# Check if the problem for n can be solved if n-1 is solved
# Find the base case

def towers_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    towers_of_hanoi(n-1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    towers_of_hanoi(n-1, auxiliary, target, source)

if __name__ == "__main__":
    print(f"For n=3:")
    towers_of_hanoi(3, 'A', 'C', 'B') # Move disk 1 from A to C
                                      # Move disk 2 from A to B
                                      # Move disk 1 from C to B
                                      # Move disk 3 from A to C
                                      # Move disk 1 from B to A
                                      # Move disk 2 from B to C
                                      # Move disk 1 from A to C
    print(f"For n=4:")
    towers_of_hanoi(4, 'A', 'C', 'B') # Move disk 1 from A to B
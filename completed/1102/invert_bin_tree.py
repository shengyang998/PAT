"""
1102. Invert a Binary Tree (25)

时间限制
400 ms
内存限制
65536 kB
代码长度限制
16000 B
判题程序
Standard
作者
CHEN, Yue
The following is from Max Howell @twitter:
Google: 90% of our engineers use the software you wrote (Homebrew), but you can't invert a binary tree on a whiteboard so fuck off.
Now it's your turn to prove that YOU CAN invert a binary tree!
Input Specification:
Each input file contains one test case. For each case, the first line gives a positive integer N (<=10) which is the total number of nodes in the tree -- and hence the nodes are numbered from 0 to N-1. Then N lines follow, each corresponds to a node from 0 to N-1, and gives the indices of the left and right children of the node. If the child does not exist, a "-" will be put at the position. Any pair of children are separated by a space.
Output Specification:
For each test case, print in the first line the level-order, and then in the second line the in-order traversal sequences of the inverted tree. There must be exactly one space between any adjacent numbers, and no extra space at the end of the line.

Sample Input:
8
1 -
- -
0 -
2 7
- -
- -
5 -
4 6

Sample Output:
3 7 2 6 4 0 5 1
6 5 7 4 3 2 0 1

"""

from collections import deque

LEFT = 1
RIGHT = 0

DEBUG = False
def debug_print(x, end='\n'):
    if DEBUG is True:
        print(x, end=end)


class Node:
    idx = None
    flag = False
    left = None
    right = None
    def __init__(self, idx, left, right):
        self.idx = idx
        self.left = left
        self.right = right

    def setVisited(self, x:bool=True):
        self.flag = x

    def isVisited(self):
        return self.flag


def in_order(tree:list, tree_top):
    stack = [tree[tree_top]]
    p = tree[tree_top]
    res = ""
    while len(stack) != 0:
        if p.left is not None and p is not None and p.isVisited() is False:
            p.setVisited()
            p = tree[p.left]
            debug_print("push: {0}".format(p.idx))
            stack.append(p)
        else:
            debug_print("Stack: {0}".format([x.idx for x in stack]), end=' ')
            debug_print("at: {0}".format(stack[-1].idx))
            p = stack.pop()
            res = "{0} {1}".format(res, p.idx)
            if p.right is not None:
                p.setVisited()
                stack.append(tree[p.right])
                p = tree[p.right]
    return res.strip()


def layer_order(tree:list, tree_top):
    queue = deque([tree[tree_top]])
    p = tree[tree_top]
    res = ""
    while len(queue) != 0:
        p = queue.popleft()
        if p.left is not None:
            queue.append(tree[p.left])
        if p.right is not None:
            queue.append(tree[p.right])
        res = "{0} {1}".format(res, p.idx)
    return res.strip()


if __name__ == "__main__":
    s = int(input().strip())
    tree = [None] * s
    list_for_tree_top = [0] * s
    for i in range(s):
        t = [int(x) if x != '-' else None for x in input().strip().split(' ')]
        tree[i] = Node(i, t[LEFT], t[RIGHT])
        if t[LEFT] != None:
            list_for_tree_top[t[LEFT]] = 1
        if t[RIGHT] != None:
            list_for_tree_top[t[RIGHT]] = 1
    tree_top = list_for_tree_top.index(0)
    debug_print("Top: {0}".format(tree_top))
    debug_print("Tree: {0}".format([[p.idx, p.left, p.right] for p in tree]))
    res_lay_order = layer_order(tree, tree_top)
    res_in_order = in_order(tree, tree_top)
    print(res_lay_order)
    print(res_in_order)


class Node:
    def __init__(self, d):
        self.val = d
        self.left = None
        self.right = None
class Solution:
    def maxSumBST(self, root ) :
        
#class Solution:
 #   def maxSumBST(self, root: TreeNode) -> int:
        res = 0
        first_root = root
        def traverse(root):
            '''return status_of_bst, size_of_bst, left_bound, right_bound'''
            nonlocal res
            if not root: return 1, 0, None, None # this subtree is empty
            
            ls, l, ll, lr = traverse(root.left)
            rs, r, rl, rr = traverse(root.right)
            #print( ls, l, ll, lr,   '                ',  rs, r, rl, rr)
            if ((ls == 2 and lr < root.val) or ls == 1) and ((rs == 2 and rl > root.val) or rs == 1): ##.  lr  <.  root.val  < rl
		        # this subtree is a BST
                size = root.val + l + r
                res = max(res, size)
                #print(2, size, (ll if ll is not None else root.val), (rr if rr is not None else root.val))
                if root == first_root and res != 0:
                    print(    (ll if ll is not None else root.val), (rr if rr is not None else root.val) )
                return 2, size, (ll if ll is not None else root.val), (rr if rr is not None else root.val)
            return 0, None, None, None # this subtree is not a BST
    
        traverse(root)
        return res  
# Initialize and allocate memory for tree nodes
_1_1 = Node(1)
_2_1 = Node(2)
_3_1 = Node(3)
_4_1 = Node(4)
_5_1 = Node(5)
_6_1 = Node(6)
_7_1 = Node(7)

_4_1.left = _2_1
_4_1.right = _6_1

_2_1.left = _1_1
_2_1.right = _3_1

_6_1.left = _5_1
_6_1.right = _7_1

Obj = Solution()
Obj. maxSumBST( _4_1 )
print()

_1_2 = Node(1)
_2_2 = Node(2)
_3_2 = Node(3)
_4_2 = Node(4)
_5_2 = Node(5)
_6_2 = Node(6)
_7_2 = Node(7)

_4_2.left = _2_2
_4_2.right = _6_2

#_2_2.left = _1_2
_2_2.right = _3_2

_6_2.left = _5_2
_6_2.right = _7_2


Obj = Solution()
Obj. maxSumBST( _4_2 )
print()


_1_3 = Node(1)
_2_3 = Node(2)
_3_3 = Node(3)
_4_3 = Node(4)
_5_3 = Node(5)
_6_3 = Node(6)
_7_3 = Node(7)

_4_3.left = _2_3
_4_3.right = _6_3

_2_3.left = _1_3
#_2_3.right = _3_3

_6_3.left = _5_3
_6_3.right = _7_3

Obj = Solution()
Obj. maxSumBST( _4_3 )
print()


_1_4 = Node(1)
_2_4 = Node(2)
_3_4 = Node(3)
_4_4 = Node(4)
_5_4 = Node(5)
_6_4 = Node(6)
_7_4 = Node(7)

_4_4.left = _2_4
_4_4.right = _6_4

_2_4.left = _1_4
_2_4.right = _3_4

#_6_4.left = _5_4
_6_4.right = _7_4

Obj = Solution()
Obj. maxSumBST( _4_4 )
print()


_1_5 = Node(1)
_2_5 = Node(2)
_3_5 = Node(3)
_4_5 = Node(4)
_5_5 = Node(5)
_6_5 = Node(6)
_7_5 = Node(7)

_4_5.left = _2_5
_4_5.right = _6_5

_2_5.left = _1_5
_2_5.right = _3_5

_6_5.left = _5_5
#_6_5.right = _7_5

print("#############")
Obj = Solution()
Obj. maxSumBST( _4_5 )
print()

_1_6 = Node(1)
_2_6 = Node(2)
_3_6 = Node(3)
_4_6 = Node(4)
_5_6 = Node(5)
_6_6 = Node(6)
_7_6 = Node(7)

_4_6.left = _2_6
_4_6.right = _6_6

#_2_6.left = _1_6
#_2_6.right = _3_6

_6_6.left = _5_6
_6_6.right = _7_6

print("#############")
Obj = Solution()
Obj. maxSumBST( _4_6 )
print()

_1_7 = Node(1)
_2_7 = Node(2)
_3_7 = Node(3)
_4_7 = Node(4)
_5_7 = Node(5)
_6_7 = Node(6)
_7_7 = Node(7)

_4_7.left = _2_7
_4_7.right = _6_7

#_2_7.left = _1_7
_2_7.right = _3_7

#_6_7.left = _5_7
_6_7.right = _7_7

Obj = Solution()
Obj. maxSumBST( _4_7 )
print()

_1_8 = Node(1)
_2_8 = Node(2)
_3_8 = Node(3)
_4_8 = Node(4)
_5_8 = Node(5)
_6_8 = Node(6)
_7_8 = Node(7)


_4_8.left = _2_8
_4_8.right = _6_8

#_2_8.left = _1_8
_2_8.right = _3_8

_6_8.left = _5_8
#_6_8.right = _7_8

Obj = Solution()
Obj. maxSumBST( _4_8 )
print()


_1_9 = Node(1)
_2_9 = Node(2)
_3_9 = Node(3)
_4_9 = Node(4)
_5_9 = Node(5)
_6_9 = Node(6)
_7_9 = Node(7)

_4_9.left = _2_9
_4_9.right = _6_9

_2_9.left = _1_9
#_2_9.right = _3_9

#_6_9.left = _5_9
_6_9.right = _7_9

print("#############")

Obj = Solution()
Obj. maxSumBST( _4_9 )
print()

_1_10 = Node(1)
_2_10 = Node(2)
_3_10 = Node(3)
_4_10 = Node(4)
_5_10 = Node(5)
_6_10 = Node(6)
_7_10 = Node(7)

_4_10.left = _2_10
_4_10.right = _6_10

_2_10.left = _1_10
#_2_10.right = _3_10

_6_10.left = _5_10
#_6_10.right = _7_10

Obj = Solution()
Obj. maxSumBST( _4_10 )
print()


_1_11 = Node(1)
_2_11 = Node(2)
_3_11 = Node(3)
_4_11 = Node(4)
_5_11 = Node(5)
_6_11 = Node(6)
_7_11 = Node(7)

_4_11.left = _2_11
_4_11.right = _6_11

_2_11.left = _1_11
_2_11.right = _3_11

#_6_11.left = _5_11
#_6_11.right = _7_11
print("#############")

Obj = Solution()
Obj. maxSumBST( _4_11 )
print()

_1_12 = Node(1)
_2_12 = Node(2)
_3_12 = Node(3)
_4_12 = Node(4)
_5_12 = Node(5)
_6_12 = Node(6)
_7_12 = Node(7)


_4_12.left = _2_12
_4_12.right = _6_12

#_2_12.left = _1_12
#_2_12.right = _3_12

#_6_12.left = _5_12
_6_12.right = _7_12

print("#############")

Obj = Solution()
Obj. maxSumBST( _4_12 )
print()

_1_13 = Node(1)
_2_13 = Node(2)
_3_13 = Node(3)
_4_13 = Node(4)
_5_13 = Node(5)
_6_13 = Node(6)
_7_13 = Node(7)


_4_13.left = _2_13
_4_13.right = _6_13

#_2_13.left = _1_13
#_2_13.right = _3_13

_6_13.left = _5_13
#_6_13.right = _7_13

Obj = Solution()
Obj. maxSumBST( _4_13 )
print()


_1_14 = Node(1)
_2_14 = Node(2)
_3_14 = Node(3)
_4_14 = Node(4)
_5_14 = Node(5)
_6_14 = Node(6)
_7_14 = Node(7)


_4_14.left = _2_14
_4_14.right = _6_14

#_2_14.left = _1_14
_2_14.right = _3_14

#_6_14.left = _5_14
#_6_14.right = _7_14

Obj = Solution()
Obj. maxSumBST( _4_14 )
print()

_1_15 = Node(1)
_2_15 = Node(2)
_3_15 = Node(3)
_4_15 = Node(4)
_5_15 = Node(5)
_6_15 = Node(6)
_7_15 = Node(7)

_4_15.left = _2_15
_4_15.right = _6_15

_2_15.left = _1_15
#_2_15.right = _3_15

#_6_15.left = _5_15
#_6_15.right = _7_15

Obj = Solution()
Obj. maxSumBST( _4_15 )
print()

_1_16 = Node(1)
_2_16 = Node(2)
_3_16 = Node(3)
_4_16 = Node(4)
_5_16 = Node(5)
_6_16 = Node(6)
_7_16 = Node(7)


_4_16.left = _2_16
_4_16.right = _6_16

#_2_16.left = _1_16
#_2_16.right = _3_16

#_6_16.left = _5_16
#_6_16.right = _7_16

print("#############")
Obj = Solution()
Obj. maxSumBST( _4_16 )
print()





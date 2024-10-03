import unittest
from collections import deque

import assignment04
from assignment04 import SingleSidedNode
from assignment04 import DoubleSidedNode
from assignment04 import SinglyLinkedList
from assignment04 import DoublyLinkedList
from assignment04 import Queue
from assignment04 import Dictionary
from assignment04 import ReverseDoublyLinkedList
from assignment04 import RotateLinkedList
from assignment04 import MergeLinkedLists
from assignment04 import BinaryNode
from assignment04 import BinarySearchTree

class Test_TestAssignment04(unittest.TestCase):


    def testLinkedList(self):

        node = SingleSidedNode(0)
        self.assertEqual(node.data, 0)

        list = SinglyLinkedList(0)
        node = list.read_node(0)
        self.assertEqual(node.data, 0)

        list = SinglyLinkedList(0)
        for i in range(1,10):
            list.insert(i,i)

        for i in range(10):
            node = list.read_node(i)
            self.assertEqual(node.data, i)

        count = list.count
        self.assertEqual(count, 10)

        value = list.read_data(9)
        self.assertEqual(value,9)

        list.delete(0)

        count = list.count
        self.assertEqual(count, 9)

        value = list.read_data(0)
        self.assertEqual(value,1)

        list.insert(0,0)

        count = list.count
        self.assertEqual(count, 10)

        value = list.read_data(0)
        self.assertEqual(value,0)

        list.update(0,10)

        value = list.read_data(0)
        self.assertEqual(value,10)


    def testDoublyLinkedList(self):

        list = DoublyLinkedList(0)

        for val in range(0,10):
            list.append(val)

        count = list.count
        self.assertEqual(count, 10)

        value = list.read_data(9)
        self.assertEqual(value,9)

        list.delete(0)

        count = list.count
        self.assertEqual(count, 9)

        value = list.read_data(0)
        self.assertEqual(value,1)

        list.insert(0,0)

        count = list.count
        self.assertEqual(count, 10)

        value = list.read_data(0)
        self.assertEqual(value,0)

        list.update(0,10)

        count = list.count
        self.assertEqual(count, 10)

        value = list.read_data(0)
        self.assertEqual(value,10)


    def testQueue(self):

        queue = Queue()

        queue.Enqueue(1)

        value = queue.Read()
        print('value=' + str(value))
        self.assertEqual(value,1)

        queue.Enqueue(2)

        value = queue.Read()
        self.assertEqual(value,1)

        value = queue.Dequeue()
        self.assertEqual(value,1)

        value = queue.Read()
        self.assertEqual(value,2)
        
        value = queue.Dequeue()
        self.assertEqual(value,2)

        value = queue.Read()
        self.assertEqual(value,None)


    def testDictionary(self):

        dictionary = Dictionary()

        dictionary.Add("Sammy","dolphin")

        value = dictionary.Read("Sammy")
        self.assertEqual(value,"dolphin")

        dictionary.Update("Sammy","porpoise")

        value = dictionary.Read("Sammy")
        self.assertEqual(value,"porpoise")

        value = dictionary.Delete("Sammy")

        value = dictionary.Read("Sammy")
        self.assertEqual(value,None)


    def testReverseDoublyLinkedList(self):

        list = DoublyLinkedList(10)
        list.append(20)
        list.append(30)
        list.append(40)
        list.append(50)

        list.print()

        ReverseDoublyLinkedList(self,list)

        list.print()


    def testRotateLinkedList(self):

        # 10 20 30 40 50
        # rotate 3 (right)
        # preceding = 20 => index = list.count - rotate - 1 = 5 - 3 - 1 = 1 = 20
        # 30 40 50 10 20
        # rotate -3 (left)
        # preceding = 50 => index = rotate - 1 = 3 - 1 = 2
        # 10 20 30 40 50

        list = SinglyLinkedList(10)
        list.append(20)
        list.append(30)
        list.append(40)
        list.append(50)

        list.print()

        self.assertEqual(list.first_node.data,10)

        RotateLinkedList(self, list, 3)

        list.print()

        self.assertEqual(list.first_node.data,30)

        RotateLinkedList(self, list, -3)

        list.print()

        self.assertEqual(list.first_node.data,10)


    if __name__ == '__main__':
        unittest.main()

    # import unittest
    # class Test_TestWhatever(unittest.TestCase):

    #     def test_whatever(self):
    #         self.assertEqual(4, 4)

    # if __name__ == '__main__':
    #     unittest.main()



    def testMergeLinkedLists(self):

        #  [2, 10, 5, 3, 4] and [4, 7, 8, 3, 11] has a union of [2, 10, 3, 4, 5, 7, 8, 11]

        list1 = SinglyLinkedList(2)
        list1.append(10)
        list1.append(5)
        list1.append(3)
        list1.append(4)

        print()
        print("list1",end=" ")
        list1.print()

        list2 = SinglyLinkedList(4)
        list2.append(7)
        list2.append(8)
        list2.append(3)
        list2.append(11)

        print("list2",end=" ")
        list2.print()

        node = MergeLinkedLists(self,list1,list2)

        print("merged",end=" ")
        list1.print()

        #  [2, 10, 5, 3, 4] and [4, 7, 8, 3, 11] has a union of [2, 10, 3, 4, 5, 7, 8, 11]

        self.assertEqual(list1.read_data(0),2)
        self.assertEqual(list1.read_data(1),10)
        self.assertEqual(list1.read_data(2),5)
        self.assertEqual(list1.read_data(3),3)
        self.assertEqual(list1.read_data(4),4)
        self.assertEqual(list1.read_data(5),7)
        self.assertEqual(list1.read_data(6),8)
        self.assertEqual(list1.read_data(7),11)

         

    def testBinarySearchTree(self):

        #             100
        #     50              150
        # 25      75      125     175    
        #                       160

        head = BinaryNode(100) 
        left = BinaryNode(50) 
        right = BinaryNode(150) 
        leftleft = BinaryNode(25) 
        leftright = BinaryNode(75) 
        rightleft = BinaryNode(125) 
        rightright = BinaryNode(175) 

        head.left = left
        head.right = right
        left.left = leftleft
        left.right = leftright
        right.left  = rightleft
        right.right = rightright

        tree = BinarySearchTree(head)

        print('tree.node.data=' + str(tree.node.data))

        print('tree in order traversal')
        tree.PrintInOrderTraversal()
        print()
        
        print('tree.MinValue()=' + str(tree.MinValue()))
        print('tree.MaxValue()=' + str(tree.MaxValue()))
        print('tree.Sum()=' + str(tree.Sum()))
        print('tree.Height()=' + str(tree.Height()))
        print('tree.IsValid()=' + str(tree.IsValid()))
        print('tree.Search(175)=' + str(tree.Search(175)))
        print('tree.Search(200)=' + str(tree.Search(200)))
        print('tree.Insert(160)=' + str(tree.Insert(160)))
        print('tree.IsValid()=' + str(tree.IsValid()))

        print('tree in order traversal')
        tree.PrintInOrderTraversal()
        print()
        
        print('tree.Height()=' + str(tree.Height()))
        print('tree.Delete(160)=' + str(tree.Delete(160)))
        print('tree.IsValid()=' + str(tree.IsValid()))
        
        print('tree in order traversal')
        tree.PrintInOrderTraversal()
        print()
        
        print('tree.Height()=' + str(tree.Height()))

        self.assertEqual(tree.MinValue(), 25)
        self.assertEqual(tree.MaxValue(), 175)
        self.assertEqual(tree.Sum(), 700)
        self.assertEqual(tree.Height(), 2)

        print('tree in order traversal')
        tree.PrintInOrderTraversal()
        print()

        self.assertEqual(tree.IsValid(), True)
        
        print('tree in order traversal')
        tree.PrintInOrderTraversal()
        print()
        
        self.assertEqual(tree.Search(175), True)
        self.assertEqual(tree.Search(200), False)
        self.assertEqual(tree.Insert(160), True)
        self.assertEqual(tree.Search(160), True)


        #             100
        #     50              150
        # 25      75      125     175    
        #                       160
        #                     165

        head = BinaryNode(100) 
        left = BinaryNode(50) 
        right = BinaryNode(150) 
        leftleft = BinaryNode(25) 
        leftright = BinaryNode(75) 
        rightleft = BinaryNode(125) 
        rightright = BinaryNode(175) 
        rightrightleft = BinaryNode(160)
        rightrightleftleft = BinaryNode(165) 

        head.left = left
        head.right = right
        left.left = leftleft
        left.right = leftright
        right.left  = rightleft
        right.right = rightright
        rightright.left = rightrightleft
        rightrightleft.left = rightrightleftleft

        tree = BinarySearchTree(head)

        self.assertEqual(tree.IsValid(), False)


    def testBST(self):

        #               20
        #       10             30
        #                   15      35             

        head = BinaryNode(20) 
        left = BinaryNode(10) 
        right = BinaryNode(30) 
        rightleft = BinaryNode(15) 
        rightright = BinaryNode(35) 
        head.left = left
        head.right = right
        right.left  = rightleft
        right.right = rightright

        tree = BinarySearchTree(head)

        self.assertEqual(tree.IsValid(), False)

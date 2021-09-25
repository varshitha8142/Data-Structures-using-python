# Arrange in order
"""
A teacher has given her students to arrange a list of alphabets and unarranged
words of a sentance.

your task is to help the students by writing a program

first of all the unarranged alphabets or words in a sentance are given as linked lists

sort them based on the alphabetical order and return the linked list

Example 1:

input:
'f' => 'x' => 'a' => 'b' => 'i' => None

output: 
'a' => 'b' => 'f' => 'i' => 'x' => None

Example 2:

input:
'duck' => 'caught' => 'a' => 'boy' => None

output:
'a' => 'boy' => 'caught' => 'duck' => None

"""

import unittest
import helper_llists as llists


def sorted_linked_list(node):
    """
    Return the sorted linked list's head node
    """
    lis=[]
    initial_node=node
    while node!=None:
        lis.append(node.val)
        node=node.next
    lis.sort()
    i=0
    final=initial_node
    while i<len(lis) and initial_node!=None:
        initial_node.val=lis[i]
        initial_node=initial_node.next
        i+=1
    return final
class TestSortingLinkedList(unittest.TestCase):

    def test_01(self):
        node = llists.create_from_string(
            '{val:"c",next:{val:"f",next:{val:"a",next:{val:"b",next:{val:"x",next:{val:"k",next:None}}}}}}')
        sorted_list_01 = llists.create_from_string(
            '{val:"a",next:{val:"b",next:{val:"c",next:{val:"f",next:{val:"k",next:{val:"x",next:None}}}}}}')
        self.assertEqual(sorted_linked_list(node), sorted_list_01)

    def test_02(self):
        node = llists.create_from_string(
            '{val:"a",next:{val:"b",next:{val:"c",next:{val:"f",next:{val:"e",next:{val:"d",next:None}}}}}}')
        sorted_list_02 = llists.create_from_string(
            '{val:"a",next:{val:"b",next:{val:"c",next:{val:"d",next:{val:"e",next:{val:"f",next:None}}}}}}')
        self.assertEqual(sorted_linked_list(node), sorted_list_02)

    def test_03(self):
        node = llists.create_from_string(
            '{val:"string",next:None}')
        sorted_list_03 = llists.create_from_string(
            '{val:"string",next:None}')
        self.assertEqual(sorted_linked_list(node), sorted_list_03)

    def test_04(self):
        node = llists.create_from_string(
            '{val:"boy",next:{val:"varanasi",next:{val:"a",next:{val:"to",next:{val:"came",next:None}}}}}')
        sorted_list_04 = llists.create_from_string(
            '{val:"a",next:{val:"boy",next:{val:"came",next:{val:"to",next:{val:"varanasi",next:None}}}}}')
        self.assertEqual(sorted_linked_list(node), sorted_list_04)

    def test_05(self):
        node = llists.create_from_string(
            '{val:"f",next:{val:"e",next:{val:"d",next:{val:"c",next:{val:"b",next:{val:"a",next:None}}}}}}')
        sorted_list_05 = llists.create_from_string(
            '{val:"a",next:{val:"b",next:{val:"c",next:{val:"d",next:{val:"e",next:{val:"f",next:None}}}}}}')
        self.assertEqual(sorted_linked_list(node), sorted_list_05)


if __name__ == '__main__':
    unittest.main(verbosity=2)

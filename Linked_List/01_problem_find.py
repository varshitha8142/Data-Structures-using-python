# Search for an Author
"""
A dedicated librarian has collected all the names of authors, who authored the
the books or articles in his library.

He then stored this list of author names as linked list. 

Now he approached you to write a program to help a user find whether
the specified author name is present in the list or not, and give the node number,
as the node number helps the user to find the related books.

your task is to return in which node the author exist.

Example 1:

input:
linked list: "eshwar" => "kranthi" => "vikas" => None
search key : "kranthi"
output: 
2

"""

import unittest
import helper_llists as llists


def search_linked_list(node, key):
    f=0
    t=node
    count=0
    while(t!=None):
        count+=1
        if t.val==key:
            f=1
            break
        t=t.next
    if f==1:
        return count
    else:
        return -1
    """
    Return the position of the word in the list.
    Position starts with 1.
    Return -1, if the given key does not exists in the list.
    """
    '''
    class node:
    
        def __init__(self,data):
            self.data=data
            self.next=None
            head=0
            key=(input("enter name"))
            b=0
            n=int(input("enter no.of nodes:"))
            for i in (range(1,n)):
                c=(input("enter the data:"))
                if(head==0):
                    head=node(c)
                    n=head
                else:
                    n.next=node(c)
                    n=n.next
                t=n
                if(key==t.data):
                    print(i)
                    b+=1
                t=t.next
            if(b==1):
                pass
                        
            else:
                print("element node is not found")
                '''
            

class TestSearchLinkedList(unittest.TestCase):

    def test_01(self):
        node = llists.create_from_string(
            '{val:"arun",next:{val:"babu",next:{val:"john",next:{val:"kavya",next:{val:"raheem",next:{val:"surya",next:None}}}}}}')
        search_key = "john"
        nodenumber = 3
        self.assertEqual(search_linked_list(node, search_key), nodenumber)

    def test_02(self):
        node = llists.create_from_string(
            '{val:"arun",next:{val:"babu",next:{val:"john",next:{val:"kavya",next:{val:"raheem",next:{val:"surya",next:None}}}}}}')
        search_key = "surya"
        nodenumber = 6
        self.assertEqual(search_linked_list(node, search_key), nodenumber)

    def test_03(self):
        node = llists.create_from_string(
            '{val:"arun",next:{val:"balu",next:{val:"john",next:{val:"kavya",next:{val:"raheem",next:{val:"surya",next:None}}}}}}')
        search_key = "arun"
        nodenumber = 1
        self.assertEqual(search_linked_list(node, search_key), nodenumber)

    def test_04(self):
        node = llists.create_from_string(
            '{val:"arun",next:{val:"arun madhav",next:{val:"john",next:{val:"kavya",next:{val:"raheem",next:{val:"surya",next:None}}}}}}')
        search_key = "arun madhav"
        nodenumber = 2
        self.assertEqual(search_linked_list(node, search_key), nodenumber)

    def test_05(self):
        node = llists.create_from_string(
            '{val:"arun",next:{val:"arun madhav",next:{val:"john",next:{val:"kavya",next:{val:"raheem",next:{val:"surya",next:None}}}}}}')
        search_key = "govind"
        nodenumber = -1
        self.assertEqual(search_linked_list(node, search_key), nodenumber)

    def test_06(self):
        node = llists.create_from_string(
            '{val:"arun",next:None}')
        search_key = "govind"
        nodenumber = -1
        self.assertEqual(search_linked_list(node, search_key), nodenumber)

    def test_07(self):
        node = llists.create_from_string(
            '{val:"arun",next:None}')
        search_key = "arun"
        nodenumber = 1
        self.assertEqual(search_linked_list(node, search_key), nodenumber)


if __name__ == "__main__":
    unittest.main(verbosity=2)

# Guess the switch that is "on"
"""
There is a switch board which is having 8 switches. Each switch has a number like
0 for switch 1, 1 for switch 2, 2 for switch 3 and so on. so the switch numbers will be 
0, 1, 2, 3, 4, 5, 6, 7 -> each one is called switchnumber
If a switch is on/off then an integer number with ( 2 to the power of switchnumber) is 
recorded as linked list

Ram, a student is now tasked to switch on and off the switches. for every turn Ram 
can on and off all or few switches, any number of times.

The data for on and off the switches will be recored as a string and later converted 
to a linked list

your task is to find which switches are on at the end of a turn

you will be provided with a record of one turn as a string, but internally it is
converted as linked list

you have to go throught the constructed linked list to get the answer

Example 1:

input_string_for_linked_list = "2->4->32"

output_switches = [1, 2, 5]

Explination: 

2 is 2**1, 4 is 2**2, 32 is 2**5

as they appear only one time it is assument the corresponding switches are "on"

so return their switchnumbers as list [1, 2, 5]

Example 2:

input_string_for_linked_list = "2->4->2"

output_switches = [2]

Explination:

in the string 2 appears two times, for the first time 2 appears we assume that its
corresponding switch is "on" and when again 2 appears its corresponding switch is "off"

so there is only one switch which is "on" -> 4 and its switchnumber is 2 (2**2)

hence return [2] as list
"""

import unittest
import helper_llists as llists
import math


def get_on_switches(node):
    """
    Return the list of switches, which are on.
    """
    lis=[]
    while node!=None:
        count=0
        while 2**(count)!=node.val:
            count+=1
        if count not in lis:
            lis.append(count)
        else:
            lis.remove(count)
        node=node.next
    lis.sort()
    return lis
class TestGetOnSwitches(unittest.TestCase):

    def test_01(self):
        node = llists.create_from_string(
            "{val:1,next:None}")

        output_switches = [0]

        self.assertEqual(get_on_switches(node), output_switches)

    def test_02(self):
        node = llists.create_from_string(
            "{val:2,next:{val:4,next:{val:32,next:None}}}")

        output_switches = [1, 2, 5]

        self.assertEqual(get_on_switches(node), output_switches)

    def test_03(self):
        node = llists.create_from_string(
            "{val:2,next:{val:4,next:{val:2,next:None}}}")

        output_switches = [2]

        self.assertEqual(get_on_switches(node), output_switches)

    def test_04(self):
        node = llists.create_from_string(
            "{val:2,next:{val:4,next:{val:32,next:{val:16,next:{val:4,next:{val:2,next:{val:4,next:None}}}}}}}")

        output_switches = [2, 4, 5]

        self.assertEqual(get_on_switches(node), output_switches)

    def test_05(self):
        node = llists.create_from_string(
            "{val:2,next:{val:4,next:{val:32,next:{val:16,next:{val:64,next:{val:16,next:{val:4,next:{val:64,next:{val:128,next:{val:1,next:None}}}}}}}}}}")

        output_switches = [0, 1, 5, 7]

        self.assertEqual(get_on_switches(node), output_switches)


if __name__ == '__main__':
    unittest.main(verbosity=2)

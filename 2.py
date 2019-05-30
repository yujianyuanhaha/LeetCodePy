#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 22:49:21 2018

@author: Jet
"""

def addTwoNumbers( l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans = []
        # align list
        len1 = len(l1)
        len2 = len(l2)
        if len1 > len2:
            delta = len1 - len2
            for i in range(delta):
                l2.append(0)
        elif len1 < len2:
            delta = len2 - len1
            for i in range(delta):
                l1.append(0)
        # do bit-by-bit calculation
        lenmax = max(len1,len2)
        tenDigit = 0
        for i in range(lenmax):
            temp = l1[i] + l2[i] + tenDigit
            tenDigit = temp / 10
            oneDigit = temp % 10
            ans.append(oneDigit)
        if tenDigit:
            ans.append(tenDigit)               
        
        return ans

if __name__ == '__main__':
    l1 = [2,4,3]
    l2 = [0]
    # ans = 342+465 = 807
    ans = addTwoNumbers(l1,l2)
    print(ans)
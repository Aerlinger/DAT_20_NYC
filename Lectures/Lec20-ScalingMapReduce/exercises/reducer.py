#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

tmp = ""
val = 0

for line in sys.stdin:
    i = line.split()
    if tmp and (len(i) > 0) and i[0] != tmp:
        print tmp, val
        val = 0
    tmp = i[0]

    if len(i) > 1:
      val += int(i[1])

print tmp, val


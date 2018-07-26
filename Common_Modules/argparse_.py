#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Argparse: Parser for command-line options, arguments and sub-commands

# 定位参数和选项参数混合使用
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',const=sum, default=max,help='sum the integers (default: find the max)')
args = parser.parse_args(['--sum', '7', '-1', '42'])
print(args.accumulate(args.integers))
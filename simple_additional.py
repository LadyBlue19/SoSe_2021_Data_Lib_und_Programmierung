# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# -> Kommentare lassen und werden auch nicht ausgeführt
"""
längere Kommentare, über mehrere Zeilen
:)
"""

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("nummer_1", type=int, help="An Integer")
parser.add_argument("nummer_2", type=int, help="Another Integer")
# parser.add_argument("-multi", default=False, action="store_true")
parser.add_argument("--operation", choices=["sum", "mult", "div", "sub"])

args = parser.parse_args()


# Nun Kommentar -> kein aktiver Code mehr
# print(args)
# print(args.nummer_1, args.nummer_2)

if args.operation == "div":
    result = args.nummer_1 / args.nummer_2
elif args.operation == "sum":
    result = args.nummer_1 + args.nummer_2
elif args.operation == "sub":
    result = args.nummer_1 - args.nummer_2
elif args.operation == "mult":
    result= args.nummer_1 * args.nummer_2

# Für Multipliaktionen und Aditionen
# if args.multi:
   # result = args.nummer_1 * args. nummer_2
# else:
    # result = args.nummer_1 + args. nummer_2

print(result)

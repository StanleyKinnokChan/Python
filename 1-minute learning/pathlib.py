from pathlib import Path



def seperator():
    print("  -----------------------------------------------")

#1. what is __file__?
print(f"  1: {__file__}")
seperator()

#2. Path object
test = Path(__file__)
print(f"  2: {__file__}")
seperator()

#3. Path object, normalized the path (e.g. slash to backslash in window)
test = Path(__file__).resolve()
print(f"  3: {test}")
seperator()

#3. Path object, normalized the path (e.g. slash to backslash in window), move up by 1 level
test = Path(__file__).resolve().parents[0]
print(f"  4: {test}")
seperator()
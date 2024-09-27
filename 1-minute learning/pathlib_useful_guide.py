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

#4. useful
print(f"original : {Path(__file__)}")
print(f"suffix : {Path(__file__).suffix}")
print(f"stem : {Path(__file__).stem}")
print(f"parent : {Path(__file__).parent}")
new_file_path = Path(__file__).parent.joinpath(f"new_name_{Path(__file__).suffix}")
print(f"joinpath : {new_file_path}")

##'rename file
#file_path.rename(new_file_path)

## delete file
# file_path.unlink()
import import_script_1
print("top-level in two.py")

import_script_1.func_a()

if __name__ == "__main__":
    print("script2 is being run directly")
else:
    print("script2 is being imported into another module")
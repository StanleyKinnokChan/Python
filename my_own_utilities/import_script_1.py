def func_a():
    print("func() in one.py")

print("top-level in one.py")

if __name__ == "__main__":
    print("script1 is being run directly")
else:
    print("script1 is being imported into another module")
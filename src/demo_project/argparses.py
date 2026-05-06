import argparse

a = argparse.ArgumentParser()
a.add_argument("command")
a.add_argument("value", nargs="?")
b = a.parse_args()
print("command is ", b.command)
print("value is ", b.value)

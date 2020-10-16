a = ["erfan","hi","ffff"]

def main():
   num = -1
   for i in a:
       if num < len(a):
           yield i
           num += 1

for returnedval in main():
    print(returnedval)
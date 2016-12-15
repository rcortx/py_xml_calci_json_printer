#!/usr/bin/python
# cmd_interpret.py by Cubohan
# circa 2016

socv = ['{', '[',]
eov = [']', '}', ',',]
inde = "    "
def indent(lev):
    for _ in range(lev):
        print(inde, end="")

def print_json(st):
    lev = 0
    skip_n = False
    for ind, i in enumerate(st):
        if skip_n:
            skip_n = False
            continue
        if i in eov:
            if i != ',':
                print("\n", end="")
                lev -= 1 
                indent(lev)
            print(i, end="")
            if ind<len(st)-1:
                    if st[ind+1] == ",":
                        print(st[ind+1], end="")
                        skip_n = True
            print("\n", end="")
            indent(lev)
            continue
        print(i, end="")
        if i in socv:
            lev += 1
            print("\n", end="")
            indent(lev)

def test():            
    st = ['{“group” : {lis : [1,2,3]}, “list” : [“a”,”b”,”c”]}',
         '{“group” : {lis : [{“group” : {lis : [1,2,3]}, “list” : [“a”,”b”,”c”]},2,{“group” : {lis : [1,2,3]}, “list” : [“a”,”b”,”c”]}]}, “list” : [“a”,”b”,”c”]}',
          '{“group” : {lis : [“group”,[“a”,”b”,”c”],“group”]}, “list” : [“a”,”b”,”c”]}',
          '{“group” : {lis : [1,2,3]}, “list” : [“a”,”b”,”c”]}',
          '{“group” : {lis : [1,2,3]}, “list” : [“a”,”b”,”c”]}',
         ]
    for i in range(len(st):
        print_json(st[i])
        print("\n\n **END** \n\n")
        
if __name__ == "__main__": test()

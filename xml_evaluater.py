#!/usr/bin/python
# cmd_interpret.py by Cubohan
# circa 2016

def add(els):
    print("Executing...")
    print(" + ".join(map(str, els)), ' = {}'.format(sum(els)))
    return sum(els)


def sub(els):
    print("Executing...")
    ans = 2*els[-1] - sum(els)
    print(" - ".join(map(str, els)), ' = {}'.format(ans))
    return ans


def div(els):
    print("Executing...")
    ans = els[-1]/els[0]
    print(" / ".join(map(str, els)), ' = {}'.format(ans))
    return ans


def mul(els):
    print("Executing...")
    ans = 1
    for i in els:
        ans*=i
    print(" * ".join(map(str, els)), ' = {}'.format(ans))
    return ans


def extract_next(st, i): # NAIVE XML parser without REGEX
    if i>len(st)-8:
        return (None, None)
    el = None
    while st[i] != _open:
        i += 1
        if i>len(st)-8:
          return (None, None)
    ends = i+1
    while st[ends] != _clos:
        ends += 1
    el = st[i+1:ends]
    i = ends+1
    ends = i+1
    if end in el:
        return (end, i)
    if not el in op:
        while st[ends] != _open:
            ends += 1
        el = st[i:ends]
        while st[ends] != _clos:
            ends += 1
        i = ends + 1
    return (el, i)

def resolve(st):
    ind = 6
    sta = []
    while(True):
        el, ind = extract_next(st, ind)
        if el == None: break  
        if el == end: 
            els = []
            cur = sta.pop()
            els.append(cur)
            while els:
                cur = sta.pop()
                if type(cur) == str:
                    break
                els.append(cur)
            sta.append(op[cur](els))
            continue
        sta.append(el if not (el.isdigit() or el[1:].isdigit()) else int(el))
    print("Answer: {}".format(sta[0]))

end = "/"
_open = '<'
_clos = '>'
op = {"sum":add, "div":div, "mul":mul, "sub":sub}

def test():
    st = """<expr>

    <sum>

    <elem>4</elem>

    <elem>6</elem>

    <elem>7</elem>

    <mul>

    <elem>4</elem>

    <elem>6</elem>

    <elem>7</elem>

    <elem>3</elem>

    </mul>

    <elem>3</elem>

    </sum>
    </expr>"""

    resolve(st)

if __name__ == "__main__": test()

def inputs():
    inp = 4
    inp_list = []
    for i in range(inp):
        inp_list.append(input("x,y: "))
    return inp_list


def make_list(x, y):
    global_lst = []

    ink = 1
    for i in range(x):          # [],[],...
        lst = []
        for k in range(y):      # [...]
            lst.append(ink)
            ink += 1
        # print(lst)
        global_lst.append(lst)

    print(global_lst)


def convert(xy):
    for i in xy:
        x, y = i.split(',')
        x = int(x)
        y = int(y)
        make_list(x, y)


if __name__ == '__main__':
    inp_l = inputs()
    convert(inp_l)

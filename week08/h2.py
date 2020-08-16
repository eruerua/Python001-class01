def like_map(func,*args):
    n = func.__code__.co_argcount
    l = len(args)
    r=[]
    if n==1:
        for arg in args[0]:
            r.append(func(arg))
    elif n>1:
        if l==1:
            for arg in args[0]:
                r.append(func(*arg))
        elif l>1:
            for arg in zip(*args):
                r.append(func(*arg))
    return r

    


def add(x,y,z):
    return x+y+z

list1=[1,2,3]
list2=[1,2,3]
list3=[1,2,3]
res=like_map(add, list1,list2,list3)
print(res)
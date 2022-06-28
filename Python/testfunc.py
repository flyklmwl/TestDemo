def robot(oldfunc):
    def newfunc():
        print("============================")
        oldfunc()
        print("============================")
    return newfunc


@robot
def hello(var1=1):
    print("hello, World!")
    print(var1)


hello()

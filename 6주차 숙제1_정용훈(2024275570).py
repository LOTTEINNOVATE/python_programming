print("1번 문제 : Come up with a function that 'divides' the first input by second input:")
def div(a, b) :
    c = a/b
    print(a, "if you divides one", b)
    return(c)
return_value = div(4,2)
print("1번 문제 정답 :", return_value)
print("===================================================")
print("2번 문제 : Use the function 'con' for the following question.")

def con (a, b) :
    c = a + b
    print(a, "if you con one", b)
    return (c)
return_value = con (1,2)
print("2번 문제 정답 :", return_value)
print("===================================================")
print("3번 문제 : Can the 'con' function we defined before be used to add integers or strings?")
def con (a, b) :
    return a + b
print("3번 문제 정답 :",con(2,2))
print("===================================================")
print("4번 문제 : Can the 'con' function we defined before be used to concentrate a list or tuple?")
def con (a, b) :
    return a + b
return_value = con([('a',1)], [('b',1)])
print("4번 문제 정답 :" , return_value)
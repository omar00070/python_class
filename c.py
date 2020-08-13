# def hello(name):
#     name = name.capitalize()
#     if name == "": return "hello world"
#     return "hello " + name


# f'hello {name}'


# def function1():
#     return 3

# def function2():
#     print(4)

# x = function1()
# y = function2()


# print("this is x",x, "this is y", y)


# def AreaCircle(r):
#     area = r**2 * 22/7
#     return area




# def function3():
#     return 10
#     return 20
#     print(1922)

# print(function3())
x = 25


def function5():
    global x
    x = x + 5
    print("this is inside the function",x)
    return "hello"

function5()
print("this is outside the function",x)




x_list = [1, 2, 3, 4, 5, 6]
print(x_list)

x_list[5] = "something"
print(x_list)

x_list.append('newthing')
print(x_list)

x_list.insert(2, "something at index 2")
print(x_list)

x_list.remove(3)
x_list.insert( 3,"III" )
print(x_list)

print(len(x_list)) # number of elements


len_list_x = len(x_list)

x_list.insert(len_list_x, 'new thing at the end')
print(x_list)

len_list_x = len(x_list)
print(x_list[len_list_x - 1]) # -1 because the len gives you the number of elements but indecies start from 0

new_tuple = (1, 2, 3, 5, 6, "something", [1, 3, 5])

print(type(new_tuple[5]))

print(new_tuple)
# number = 2
# assert number<5, f'The number should not exceed 5'
# print(number)


# def addFunct(a,b):
#     if a > 5 or b>5:
#         raise Exception("Value of a or b is higher than 5")
#     return a+b
# try:
#     addFunct(10,3)
# except Exception as e:
#     print(e)


def divide(a,b):
    if a<0 or b<0:
        raise Exception('Either of a of B is negative')
    x=  a//b

# try:
#     divide(2,3)
# # except ZeroDivisionError as error:
# #     print(error)
# except Exception as e:
#     pass



# print(divide(-1,-1))
# print('Hello')


try:
    with open("file.log") as file:
        read_data = file.read()
except:
    print("Couldn't open file.log")
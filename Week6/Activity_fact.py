number = [1, 2, 3, 4, 5]

factorials = [1 if n == 0 else (f := 1, [f := f * i for i in range(1, n + 1)], f)[-1] for n in number]
print(factorials)

# f =5
# i=3
# f:= f*i
# # f*=i
# print(f)
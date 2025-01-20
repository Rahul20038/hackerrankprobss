x, k = map(int, input().split())
polynomial = input()
result = eval(polynomial)
if result == k:
    print("True")
else:
    print("False")


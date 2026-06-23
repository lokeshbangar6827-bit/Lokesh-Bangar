str=input("enter string to check char count\n")
ip=input("enter char to check: ")
ct =0
for ch in str:
    if ch==ip:
        ct+=1
print(ct)
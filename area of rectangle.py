def area_rectangle(length,width):
    if length==width:
        return "This is a square!"
    else:
        return length*width
length=int(input("Enter the lenght of the rectangle  "))
width=int(input("Enter the width of the rectangle  "))
res=area_rectangle(length,width)
print(res)

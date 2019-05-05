
def  pentagon(a,r):
    area = (5 * (int (a) * int (r) )) / 2
    perimeter = 5 * int(a)
    
    print ("Pentagon area  :"+ str(area)) # مساحت
    print ("Pentagon perimeter :"+ str(perimeter)) # محیط

a = input("input the border length? ") # طول ضلع
r = input("input radius (r): ") # شعاع

pentagon(a,r)
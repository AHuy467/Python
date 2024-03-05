#Đọc gh file
#Lê Anh Huy
#19/01/2024

obj = open("data.txt","w")  ##mo file data.txt
obj.write("Python xin chao Huy") ##Ghi dong nay vao txt
obj.close() ##ghi xong dong file
obj1 = open("data.txt","r") ##
s=obj1.read()
print (s)
obj1.close()
obj2=open("data.txt","r")
s1=obj2.read(10)
print(s1)
obj2.close()
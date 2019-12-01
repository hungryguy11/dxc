# fr=open("visual.jpg","rb")

# data=fr.read(250*140)
# i=0
# while data:
    
#     i+=1
#     print(i)
#     chunk=open("C:\\Users\\croy20\\Desktop\\python\\Assignments\\day3\\chunks"+str(i)+".jpg","wb")
#     chunk.write(data)
#     chunk.close()
#     data=fr.read(250*140)
# fr.close()

f=open("visual.jpg","rb")
chunk=250
i=1
while True:
    data=f.read(chunk)
    if not data:
        break
fo=open("chunk"+str(i)+'.jpg', 'wb')
fo.write(data)
fo.close()
file = open ("myfile.txt","a")
file.write("Hello!!")
file.close()

try:
    file = open ("myfile2.txt", "r")
    contents = file.read()
    print (contents)
    file.close()
except:
    print ("Could not find file. Creating new file. ")
    file = open ("myfile2.txt", "w")
    file.close()

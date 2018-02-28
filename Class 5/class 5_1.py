try:
    f=open('Python_text_file.txt','r')
    g=f.read()
    print(g)
    f.close()
except IOError:
    print("Sorry this file does not exist\n")    

try:
    f=open('Python_text_file.txt','a')
    data= ' Hello world '
    f.write(data)
    f.close()

    f=open('Python_text_file.txt','r')
    g=f.read()
    print(g)
    print('\n')
    f.close()
except IOError:
    print("Sorry this file does not exist\n")   

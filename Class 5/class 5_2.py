try:
    f=open('Python_text_file_2.txt','r')
    g=f.read()
    print(g)
    f.close()
except IOError:
    print("Sorry this file does not exist\n")    


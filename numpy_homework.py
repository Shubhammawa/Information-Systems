import numpy as np
Record=np.random.randint(0,100,size=60).reshape(10,6)
print('Marks List\n')
print(Record)
print('\n1 - Students with highest and lowest marks\n2 - Students with highest and lowest average scores\n3 - Student with highest score across all subjects\n\nEnter choice ')

Total_marks=Record.sum(axis=1)
Mean=Record.mean(axis=0)
while 1:
    try:
        choice=input()
        if not choice.isdigit():
            raise ValueError('Please enter 1 2 or 3')
        else :
            break
    except ValueError as err:
        print(err)
 
if (int(choice)==1):
    print('Highest total marks - Student {} - {}\nLowest total marks - Student {} - {}'.format(np.argmax(Total_marks)+1,Total_marks.max(),np.argmin(Total_marks)+1,Total_marks.min()))
elif (int(choice)==2):
    print('Highest average score - Subject {} - {}\nLowest average score - Subject {} - {}'.format(np.argmax(Mean)+1,Mean.max(),np.argmin(Mean)+1,Mean.min()))
elif (int(choice)==3):
    print('Student {} Subject {} Marks {}'.format(int((np.argmax(Record)/6))+1,(np.argmax(Record)%6)+1,Record.max()))
else :
    print('Invalid choice')
    

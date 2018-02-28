import csv
import json
import decimal

def Accept_input():
    'Reads all data from csv file'
    with open ('Student_Record.csv', newline='') as csvfile:
        record_reader = csv.reader(csvfile, dialect='excel', delimiter=',')
        record_list=[]
        for row in record_reader:
            record_list.append(row)
        return record_list
        
def Do_processing(record_list):
    'Finds SGPA for each semester and CGPA and keeps in a jsn file'
    points=0
    sgpa_1_list=['','','',]
    cgpa_1_list=['','','',]
    for j in range(3,23):
        for i in range(5,12):
            points=points+(int(record_list[2][i]))*(int(record_list[j][i]))
        sgpa_1=round(points/23,2)                                  #change this. (for any value)
        sgpa_1_list.append(sgpa_1)
        cgpa_1=sgpa_1
        cgpa_1_list.append(cgpa_1)
        points=0
    
    sgpa_2_list=['','','',]
    cgpa_2_list=['','','',]
    for j in range(3,23):
        for i in range(12,19):
            points=points+(int(record_list[2][i]))*(int(record_list[j][i]))
        sgpa_2=round(points/22,2)                                                     #change this. (for any value)
        sgpa_2_list.append(sgpa_2)
        cgpa_2=(cgpa_1_list[j]*23+sgpa_2_list[j]*22)/45
        cgpa_2_list.append(round(cgpa_2,2))
        points=0
    
    sgpa_3_list=['','','',]
    cgpa_3_list=['','','',]
    for j in range(3,23):
        for i in range(19,27):
            points=points+(int(record_list[2][i]))*(int(record_list[j][i]))
        sgpa_3=round(points/25,2)                                                     #change this. (for any value)
        sgpa_3_list.append(sgpa_3)
        cgpa_3=(cgpa_2_list[j]*45+sgpa_3_list[j]*25)/70
        cgpa_3_list.append(round(cgpa_3,2))
        points=0
    
    sgpa_4_list=['','','',]
    cgpa_4_list=['','','',]
    for j in range(3,23):
        for i in range(27,34):
            points=points+(int(record_list[2][i]))*(int(record_list[j][i]))
        sgpa_4=round(points/21,2)                                             #change this. (for any value)
        sgpa_4_list.append(sgpa_4)
        cgpa_4=(cgpa_3_list[j]*70+sgpa_4_list[j]*21)/91
        cgpa_4_list.append(round(cgpa_4,2))
        points=0

    data={
        'sgpa_1' : sgpa_1_list,
        'sgpa_2' : sgpa_2_list,
        'sgpa_3' : sgpa_3_list,
        'sgpa_4' : sgpa_4_list,
        'cgpa_1' : cgpa_1_list,
        'cgpa_2' : cgpa_2_list,
        'cgpa_3' : cgpa_2_list,
        'cgpa_4' : cgpa_4_list,
    }
    
    json_str = json.dumps(data)
    data = json.loads(json_str)

    with open('Student_Record_JSON.json','a') as f:
        json.dump(data,f)
    f.close()
    result_list=[sgpa_1_list,sgpa_2_list,sgpa_3_list,sgpa_4_list,cgpa_4_list]
    return result_list
    

def Execute_query(result_list,record_list):
    'Provides menu to find the topper semester wise and overall, weak students, sorting the student list as per cgpa'
    print("Enter\n  1 for Semester 1 topper\n  2 for Semester 2 topper\n  3 for Semester 3 topper\n  4 for Semester 4 topper\n  5 for overall topper\n 6 for preparing list of weak students")
    choice= int(input())
    if choice==1:
         max_1=0
         j=3
         for k in range(3,23):
            
             i= float(result_list[0][k])
             if i>max_1:
                     max_1=i
                     pos=j
                     j+=1
             else :
                     j+=1
         return record_list[pos][1]

    elif choice==2:
         max_1=0
         j=3
         for k in range(3,23):
            
             i= float(result_list[1][k])
             if i>max_1:
                     max_1=i
                     pos=j
                     j+=1
             else :
                     j+=1
                
         return record_list[pos][1]
    elif choice==3:
         max_1=0
         j=3
         for k in range(3,23):
            
             i= float(result_list[2][k])
             if i>max_1:
                     max_1=i
                     pos=j
                     j+=1
             else :
                     j+=1
                
         return record_list[pos][1]
    elif choice==4:
         max_1=0
         j=3
         for k in range(3,23):
            
             i= float(result_list[3][k])
             if i>max_1:
                     max_1=i
                     pos=j
                     j+=1
             else :
                     j+=1
                
         return record_list[pos][1]
    elif choice==5:
         max_1=0
         j=3
         for k in range(3,23):
            
             i= float(result_list[4][k])
             if i>max_1:
                     max_1=i
                     pos=j
                     j+=1
             else :
                     j+=1
                
         return record_list[pos][1]

    
    elif choice==6:
        weak_student_list=[]
        j=3
        for k in range(3,23):
            i=float(result_list[4][k])
            if i<8:
                pos=j
                weak_student_list.append(record_list[pos][1])
                j+=1
            else :
                j+=1
        return weak_student_list                
            
    elif choice==7:
        sort_cgpa=[]
        sort_name=[]
        for s in range(3,23):
            sort_cgpa.append(result_list[4][s])
        for k in range(3,23):
            sort_name.append(record_list[k][1])
        for k in range(0,20):
            j=k+1
            for j in range(0,20):
                if sort_cgpa[k]<sort_cgpa[j]:
                    a=sort_cgpa[k]
                    sort_cgpa[k]=sort_cgpa[j]
                    sort_cgpa[j]=a
                    b=sort_name[k]
                    sort_name[k]=sort_name[j]
                    sort_name[j]=b
        sort_result=[sort_name,sort_cgpa]
        return sort_result
        
        
def Show_output(ouput,n=1):
    'Prepare above reports and store it in a text file'
    print("Semester { }\nTopper : ",n,ouput)
record_list=Accept_input()
result_list=Do_processing(record_list)
output=Execute_query(result_list,record_list)
Show_output(output)

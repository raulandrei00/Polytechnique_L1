

def average (numlist):
    avg = 0.0
    for num in numlist:
        avg += num
    avg /= len(numlist)

    

    return round(avg , 2)


def string_floats_to_list (string_floats):
    ret = [float(i) for i in string_floats.split(' ')]
    return ret

def student_data(data_string):
    frs = data_string.split(' ')[0]
    
    return (frs , string_floats_to_list(data_string.replace(frs + ' ' , '')))

def student_data_to_string(name, results):
    ret = name
    for item in results: 
        ret += " " + str(item)
    
    return ret


def read_student_data(filename):
    with open(filename , 'r') as file:
        students = file.readlines()
       
        ret = []
        for item in students:
            item = item.replace('\n' , '')
            newitem = student_data(item.replace('\n' , ''))
            
            ret.insert(len(ret) , newitem)
        
        return ret

def extract_averages(filename):
    
    vect = read_student_data(filename)
    
    ret = []

    for item in vect:
        ret.insert(len(ret) , (item[0] , average(item[1])))
        
    
    return ret


def discard_scores(numlist):
    fr = min(numlist[2] , numlist[3]) 
    sec = max(numlist[3] , numlist[2])
    pos1 = 2 
    pos2 = 3
    if fr == numlist[3]:
        pos1 , pos2 = pos2 , pos1
    n = len(numlist)
    for i in range(4 , n):
       # print(pos1 , pos2)
        if fr > numlist[i]:
            sec = fr
            fr = numlist[i]
            pos2 = pos1
            pos1 = i
        elif sec > numlist[i]:
            sec = numlist[i]
            pos2 = i

    newarr = []
    for i in range(2, n):
        if i != pos1 and i != pos2:
            newarr.insert(len(newarr) , numlist[i])

    return newarr

def sum (arr):
    ret = 0
    for el in arr: 
        ret += el
    return ret

def summary_per_student(infilename, outfilename):
    
    
    data = read_student_data(infilename)
   

    totalavg = 0.0

    with open (outfilename, 'w') as file:
        for stud in data:
            file.write(student_data_to_string(stud[0], discard_scores(stud[1])) + " sum: " + str(round(sum(discard_scores(stud[1])), 2) ))
            totalavg += sum(discard_scores(stud[1]))
            file.write("\n")

        totalavg /= len(data)

        file.write("total average: " + str(round(totalavg , 2)))
        file.write('\n')


def summary_per_tutorial(infilename, outfilename):

    data = read_student_data(infilename)

    ans = []
    for td in data[0][1]:
        ans.insert(len(ans) , [0 , 1000000, 0])

    with open (outfilename, 'w') as file:
        for stud in data:
            use = stud[1]
            for i in range(0 , len(use)):
                ans[i][0] += use[i]
                ans[i][1] = min(ans[i][1] , use[i])
                ans[i][2] = max(ans[i][2] , use[i])

        for i in range (0 , len(ans)):
            ans[i][0] = round(ans[i][0] / len(data) , 2)
            file.write ("TD" + str(i+1) + ": average: " + str(ans[i][0]) + " min: " + str(ans[i][1]) + " max: " + str(ans[i][2]))
            file.write('\n')

#print ( summary_per_student("plm.in" , "plm.out") )

#print(summary_per_tutorial("plm.in" , "plm.out"))
import json
data = []
def func1():
    
    with open('alicedata.json') as json_file:
        for line in json_file:
            global data
            data.append(json.loads(line))
            #print(line)
        return data
    
e1=func1()

def func9(e1):
    lst=[]
    for i in e1:
        if(i['name']== 'vehicle_speed'):
            if (i['value']==0):
                lst.append(i['timestamp'])
    print(lst)
    print("idle time",max(lst)-min(lst))
func9(e1)
                
    
def func7(e1):
    lst=[]
    lst_a=[]
    lst_1=[]
    lst1=[]
    lst2=[]

    for i in e1:
        if(i['name']== 'transmission_gear_position'):
            lst.append(i['value'])
    #print(lst)
    for k in range(len(lst)):
        if(lst[k]=='first'):
            lst[k]=1
        elif(lst[k]=='second'):
            lst[k]=2
        elif(lst[k]=='three'):
            lst[k]=3
        elif(lst[k]=='second'):
            lst[k]=4
        else:
            lst[k]=0 #for 'neutral' gear
    print(lst)

    for i in e1:
        if(i['name']== 'transmission_gear_position'):
            if not i['value'] in lst_a:
                lst_a.append(i['value'])
    print(lst_a)

    

    
    import pygmaps
    import webbrowser
    for i in e1:
        lst_1.append(i['timestamp'])
        
    for i in e1:
        if(i['name']== 'latitude'):
            lst1.append(i['value'])
    
    for i in e1:
        if(i['name']== 'longitude'):
            lst2.append(i['value'])
            
    mymap = pygmaps.maps(lst1[int((len(lst1))/2)], lst2[int((len(lst2))/2)], 16)
    path = list(zip(lst1,lst2))
    mymap.addpath(path,"#00FF00")
    mymap.draw('./mymap.html')

func7(e1)

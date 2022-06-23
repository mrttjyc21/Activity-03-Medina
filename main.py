import thisIsStatusclass as stat
import thisIsEVclass as ev

def computation_type(data):

    print("please input (1) for Status or (2) EV  calculation")
    opt = int(input())

    if(opt == 1):
        thisIsStatusclass (data)

    elif(opt == 2):
        thisIsEVclass (data)
    else:
        print("Invalid input") 

def thisIsStatusclass (stat_data): 
   
    total_hp = stat.compute.hp(stat_data)
    print("The total hp is: ")
    print(total_hp)

   
    other_stat = stat.compute.other_stat
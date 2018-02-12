def check16(lst):
    count=0
    for i in lst:
        for x in i:
            if x =='x':
                count+=1
    if count==16:
                return True
    else:
        return False

def check(lst):
    count=0
    lst2=[]
    for i in lst:
        for z in i:
            if(z!='x'):
                lst2.append(z)
    for i in range(0,len(lst2)):
        for j in range(i+1,len(lst2)):
            if abs(lst2[i]-lst2[j]) == 4 or abs(lst2[i]-lst2[j]) == 1:
                if not((lst2[i]==4 and lst2[j]==5)or(lst2[j]==4 and lst2[i]==5)or(lst2[i]==8 and lst2[j]==9)or(lst2[j]==8 and lst2[i]==9)or(lst2[i]==12 and lst2[j]==13)or(lst2[i]==12 and lst2[j]==13)or lst2[i]>16 or lst2[i]<1 or lst2[j]>16 or lst2[j]<1):
                    return False
    return True
changer = 1
lst=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(lst[0])
print(lst[1])
print(lst[2])
print(lst[3])
while(True):
    if(changer == 1):
        print( 'please player 1 will play : ')
        x=int (input())  
        y=int (input()) 
        if(x>16 or x<0 or y>16 or y<0):
            print('the number is bigger ')
            continue
        if(x==5 and y==4 or x==4 and y==5 or x==8 and y==9 or x==9 and y==8 or x==12 and y==13 or x==13 and y==12 or lst[(x-1)//4][(x%4)-1]=='x' or lst[(y-1)//4][(y%4)-1]=='x'):
            print('wrong positionand not be x')
            continue
        
        if abs(x-y)==4 or abs(x-y)==1:
                  lst[(x-1)//4] [x%4-1]='x'
                  lst[(y-1)//4] [y%4-1]='x'
                  print(lst[0])
                  print(lst[1])
                  print(lst[2])
                  print(lst[3])
        if(check16(lst)):
            print ("draw")
            break
        if(check(lst)):
            print('player 1 is the winner ')
            break
            if(abs(temp1-temp2)!=1 or abs(temp1-temp2)!=4):
                 print('player 1 is winner')
                 break
            else:
                 continue  
        changer = 2
    elif(changer == 2):
        print('player 2 will play : ' )
        x1=int (input())
        y1=int (input())
        if(x>16 or x<0 or y>16 or y<0):
            print('wrong inputs')
            continue
        if((x1==5 and y1==4) or (x1==4 and y1==5 )or (x1==8 and y1==9) or (x1==9 and y1==8) or (x1==12 and y1==13) or (x1==13 and y1==12) or lst[(x1-1)//4][(x1%4)-1]=='x' or lst[(y1-1)//4][(y1%4)-1]=='x'):
            print('wrong position and not be x')
            continue        
        if abs(x1-y1)==4 or abs(x1-y1)==1:
            lst[(x1-1)//4] [x1%4-1]='x'
            lst[(y1-1)//4] [y1%4-1]='x'
            print(lst[0])
            print(lst[1])
            print(lst[2])
            print(lst[3])
        else:
            print('wrong number and wrong position')
        if(check16(lst)):
            print ("draw")
            break
        changer = 1
        #break
        if(check(lst)):
            print('player 2 is the winner ')
            break
        
            if(abs(temp1-temp2)!=1 or abs(temp1-temp2)!=4):
                 print('player 2 is winner')
                 break
            else:
                 u=temp1
                 continue
                 




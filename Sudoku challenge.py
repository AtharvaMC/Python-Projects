import random,numpy
from math import sqrt


class GetSet_:
	
    def getRandomSudoku(self): 
        for i in range(slen):
            sudokuRandom.append([])
            for j in range(slen):
                
                if (i == 0 and j == 0) or (i == slen - 2 and j == slen - 2):
                    val = random.randint(1, slen)
                else:
                    val = 0
                sudokuRandom[i].append(val)

            
    def MakeSudoku(self,sudokuAns):
    	for i in range(slen):
    		for j in range(slen):
    			sudokuRandom[i][j]=sudokuAns[i][j]
    
    	for k in range(slen*slen):
    		i= random.randint(0,slen-1)
    		j= random.randint(0,slen-1)
    		sudokuRandom[i][j]=0
    		
    	print('\nSolve the given sodoku...')
    	obj1.show(sudokuRandom)
			
			
    def show(self,sudoku):
    	for i in range(slen):
    		print("|", end=" ")
    		for j in range(slen):
                    print(sudoku[i][j],end=" | ")
    		print("")
        	



class sudoBrain_():

    def check(self,sudokuAns):
        global sudokuInput,flag,valid
        for i in range(slen):
        	row=list(input("Entre the values of row {} without any space and comma:" .format(i+1)))
        	row=[int(i) for i in row]
        	for i in row:
                    if i>slen or i<=0:
                        print("You Entered invalid value",i,"is not valid")
                        valIndex=row.index(i)
                        row[valIndex]=int(input("Please enter valid value: "))
                        while row[valIndex]>slen or row[valIndex]<=0:
                            print("You Entered invalid value",row[valIndex],"is not valid")
                            row[valIndex]=int(input("Please enter valid value: "))
          
        	sudokuInput.append(row)
        	print(numpy.matrix(row))
        print('Your Sudoku:-')
        obj1.show(sudokuInput)
        #new condition
        obj2. checkValid(sudokuInput)
        if valid==slen**2:
        	for i in range(slen):
        		for j in range(slen):
        			if sudokuAns[i][j] ==sudokuInput[i][j]:
        			     flag+=1
        			else:
        				flag=0
        	if (flag==slen**2) or (valid==slen**2):
        		print('Congratulations!!You are correct')
        		if (flag!=slen**2):
        			print('Another solution for this sudoku:')
        			obj1.show(sudokuAns)
        else:#else of new condition's if
        	print('**Oops!! You are wrong**\n\n The correct solution is:-')
        	obj1.show(sudokuAns)
                          

    def Possible(self,y, x, n,amc):
        for i in range(slen):
            if amc[y][i] == n:
                return False
        for i in range(slen):
            if amc[i][x] == n:
                return False
        box_y = (y // int(sqrt(slen))) * int(sqrt(slen))
        box_x = (x // int(sqrt(slen))) * int(sqrt(slen))
        for i in range(int(sqrt(slen))):
            for j in range(int(sqrt(slen))):
                if amc[box_y + i][box_x + j] == n:
                    return False
        return True


    def solve(self,abc):
        global flag1
        if flag1==0:
            for y in range(slen):
                for x in range(slen):
                    if abc[y][x] == 0:
                    	for n in range(1, slen+1):
                    		if sudoBrain_.Possible(self,y,x,n,abc):
                    		    abc[y][x] = n
                    		    sudoBrain_.solve(self,abc)
                    		    if x!=slen-1 and y!=slen-1:
                    		    	abc[y][x] = 0
                    		    if x==slen-1 and y==slen-1 and abc[slen-1][slen-1]!=0:
                    		    	flag1=1
                    		    	for i in range(slen):
                    		    		for j in range(slen):
                    		    			sudokuAns[i][j]=abc[i][j]                   		    							
                    	return
	
   
    def isValid(self,y,x,n):
    	global sudokuInput
    	for i in range(1,slen-x):
    		if sudokuInput[y][x+i]==n:
    			return False
    		for i in range(1,slen-y):
    			if sudokuInput[y+i][x]==n:
    				return False
    		box_y = (y // int(sqrt(slen))) * int(sqrt(slen))
    		box_x = (x // int(sqrt(slen))) * int(sqrt(slen))
    		for i in range(int(sqrt(slen))):
    			for j in range(int(sqrt(slen))):
    			    if sudokuInput[box_y+i][box_x+j]==n:
    			    	if(((box_y+i)!=y) and ((box_x+j)!=x)):
    			    		return False
    	return True
                    	
                    	
    def checkValid(self,sudokuInput):
    	global sudokuRandom,flag3,valid,cnt
    	for i in range(slen):
    		for j in range(slen):
    			if sudokuRandom[i][j]!=0:
    				cnt+=1
    				if sudokuRandom[i][j]==sudokuInput[i][j]:
    					flag3+=1
    				else:
    					flag3=0
    	if flag3==cnt:
    		for i in range(slen):
    			for j in range(slen):
    				val=sudokuInput[i][j]
    				if obj2.isValid(i,j,val):
    					valid+=1
    				else:
    					valid=0
    					return
    	else:
    		print("\n!!!**You have not used the given sudoku**!!!\n ")
		


#start
c=1
while(c>=1):         
	sudoku= []
	sudokuRandom = []
	sudokuAns=[]
	sudokuInput=[]
	valid=0
	flag=0
	flag1=0
	flag3=0
	cnt=0
	
	print('\n!! Welcome To Sudoku Challenge !!')
	slen = int(input("Which sodoku you want to solve:- "))
		
	for i in range(slen):
		sudokuAns.append([])
		for j in range(slen):
			sudokuAns[i].append(0)
	
	obj1=GetSet_()
	obj2=sudoBrain_()
	
	obj1.getRandomSudoku()
	obj2.solve(sudokuRandom)
	obj1.MakeSudoku(sudokuAns)
	
	input('If you want to check your solution is  correct or not "Press Entre"')
	obj2.check(sudokuAns)
	
	print('******************************************')
	#input('\n Do you want to solve another ("Y" for YES and "N" for NO ')
	c+=1
	c=int(input('Do you yant to solve another sudoku (" 1 " for YES " 0 " for NO")'))
	
	
		

print('\n      Thank you !! Hope you enjoyed it :)')
print('\nGame Creators: Atharva Charde,Yash Dharmale and Rutika Kale')


#Generates Sudoku puzzles
import random
global incomplete
incomplete=True
class cell: 
	stage=[[0,0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
	def __init__(self,list1,list2):
		self.list1=list1
		self.list2=list2
		self.group=[]
	
		for i in self.list1:
			for j in self.list2:
				self.group.append(cell.stage[i][j])
	def validchk(self):
		megacall()
		temp=[]
		for i in range(1,10):
			if i not in self.group:
				temp.append(i)	
		if temp==[]:
			return True
		else:
			return temp
	def __str__(self):
		string=str(self.group)
		return string			
def incomplete():
	for i in cell.stage:
		for j in i:
			if j==0:
				return True
	print"returning false"
	return False
def randomValue(ar):
	val = random.randint(0,len(ar)-1)
	return ar[val]
def randomLocations():
	a=[[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [2, 0], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [3, 0], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [3, 6], [3, 7], [3, 8], [4, 0], [4, 1], [4, 2], [4, 3], [4, 4], [4, 5], [4, 6], [4, 7], [4, 8], [5, 0], [5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7], [5, 8], [6, 0], [6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [6, 6], [6, 7], [6, 8], [7, 0], [7, 1], [7, 2], [7, 3], [7, 4], [7, 5], [7, 6], [7, 7], [7, 8], [8, 0], [8, 1], [8, 2], [8, 3], [8, 4], [8, 5], [8, 6], [8, 7], [8, 8]]
	temp=[]
	while len(a) != 0:
		rno=random.randint(0,len(a)-1)
		temp.append(a.pop(rno))
	return temp
def generator(gr1s,gr2s,gr3s):
	n=0
	array=randomLocations()
	for i in array:
		n+=1
		options=getoptions(i[0],i[1])
		if options==[]:
			print"GENERATOR FAILED. PLEASE TRY AGAIN"
		elif n>= 15:
			print""
			return(cell.stage)
		cell.stage[i[0]][i[1]]=randomValue(options)
		megacall()		
	return cell.stage
def printer(stage1):
	stage=list(stage1)
	addit=""
	printstr=""
	for i in range(9):
		for j in range(9):
			if stage[i][j]==0:
				addit=" "
			else:
				addit=str(stage[i][j])
			printstr=printstr+ "| "+addit + "  "
			if j == 2 or j ==5:
				printstr+="#"
		printstr+= "|\n"
		if i == 2 or i == 5:
			printstr+= "# # # # # # # # # # # # # # # # # # # # # # # # #  \n"
	print printstr
	print          "___________________________________________________________________________"
def getoptions(i,j):
	gr1s=grOFgr1
	gr2s=grOFgr2
	gr3s=grOFgr3
	table=[[111, 112, 113, 214, 215, 216, 317, 318, 319], [121, 122, 123, 224, 225, 226, 327, 328, 329], [131, 132, 133, 234, 235, 236, 337, 338, 339],[441, 442, 443, 544, 545, 546, 647, 648, 649], [451, 452, 453, 554, 555, 556, 657, 658, 659], [461, 462, 463, 564, 565, 566, 667, 668, 669],[771, 772, 773, 874, 875, 876, 977, 978, 979], [781, 782, 783, 884, 885, 886, 987, 988, 989], [791, 792, 793, 894, 895, 896, 997, 998, 999]]
	optCode=str(table[i][j])
	code1=int(optCode[0])
	code2=int(optCode[1])
	code3=int(optCode[2])
	options1=gr1s[code1-1].validchk()
	megacall()
	options2=gr2s[code2-1].validchk()
	megacall()
	options3=gr3s[code3-1].validchk()
	megacall()
	finaloptions=[]
	for i in range(1,10):
		if i in options1 and i in options2 and i in options3:
			finaloptions.append(i)
	return finaloptions
def megacall():
	print".",
	g1=[0,1,2]
	g2=[3,4,5]
	g3=[6,7,8]
	nos=[0,1,2,3,4,5,6,7,8]
	gr11=cell(g1,g1)
	gr12=cell(g1,g2)
	gr13=cell(g1,g3)
	gr14=cell(g2,g1)
	gr15=cell(g2,g2)
	gr16=cell(g2,g3)
	gr17=cell(g3,g1)
	gr18=cell(g3,g2)
	gr19=cell(g3,g3)
	gr21=cell([0],nos)
	gr22=cell([1],nos)
	gr23=cell([2],nos)
	gr24=cell([3],nos)
	gr25=cell([4],nos)
	gr26=cell([5],nos)
	gr27=cell([6],nos)
	gr28=cell([7],nos)
	gr29=cell([8],nos)
	gr31=cell(nos,[0])
	gr32=cell(nos,[1])
	gr33=cell(nos,[2])
	gr34=cell(nos,[3])
	gr35=cell(nos,[4])
	gr36=cell(nos,[5])
	gr37=cell(nos,[6])
	gr38=cell(nos,[7])
	gr39=cell(nos,[8])
	global grOFgr1
	global grOFgr2
	global grOFgr3
	grOFgr1=[gr11,gr12,gr13,gr14,gr15,gr16,gr17,gr18,gr19]
	grOFgr2=[gr21,gr22,gr23,gr24,gr25,gr26,gr27,gr28,gr29]
	grOFgr3=[gr31,gr32,gr33,gr34,gr35,gr36,gr37,gr38,gr39]
megacall()
global grOFgr1
global grOFgr2
global grOFgr3
printer(generator(grOFgr1,grOFgr2,grOFgr3))

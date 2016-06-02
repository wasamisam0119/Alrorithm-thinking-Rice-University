import time
def maxRNA(rna):
	
	length=len(rna)
	mat=[[0 for j in range(length-4)] for i in range(length-4)]
	for k in range(5,length):
		for i in range(0,length-k):
			j=i+k
			#print j
			#print i
			l=[0]
			count=0	
			for t in range(i,j):				
				if (rna[t]==rna[j]) and (j-t>4):									
					l.append(1+mat[i][t-1]+mat[t+1][j-6])
					#print l
				else:		
					count+=1								
			if (count == j-i):
				#print "hello"
				mat[i][j-5]=mat[i][j-6]
				#print mat[i][j-5]
			else:				
				#print "mat[%d][%d] = %d"%(i,j,max(l))
				mat[i][j-5]=max(l)
	
	return mat[0][length-6]

start =time.clock()
print maxRNA("QWERTYUIOPASDFGHJKLZXCVBNMQWERTYUIOPASDFGHJKLZXCVBNMQWERTYUIOPASDFGHJKLZXCVBNMQWERTYUIOPASDFGHJKLZXCVBNMQWERTYUIOPASDFGHJKLZXCVBNMQWERTYUIOPASDFGHJKLZXCVBNM1234567890QAZWSXEDCRFVTGBYHNUJMASDFGHJKLQWERTYUIOPZXCVBNMHIJKMNBVCXZPOIUYTREWQSLKJHGFDSAMJUNHYBGTVFRCDEXSWZAQ0987654321MNBVCXZLKJHGFDSAPOIUYTREWQMNBVCXZLKJHGFDSAPOIUYTREWQMNBVCXZLKJHGFDSAPOIUYTREWQMNBVCXZLKJHGFDSAPOIUYTREWQMNBVCXZLKJHGFDSAPOIUYTREWQMNBVCXZLKJHGFDSAPOIUYTREWQ")
end = time.clock()
print('Running time: %s Seconds'%(end-start))




class Part1:

	def total_cost(self, NY, SF, n, M):

		temp_NY = [0] * n
		temp_SF = [0] * n

		for i in range(n):

			temp_NY[i] = NY[i] + min(temp_NY[i - 1], M + temp_SF[i - 1])
			temp_SF[i] = SF[i] + min(temp_SF[i - 1], M + temp_NY[i - 1])


		return min(temp_SF[n - 1],temp_NY[n- 1])


class Part2:
	def printMaxActivities(self, s, f):


		f,s = zip(*sorted(zip(f,s)))

		print("Start  :  ", s)
		print("Finish  :  ", f)

		n = len(f)
		print ("Optimal list of sessions  :  " , end = " ")

		i = 0
		print (i, end = " ")

		for j in range(n):
			if s[j] >= f[i]:
				print (j, end = " ")
				i = j

		print()


class Part3:

	def Subset_zero(self,index, sum_of_subarr, arr, size_of_arr, visit, dp, temp):

		if (index == size_of_arr) : 
			if (sum_of_subarr == 0) : 
				print(temp)
				return -1
			else : 
				return 0 

		if (visit[index][sum_of_subarr + size_of_arr]) : 
			return dp[index][sum_of_subarr + size_of_arr]

		visit[index][sum_of_subarr + size_of_arr] = 1;  

		temp.append(arr[index])

		dp[index][sum_of_subarr + size_of_arr ] = self.Subset_zero(index + 1, sum_of_subarr + arr[index], arr, size_of_arr, visit, dp, temp) 
		
		temp.remove(arr[index])

		if dp[index][sum_of_subarr + size_of_arr ] == -1:
			return -1

		dp[index][sum_of_subarr + size_of_arr ] += self.Subset_zero(index + 1, sum_of_subarr, arr, size_of_arr, visit, dp, temp)

		return dp[index][sum_of_subarr + size_of_arr]




class Part4:

	
	def getMin(self, word_1, word_2, mistmatch, gap, match):
	   
	    number_1 = 0
	    number_2 = 0
	    gapNum = 0
	    mistmatchNum = 0
	    matchNum = 0
	    
	    arr = []

	    for row in range(len(word_1) + len(word_2) + 1):
	        arr += [[0] * (len(word_1) + len(word_2) + 1)]

	    for i in range(len(word_1) + len(word_2)):
	        arr[i][0] = i * gap
	        arr[0][i] = i * gap
	        
	    for i in range(1,len(word_1) + 1):
	        for j in range(1, len(word_2) + 1):
	            if word_1[i-1] == word_2[j-1]:
	                arr[i][j] = arr[i-1][j-1]
	            else:
	                arr[i][j] = min(arr[i-1][j-1] + mistmatch,
	                     arr[i-1][j] + gap,
	                     arr[i][j-1] + gap)
	                
	    sum_len = len(word_1) + len(word_2)

	    i = len(word_1)
	    j = len(word_2)
	    
	    position_1 = sum_len
	    position_2 = sum_len
	    

	    answer_1 = [0] * (sum_len + 1)
	    answer_2 = [0] * (sum_len + 1)
	    
	    while not (i == 0 or j == 0):
	        
	        if word_1[i-1] == word_2[j-1]:
	            
	            answer_1[position_1] = ord(word_1[i-1])
	            answer_2[position_2] = ord(word_2[j-1])
	            
	            position_1 -= 1
	            position_2 -= 1
	            
	            i -= 1
	            j -= 1 
	            
	            number_1 += 1
	            number_2 += 1
	            matchNum += 1

	        elif arr[i-1][j-1] + mistmatch == arr[i][j]:
	            
	            answer_1[position_1] = ord(word_1[i-1])
	            answer_2[position_2] = ord(word_2[j-1])
	            
	            position_1 -= 1
	            position_2 -= 1
	            
	            i -= 1
	            j -= 1 
	            
	            number_1 += 1
	            number_2 += 1
	            mistmatchNum += 1

	        elif arr[i-1][j] + gap == arr[i][j]:
	           
	            answer_1[position_1] = ord(word_1[i-1])
	            answer_2[position_2] = ord('_')
	           
	            position_2 -= 1
	            position_1 -= 1
	           
	            i -= 1 
	            number_1 += 1
	           
	            if j < len(word_2):
	                number_2 += 1
	                gapNum += 1
	        
	        elif arr[i][j-1] + gap == arr[i][j]:
	        
	            answer_1[position_1] = ord('_')
	            answer_2[position_2] = ord(word_2[j-1])
	        
	            position_1 -= 1
	            position_2 -= 1
	        
	            j -= 1
	            number_2 += 1
	        
	            if i < len(word_1):
	                number_1 += 1
	                gapNum += 1
	                
	    while position_2 > 0:
	        
	        if j > 0:
	            j -= 1
	            answer_2[position_2] = ord(word_2[j])
	        
	            number_1 += 1
	            number_2 += 1
	            gapNum += 1
	        
	        else:
	            answer_2[position_2] = ord('_')
	            
	        position_2 -= 1
	        
	    while position_1 > 0:
	       
	        if i > 0:
	            i -= 1
	            answer_1[position_1] = ord(word_1[i])
	       
	            number_1 += 1
	            number_2 += 1
	            gapNum += 1
	       
	        else:
	            answer_1[position_1] = ord('_')

	        position_1 -= 1
	        
	    temp = 1

	    for i in range(sum_len,0,-1):
	        if chr(answer_2[i]) == '_' and chr(answer_1[i]) == '_':
	            temp = i + 1
	            break

	    cost = matchNum * match + gapNum * -gap + mistmatchNum * -mistmatch

	    return answer_1[temp:temp+number_1], answer_2[temp:temp+number_2], cost



class Part5:
	def min_number_op(self,arr):

		sum_of_arr = 0
		op = 0

		temp_neg = []
		temp_pos = []

		for i in range(len(arr)):

			if arr[i] < 0:
				temp_neg.append(arr[i])
			else:
				temp_pos.append(arr[i])


		temp_neg.sort(reverse= True)
		temp_pos.sort()

		i = 0
		j = 0

		while i < len(temp_neg) and j < len(temp_pos):

			if temp_pos[j] > (0 - temp_neg[i]):

				if i != 0 or j != 0:

					if sum_of_arr < 0:
						op += (-1) * (temp_neg[i] + sum_of_arr)
					else:
						op +=  sum_of_arr - temp_neg[i]

				sum_of_arr += temp_neg[i]
				i += 1

			else:

				if i != 0 or j != 0:

					if sum_of_arr < 0:
						op += temp_pos[j] - sum_of_arr
					else:
						op += sum_of_arr + temp_pos[j]

				sum_of_arr += temp_pos[j]
				j += 1

		if i < len(temp_neg):
			while i < len(temp_neg):

				if i != 0 or j != 0:

					if sum_of_arr < 0:
						op += (-1) * (temp_neg[i] + sum_of_arr)
					else:
						op += sum_of_arr - temp_neg[i]

				sum_of_arr += temp_neg[i]
				i += 1

		else:

			while j < len(temp_pos):

				if i != 0 or j != 0:

					if sum_of_arr < 0:
						op += temp_pos[j] - sum_of_arr
					else:
						op += sum_of_arr + temp_pos[j]

				sum_of_arr += temp_pos[j]
				j += 1


		return sum_of_arr, op


def main():

#######################################    Part 1    #######################################

	print("#######################################    Part 1    #######################################\n")

	NY = [1, 3, 20, 30]
	SF = [50, 20, 2, 4]

	n = 4
	M = 10

	part1 = Part1()

	print ("Example 1:")
	print("List 1 : ", NY)
	print("List 2 : ", SF)
	print("M value : ", M)
	print("Cost of an optimal plan  :  ", part1.total_cost(NY,SF, n, M))
	print()

	NY = [1, 100, 1, 100, 1, 100]
	SF = [100, 1, 100, 1, 100, 1]

	n = 6
	M = 15

	print("Example 2:")
	print ("List 1 : ",NY)
	print ("List 2 : ",SF)
	print ("M value : ",M)
	print("Cost of an optimal plan  :  ", part1.total_cost(NY, SF, n, M))
	print("\n")

	

#######################################    Part 2    #######################################

	
	print("#######################################    Part 2    #######################################\n")


	part2 = Part2()

	s = [1, 3, 0, 5, 8, 5]
	f = [2, 4, 6, 7, 9, 9]


	print("Example 1:")

	part2.printMaxActivities(s, f)

	print()

	s = [1, 2, 5, 3, 1, 0]
	f = [9, 3, 7, 4, 2, 6]


	print("Example 2:")
	part2.printMaxActivities(s, f)


	print("\n")
	

#######################################    Part 3    #######################################
	
	print("#######################################    Part 3    #######################################\n")

	print ("Example 1:")

	part3 = Part3()


	arr = [-2,3,-3,5,4]
	visit = []
	temp = []
	dp = []
	
	maxSum = 1000



	for row in range(len(arr)): dp += [[0] * maxSum]

	for row in range(len(arr)): visit += [[0] * maxSum]

	print("Array  :  ")
	print (arr)

	print("Subarray  :  ")
	part3.Subset_zero(0, 0, arr, len(arr), visit, dp, temp)
	
	print()

	print ("Example 2:")

	arr = [-1, 6, 4, 2, 3, -7, -5]
	visit = []
	temp = []
	dp = []

	for row in range(len(arr)): dp += [[0] * maxSum]

	for row in range(len(arr)): visit += [[0] * maxSum]
	print("Array  :  ")
	print (arr)
	print("Subarray  :  ")
	part3.Subset_zero(0, 0, arr, len(arr), visit, dp, temp)

	print()

	print("\n")

#######################################    Part 4    #######################################

	print("#######################################    Part 4    #######################################\n")


	part4 = Part4()

	print ("Example 1:")

	word1 = "ALIGNMENT"
	word2 = "SLIME"

	misMatchPenalty = 2
	gapPenalty = 1
	match = 2

	print("First word  :  ALIGNMENT")
	print("Second word  :  SLIME")
	print("Match score  :  ", 2)
	print("Mistmatch score  :  ", -2)
	print("Gap score  :  ", -1)

	arr1, arr2, cost = part4.getMin(word1, word2, misMatchPenalty, gapPenalty, match)

	print("\nOutput  :  ")

	for i in range(len(arr1)):
	    print(chr(arr1[i]),end=" ")

	print()
	    
	for i in range(len(arr2)):
		print(chr(arr2[i]),end=" ")

	print ("\n\nCost  :  ", cost)

	print("\nExample 2:")


	print("First word  :  Nurullah")
	print("Second word  :  urah")
	print("Match score  :  ", 2)
	print("Mistmatch score  :  ", -2)
	print("Gap score  :  ", -1)
	
	word1 = "Nurullah"
	word2 = "urah"

	arr1, arr2, cost = part4.getMin(word1, word2, misMatchPenalty, gapPenalty, match)

	print("\nOutput  :  ")

	for i in range(len(arr1)):
	    print(chr(arr1[i]),end=" ")

	print()
	    
	for i in range(len(arr2)):
		print(chr(arr2[i]),end=" ")


	print()
	print ("\nCost  :  ", cost)

	print("\n")


#######################################    Part 5    #######################################

	

	print("#######################################    Part 5    #######################################\n")

	arr = [5, -3, 4,2,-6,-10,1]

	part5 = Part5()


	print("Example 1:")
	print("List  : ", arr)

	s, op = part5.min_number_op(arr)

	print("Sum of the array  :  ",s)
	print("Number of operations  :  ",op)
	print()

	arr = [6,8,19,2,5,7,8]

	print ("Example 2:")
	print("List  : ", arr)
	s, op = part5.min_number_op(arr)

	print("Sum of the array  :  ", s)
	print("Number of operations  :  ", op)

	

if __name__ == '__main__':
	main()

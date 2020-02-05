#############################   PART 1   #############################

class Part1:
    class b:

        def convert_special_array(self,arr):

            temp = []

            change_num = 0

            for i in range(len(arr) - 1):
                new = []
                for j in range(len(arr[i]) - 1):
                    val = (arr[i][j] + arr[i + 1][j + 1]) - (arr[i][j + 1] + arr[i + 1][j])
                    new.append(val)

                    if val > 0:
                        change_num += 1

                temp.append(new)

            if change_num == 0:
                return arr, 2

            num = 0

            for i in range(len(temp)):
                for j in range(len(temp[i])):
                    if temp[i][j] > 0:
                        if self.__helper(temp[i][j], i, j, arr):
                            if num == 0:
                                num += 1
                            else:
                                return arr, 0
                        else:
                            return arr, 0

            return arr, 1


        def __helper(self, value, i, j, arr):

            if self.__check(arr, i, j, value * (-1)):
                arr[i][j] -= value
                return True

            if self.__check(arr, i, j + 1, value):
                arr[i][j + 1] += value
                return True

            if self.__check(arr, i + 1, j, value):
                arr[i + 1][j] += value
                return True

            if self.__check(arr, i + 1, j + 1, value * (-1)):
                arr[i + 1][j + 1] -= value
                return True


            return False


        def __check(self, arr, i, j, value):

            if i - 1 >= 0 and j - 1 >= 0:  #sol ust capraz
                if ( arr[i - 1][j - 1] + (arr[i][j] + value) ) - ( arr[i - 1][j] + arr[i + 1][j - 1] ) > 0:
                    return False

            if i + 1 < len(arr) and j + 1 < len(arr[0]):   #sag alt capraz
                if ( arr[i + 1][j + 1] + (arr[i][j] + value) ) - ( arr[i + 1][j] + arr[i][j + 1] ) > 0:
                    return False

            if i + 1 < len(arr) and j - 1 >= 0:   # sol alt capraz
                if ( arr[i + 1][j - 1] + (arr[i][j] + value) ) - ( arr[i][j - 1] + arr[i + 1][j - 1] ) < 0:
                    return False

            if i - 1 >= 0 and j + 1 < len(arr[0]):   #sag ust capraz
                if ( arr[i - 1][j + 1] + (arr[i][j] + value) ) - ( arr[i - 1][j] + arr[i][j + 1] ) < 0:
                    return False

            return True
    

    class c:

        def find_leftmost_min(self, special_arr):

            index = []

            for i in range(len(special_arr)):
                index.append(i)

            if len(special_arr) == 1:
                self.__find_row_leftmost_min(special_arr,index,[0])
                return index

            odd = len(special_arr) % 2

            even_rows, even_index = self.__find_even_and_odd_rows(special_arr[:len(special_arr) - 1], index[:len(index) - 1], [], [], 0, odd)
            odd_rows, odd_index = self.__find_even_and_odd_rows(special_arr, index, [], [], 1, odd)

            self.__find_row_leftmost_min(even_rows, index, even_index)
            self.__find_row_leftmost_min(odd_rows, index, odd_index)

            return index


        def __find_row_leftmost_min(self, special_arr, left_mosts, index):

            if len(special_arr) == 0:
                return left_mosts

            leftMost = special_arr[0][0]

            for i in range(len(special_arr[0])):
                if leftMost > special_arr[0][i]:
                    leftMost = special_arr[0][i]

            left_mosts[index[0]] = leftMost

            self.__find_row_leftmost_min(special_arr[1:], left_mosts ,index[1:])


        def __find_even_and_odd_rows(self, special_arr, index,  even_odd_row, ind, type, odd):

            if len(special_arr) - (type + 1) >= 0:
                even_odd_row.append(special_arr[len(special_arr) - 1])
                ind.append(index[len(index) - 1])
                self.__find_even_and_odd_rows(special_arr[:-2], index[:-2], even_odd_row, ind, type, odd)

            if type == 1 and odd == 1 and len(special_arr) - (type + 1) == -1:
                even_odd_row.append(special_arr[len(special_arr) - 1])
                ind.append(index[len(index) - 1])

            return even_odd_row, ind

#############################   PART 2   #############################

class Part2:

    def kth_element(self, arr1, arr2, k, arr1_index, arr2_index):
        if arr1_index == len(arr1):
            return arr2[arr2_index + k - 1]

        if arr2_index == len(arr2):
            return arr1[arr1_index + k - 1]

        if (k == 0) or (k > (len(arr1) - arr1_index) + (len(arr2) - arr2_index)):
            return -1

        if k == 1:
            return arr1[arr1_index] if (arr1[arr1_index] < arr2[arr2_index]) else arr2[arr2_index]

        size = k // 2

        if size - 1 >= len(arr1) - arr1_index:
            return arr2[arr2_index + (k - (len(arr1) - arr1_index) - 1)] if arr1[len(arr1) - 1] < arr2[arr2_index + size - 1] else self.kth_element(arr1, arr2, k - size, arr1_index, arr2_index + size)

        if size - 1 >= len(arr2) - arr2_index:
            return arr1[arr1_index + (k - (len(arr2) - arr2_index) - 1)] if arr2[len(arr2) - 1] < arr1[arr1_index + size - 1] else self.kth_element(arr1, arr2, k - size, arr1_index + size, arr2_index)

        else:
            return self.kth_element(arr1, arr2, k - size, arr1_index + size, arr2_index) if arr1[size + arr1_index - 1] < arr2[size + arr2_index - 1] else self.kth_element(arr1, arr2, k - size, arr1_index, arr2_index + size)

#############################   PART 3   #############################


class Part3:


    def find_contiguous_subset(self, arr):
        if not arr:
            return None

        start, end = self.__helper(arr, 0, len(arr) - 1)

        return arr[start:end + 1]


    def __helper(self, arr, start, end):

        if start == end:
            return (start, end)

        middle = (start + end) // 2

        left = self.__helper(arr, start, middle)

        right = self.__helper(arr, middle + 1, end)

        return self.__combine(arr, left, right)


    def __combine(self, arr, left, right):

        sum_of_left = sum(arr[left[0]:left[1] + 1])

        sum_of_right = sum(arr[right[0]:right[1] + 1])

        if (right[0] - left[1]) == 1:

            sum_left_right = sum_of_left + sum_of_right

            if sum_of_right <= sum_left_right and sum_of_left <= sum_left_right:
                return (left[0], right[1])
        else:

            sum_range = sum(arr[left[0]:right[1] + 1])

            if sum_of_right <= sum_range and sum_of_left <= sum_range:
                return (left[0], right[1])

        return right if sum_of_left < sum_of_right else left


#############################   PART 4   #############################


class Part4:

    def __helper(self,graph, color_of_vertex, position, color, vertex_num):

        if color_of_vertex[position] != -1 and color_of_vertex[position] != color:
            return False

        color_of_vertex[position] = color

        isbipartite = True

        for i in range(0, vertex_num):

            if graph[position][i] == 1:

                if color_of_vertex[i] == -1:
                    isbipartite &= self.__helper(graph, color_of_vertex, i, 1 - color, vertex_num)

                if color_of_vertex[i] != -1 and color_of_vertex[i] != 1 - color:
                    return False

            if isbipartite == False:
                return False

        return True


    def isBipartite(self, graph, vertex_num):
        color_of_vertex = [-1] * vertex_num

        return self.__helper(graph, color_of_vertex, 0, 1, vertex_num)


#############################   PART 5   #############################
class Part5:

    def best_day_buy(self, C, P):

        index = []

        for i in range(1, len(C) + 1):
            index.append(i)

        units, best_day, no_gain = self.__best_day_buy_helper(C, P, index, [])

        print("The best day to buy goods is the " + str(best_day) + " th day.")
        print("Selling day is the " + str(best_day + 1) + " th day.")
        print("Maximum possible gain is " + str(units) + ".\n")

        if len(no_gain) > 0:
            print("Days without earnings  :  ")
            for i in range(len(no_gain) - 1):
                print(no_gain[i])


    def __best_day_buy_helper(self,C, P, index, no_gain):

        if len(C) == 1 or len(P) == 1:      #if arrays size equal to 1 return price - cost and day
            if P[0] - C[0] <= 0:            #if there is no gain in that day print to screen no gain in that day
                no_gain.append("In the "+ str(index[0] + 1)+" th day there is no make money.")

            return P[0] - C[0], index[0], no_gain

        elif len(C) == 0 or len(P) == 0:
            return 0, 0, no_gain         #if arrays size equal to 0 return 0

        left_C = C[: len(C) // 2]
        right_C = C[len(C) // 2:]       #arrays are divided two parts

        left_P = P[: len(P) // 2]
        right_P = P[len(P) // 2:]

        left_indexes = index[: len(index) // 2]
        right_indexes = index[len(index) // 2:]

        leftBest, indleft, no_gain = self.__best_day_buy_helper(left_C, left_P, left_indexes, no_gain)        #call function for left part
        rightBest, indright, no_gain = self.__best_day_buy_helper(right_C, right_P, right_indexes, no_gain)   #call function for right part


        if leftBest > rightBest:        #return gain which is bigger than others
            return leftBest, indleft, no_gain
        else:
            return rightBest, indright, no_gain


class Example:

    def part_1(self, arr):

        print("Input array  : ")

        for i in range(len(arr)):
            print(arr[i])


        part1 = Part1()
        c = part1.c().find_leftmost_min(arr)

        b, num = part1.b().convert_special_array(arr)



        if num == 1:
            print("\nInput array is converted to special array.")
            print("Output  :  ")
            for i in range(len(b)):
                print(b[i])
        elif num == 2:
            print("\nInput array is already special array.")
        else:
            print("\nInput array can't be special array.")


        print("\nLeft most elements of input array  :  ", c, "\n")

    def part_2(self, arr1, arr2, k):

        part2 = Part2()

        print("First array  :  ", arr1)
        print("Second array  :  ", arr2)
        print(k, "th element  :  ", part2.kth_element(arr1, arr2, k, 0, 0), "\n")

    def part_3(self, arr):

        part3 = Part3()

        largest_sublist = part3.find_contiguous_subset(arr)
        print("Input array  :  ", arr)
        print("The largest contiguous subset for largest sum= ", largest_sublist, ", Sum =", sum(largest_sublist), "\n")

    def part_4(self, graph, vertex_num):

        part4 = Part4()

        print("Input graph  :  ")
        for i in range(len(graph)):
            print(graph[i])

        if part4.isBipartite(graph, vertex_num):
            print("\nYes, it is bipartite.\n")
        else:
            print("\nNo, it isn't bipartite.\n")

    def part_5(self, C, P):

        print("Cost:    ", C)
        print("Price:   ", P, "\n")

        part5 = Part5()

        part5.best_day_buy(C, P)

        print("\n")



def main():

    example =Example()

    #############################   PART 1   #############################

    print("------------------------   PART 1   ------------------------\n")

    arr = [[37, 23, 22, 32],
           [21, 6, 7, 10],
           [53, 34, 30, 31],
           [32, 13, 9, 6],
           [43, 21, 15, 8]]


    arr2 = [[10, 17, 13, 28, 23],
            [17, 22, 16, 29, 23],
            [24, 28, 22, 34, 24],
            [11, 13, 6, 17, 7],
            [45, 44, 32, 37, 23],
            [36, 33, 19, 21, 6],
            [75, 66, 51, 53, 34]]


    arr3 = [[37, 21, 53, 32, 43],
            [23, 6, 34, 13, 21],
            [22, 7, 30, 9, 15],
            [32, 10, 31, 6, 8],
            [15, 15, 30, 9, 15],
            [47, 7, 30, 9, 15]]

    example.part_1(arr)
    example.part_1(arr2)
    example.part_1(arr3)



 #############################   PART 2   #############################

    print("------------------------   PART 2   ------------------------\n")


    arr1 = [2, 3, 6, 7, 9]
    arr2 = [1, 4, 8, 10]
    k1 = 5

    arr3 = [0, 2, 9, 13, 17, 25, 61]
    arr4 = [2, 3, 4, 8, 10, 11]
    k2 = 8

    arr5 = [0, 1, 5, 9, 18, 23, 54]
    arr6 = [4, 6, 7, 22, 123]
    k3 = 7


    example.part_2(arr1, arr2, k1)
    example.part_2(arr3, arr4, k2)
    example.part_2(arr5, arr6, k3)


    #############################   PART 3   #############################

    print("------------------------   PART 3   ------------------------\n")

    arr = [5, -6, 6, 7, -6, 7, -4, 3]
    arr1 = [15, -6, -6, 12, 0, 7, -5, 3, 14]
    arr2 = [1, 2, -5, 10, -13, 12, 7, 1]

    example.part_3(arr)
    example.part_3(arr1)
    example.part_3(arr2)

    #############################   PART 4   #############################

    print("------------------------   PART 4   ------------------------\n")

    graph1 = [[0, 1, 0, 1],
              [1, 0, 1, 0],
              [0, 1, 0, 1],
              [1, 0, 1, 0]]

    vertex_num_1 = 4

    graph2 = [[1, 0, 1, 0],
              [0, 1, 0, 1],
              [1, 0, 1, 0],
              [0, 1, 0, 1]]

    vertex_num_2 = 4


    graph3 = [[0, 1, 0, 0, 0, 1],
              [1, 0, 1, 0, 0, 0],
              [0, 1, 0, 1, 0, 0],
              [0, 0, 1, 0, 1, 0],
              [0, 0, 0, 1, 0, 1],
              [1, 0, 0, 0, 1, 0]]

    vertex_num_3 = 6

    example.part_4(graph1, vertex_num_1)
    example.part_4(graph2, vertex_num_2)
    example.part_4(graph3, vertex_num_3)

        #############################   PART 5   #############################

    print("------------------------   PART 5   ------------------------\n")

    C = [5, 11, 2, 21, 5, 7, 8, 12, 13]
    P = [7, 9, 5, 21, 7, 13, 10, 14, 20]

    C1 = [15, 11, 22, 21, 5, 30, 18, 2, 3]
    P1 = [7, 9, 5, 21, 7, 13, 10, 14, 20]

    C2 = [2, 19, 12, 11, 5, 17, 18, 12, 31]
    P2 = [7, 9, 5, 21, 7, 13, 10, 14, 20]

    example.part_5(C, P)
    example.part_5(C1, P1)
    example.part_5(C2, P2)



if __name__ == '__main__':
    main()

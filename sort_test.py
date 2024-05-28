
import random

class SortArray:
    def arrag_arry(self, num1, num2):
        length_num1 = len(num1)
        length_num2 = len(num2)
        
        # If num1 is shorter, append random numbers to num1
        while length_num1 < length_num2:
            random_num = random.randint(1, 10)
            num1.append(random_num)
            length_num1 += 1
        
        # If num2 is shorter, append random numbers to num2
        while length_num2 < length_num1:
            random_num = random.randint(1, 10)
            num2.append(random_num)
            length_num2 += 1

        num = []

        # Compare elements and append the greater one to the result list
        for e in range(length_num1):
            if num1[e] >= num2[e]:
                num.append(num1[e])
            else:
                num.append(num2[e])

        return num

# Initialize the parameters
m = 3
n = 3
num1 = [5, 6, 7, 0, 0, 0]
num2 = [3, 5, 7, 4, 9, 10]

# Create an instance of the class
sorter = SortArray()
# Call the method and get the result
result = sorter.arrag_arry(num1, num2)
# Print the result
print(result)

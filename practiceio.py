"""inputFile = open("data.txt", "r")
for line in inputFile:
    print(line)
inputFile.close()"""


str_temp = "ABCDE"
int_temp = 5 
with open ("new-file.txt", "w")  as file:
    file.write(str_temp + "\n" +str(int_temp))
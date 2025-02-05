fp = open("text.txt")
print(fp.read())  #you need this to print the entire content of the file
fp.close() #this is used to close the file (it is still there), if you want to use the file again, you need to run it from the beginning with the first 2 lines of code I have written.

#this is a good way to open the file, but it is not the "pythonic" way.
# same exact thing with context manager
with open("text.txt") as fp:
    print(fp.read())
#this method is better because you do not need to use "fp.close()", it closes after you run the file automatically.

#let's read from the same file, but line by line now
print("Read the file line by line")
with open("text.txt") as fp:
    for line in fp: #we iterate over the file, line by line
        print(line)
        #or
        print(line, end= "")  # this asks the print to not add a new line (so the "done printing" will be on the same line as the previous text)

print("Done printing...")


#Now we do it again but with a string
print("Read the fine line by line")
line_number = 1
with open("text.txt") as fp:
    for line in fp:
        print(f"{line_number}: {line}", end="")
        line_number += 1

print("done printing blud")
#This adds numbers to each row, from 1-5 (we used the string "f""

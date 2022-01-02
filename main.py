# Variables - a way of storing data or information you can retrieve later
text = 'Hello World'
one = 1
two = 2


# Functions - help you define code that you can reuse multiple times
# Below is the structure of a function
# def functionName:
#     Action
#     return Output

# This function prints out the input passed to it
def display(input_text):
    print(input_text)


# This function adds 1 to the parameter passed to it
def addOne(input_text1):
    output = input_text1 + 1
    return output


# If statements - when a specific condition is met an action is executed
# Structure of an if statement
# if condition:
#   Action
if two > one:
    output = addOne(two)
    display("Output = " + str(output))


# Lists - mutable data type which means the elements in a list can be changed.
# Lists can contain multiple data types like strings, int, float, sub lists
# ListStructure = []
testList = ["element1", "element2", "element3"]
testList1 = [0, 1, 2]
testList2 = ["weather", 10, 0.6, [40, 41, 42]]


display(text)
display(addOne(one))
display(two)

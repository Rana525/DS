# first we take string like my name is Rana
string="Rana"
len_of_string=len(string)

#now we find the length of string to iterate the string

target="n"


#here we give the target value "n"

#now we create the function and give the arguments


def linear_srch_string(string,target):

    #here we check the there is any string given or not
    if len_of_string==0:
        return "string does not exist"

    #if any string is given the its come here and one bye one its match to the target value
    for i in range(len_of_string):
        if string[i]==target:
            return "n found at",i

    #this return is for if charecter does not found then its return
    return "char does not found"

# Now we call the function 
print(linear_srch_string(string,target))


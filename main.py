d,j,k=0,0,0
email=input("Enter your email : ")
if len(email)>=6: #Condition 1
    if email[0].isalpha(): #Condition 2
        if "@" in email and (email.count("@")==1): #Condition 3
            if (email[-4]==".") ^ (email[-3]=="."): #Condition 4
                for i in email: #Condition 5
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1
                if k==1 or j==1 or d==1:
                    print("Invalid email format!")
                else:
                    print("Valid email format!") #Correct Email
            else:
                print("Email must ends with .com, .in etc!")
        else:
            print("Email must contain '@' & only one time!")
    else:
        print("First letter of email should be alphabet!")
else:
    print("Minimum length of email should be 6 characters!")
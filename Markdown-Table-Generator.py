print("**** Welcome to Markdown Table Generator ****")
print("Press 1 : If you already have a csv file :")
print("Press 2 : If you want to create a table :")
ch = input("> ")

if ch=='1':
    name = input("Enter a csv file name: ")
    center=input("Do you want items to be centered? (true/false): ")
    input_file = open(f"{name}.csv", "r")
    output_file = open("table.md", "w")
    
    i=0
    for line in input_file:
        arr = line.split(",")
        j=0
        if i==0:                        # For headings
            for each in arr:
                if j==len(arr)-1:
                    each = each.rstrip('\n')
                    entry= f"| \t{each}\t | \n"
                else:
                    entry= f"| \t{each}\t "
                output_file.write(entry)
                j=j+1
            for j in range(0, len(arr)):
                if j==len(arr)-1:
                    if center=="true" and len(each)>2:
                        entry= f"| \t:{'-'*(len(each)-2)}:\t | \n"
                    else:
                        entry= f"| \t{'-'*len(each)}\t | \n"
                else:
                    if center=="true" and len(each)>2:
                        entry= f"| \t:{'-'*(len(each)-2)}:\t "
                    else:
                        entry= f"| \t{'-'*len(each)}\t "
                output_file.write(entry)
                j=j+1
        else:                        # For remaining rows
            for each in arr:
                if j==len(arr)-1:
                    each = each.rstrip('\n')
                    entry= f"| \t{each}\t | \n"
                else:
                    entry= f"| \t{each}\t"
                output_file.write(entry)
                j=j+1
        i=i+1
    input_file.close()
    output_file.close()

elif ch=='2':
    rows=int(input("Enter number of rows: "))
    cols=int(input("Enter number of columns: "))
    center=input("Do you want items to be centered? (true/false): ")
    headings=[]
    print("\nEnter the data for each cell respectively!")
    file = open("table.md", "w")
    print("Let's Generate a Table in Markdown Syntax:\n")

    for i in range(1, cols+1):
        value=input(f"Enter Heading for column{i} : ")
        if i==cols:
            entry= f"| {value} |\n"
            headings.append(value)
        else:
            entry= f"| {value} "
            headings.append(value)
        file.write(entry)
    print("Headings Received!")

    for i in range(0, cols):
        if i==cols-1:
            if center=="true" and len(headings[i])>2:
                entry= f"| :{'-'*(len(headings[i])-2)}: |\n"
            else:
                entry= f"| {'-'*len(headings[i])} |\n"
        else:
            if center=="true" and len(headings[i])>2:
                entry= f"| :{'-'*(len(headings[i])-2)}: "
            else:
                entry= f"| {'-'*len(headings[i])} "
        file.write(entry)
    print("Done!")

    for i in range(2, rows+1):
        print(f"\nEnter data for Row{i} : ")
        for j in range(1, cols+1):
            value=input(f"Row{i} Column{j} - {headings[j-1]}: ")
            if j==cols:
                entry= f"| {value} |\n"
                file.write(entry)
            else:
                entry= f"| {value} "
                file.write(entry)
    file.close()

else: 
    print("Wrong input!")

print("\nDone Succesfully! :)")
print("Now check table.md or run 'cat table.md' in terminal to copy the syntax.\n")

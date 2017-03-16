letters_1 = {0:"zero",1: "one", 2:"two", 3:"three", 4:"four", 5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
letters_2 = {10:"ten",11: "eleven",12: "twelve",13: "thirteen",14: "fourteen",15: "fifteen",16: "sixteen",17: "seventeen",18: "eighteen",19: "nineteen"}
letters_3 = {2:"twenty", 3: "thirty", 4: "forty", 5:"fifty", 6:"sixty", 7:"seventy", 8:"eighty", 9:"ninety"}

total_letters = 0
for i in range(1,1001):
    number = str(i)
    text = ""
    if len(number) == 1:
        text = letters_1[i]
    elif len(number) == 2:
        if i < 20:
            text = letters_2[i]
        else:
            text += letters_3[int(number[0])]
            if number[1] != "0":
                text += letters_1[int(number[1])]
    elif len(number) == 3:
        #Take the first digit
        text += letters_1[int(number[0])]
        text += "hundred"
        #Now the last two
        i = int(number[1:])
        if i < 20 and i > 9:
            text += "and"
            text += letters_2[i]
        elif i >= 20:
            text += "and"
            text += letters_3[int(number[1])]
            if number[2] != "0":
                text += letters_1[int(number[2])]
        elif i > 0:
            text += "and"
            text += letters_1[int(number[2])]
    else:
        text = "onethousand"

    print(text,number)

    total_letters+=len(text)

print(total_letters)

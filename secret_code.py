import random
import string


# for encoding your message

def encoding():
    # generate 3 random words
    def ram_word():
        ram=''.join(random.choices(string.ascii_letters, k=3))
        return(ram)
    #take input
    take=input("enter your message: ")

    #handling error by checking if input is str only
    if not all(char.isalpha() or char.isspace() for char in take):
        raise ValueError("invalid input you should input string only")

    # splitting str as group by words
    words=take.split()


    #here final sentence will store
    code_sen=("")

    #main logic to convert input into secret code
    for word in words:
        if(len(word)>=3):
            word_code=ram_word()+word[1:]+word[0]+ram_word()
            code_sen+=word_code+' '
        elif(len(word)==2):
            small_word_code=ram_word()+word[1]+word[0]+ram_word()
            code_sen+=small_word_code+' '
        else:
            one_letter=word
            code_sen+=one_letter+' '

    print(f"\n\nyour secret code is:\n{code_sen}")


#for decodeing your secret code

def decoding():
    # taking secret code
    sect_code=input("enter your secret code: ")  

    codes=sect_code.split()
    
    #final mesg will be stored here
    final_mesg=''

    #logic for decoding secret code
    for code in codes:
        if(len(code)==8):
            mesg_two=code[4]+code[3]
            final_mesg+=mesg_two+' '
        elif(len(code)>8):
            code.replace(code[0:3],' ')
            temp=code[3:-3]
            mesg=temp[-1]+temp[0]+temp[1:-1]
            final_mesg+=mesg+' '
        else:
            one_word=code
            final_mesg+=one_word+' '

    #printing final mesg after decoding
    print(f"\n\nyour message is:\n{final_mesg}")

                      
# layout

print("(1). message encoding\n(2). message decoding\n")
choice=int(input("choose your 1 or 2: "))
if(choice==1):
    encoding()
elif(choice==2):
    decoding()
else:
    raise ValueError("enter 1 or 2 only")   
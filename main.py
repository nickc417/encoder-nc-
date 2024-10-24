# Nicholas Chaves

def encode(num):
    encoded_num=''
    for i in num:
        digit=int(i)+3
        if digit>9:
            digit-=10
        encoded_num+=str(digit)
    return encoded_num


# Michael Ostrowski

def decode():
    pass







def main():
    num=''
    while True:
        choice=int(input('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n\nPlease enter an option: '))
        if choice==1:
            num=input('Please enter your password to encode: ')
            encoded_num=encode(num)
            print('Your password has been encoded and stored!\n')
        elif choice==2:
            print(f'The encoded password is {encoded_num}, and the original password is {decode(encoded_num)}.')
        elif choice==3:
            break

if __name__=='__main__':
    main()

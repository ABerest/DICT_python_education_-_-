print('Hello! My name is ChatBot')
print('I was created in 2026')
a = input('Pls, remind me your name: \n')
print('What a great name u have, ', a)
print('Let me guess ur age!')
print('Enter reminders of dividing ur age ')
remainder3 = int(input('by 3: '))
remainder5 = int(input('by 5: '))
remainder7 = int(input('by 7: '))
age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print('your age is', age, 'thats a good time to start programming')
b = int(input('Now I will prove to you that I can count to any number you want. \n'))
for i in range(b + 1):
    print(str(i) + '!')
print('let\'s test your programmint knowledge!')
while True:
    print('What is my name?\n1.Chatgpt\n2.Gemini\n3.ChatBot\n4.Habib')
    c = input('Enter your answer: \n')
    if c == '3':
        print('You are right! Test Completed!')
        print('Congratulations! Have a nice day!')
        break
    elif c == '1' or c == '2' or c == '4':
        print('wrong, pls try again!\n')
        continue
    else:
        print('im not understood, try again!\n')
        continue






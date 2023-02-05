
toollist=['+','-','/','*']
while True:
    number1=int(input("숫자1을 입력하세요:"))
    number2=int(input("숫자2를 입력하세요:"))
    tool=input("연산기호를 입력하세요:")
    if tool=="*":
        print(number1*number2)
    elif tool=="/" :
        print(number1/number2)
    elif tool=="+":
        print(number1+number2)
    elif tool=="-":
        print(number1-number2)
    elif tool not in toollist:
        print("호환되지 않는 성능입니다.")
    
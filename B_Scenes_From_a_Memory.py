def sum_digit(s):
    sm = 0
    for digit in s:
        sm += int(digit)
    return sm

for _ in range(int(input())):
    n = int(input())
    num = input()

    co_prime_digits = '14689'
    for digit in num:
        if digit in co_prime_digits:
            print(1,digit,sep='\n')
            break
    else:
        if num.count('2') > 1 or num.count('3') > 1 or num.count('5') > 1 or num.count('7') > 1:
            num = sorted(num)
            for i in range(n-1):
                if num[i] == num[i+1]:
                    print(2,num[i]*2,sep='\n')
                    break
        elif num[-1] == '5' or num[-1] == '2':
            print(2,num[-2]+num[-1],sep='\n')
        elif ((x:=num.find('5')) != -1 and (y:=num.find('2')) != -1) or ((x:=num.find('2')) != -1 and (y:=num.find('7')) != -1) or ((x:=num.find('5')) != -1 and (y:=num.find('7')) != -1):
            print(2,num[min(x,y)]+num[max(x,y)],sep='\n')
                    

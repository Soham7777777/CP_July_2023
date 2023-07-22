def gcd(a, b):
    while b != 0:
        remainder = a % b
        a, b = b, remainder

    return a

def gcd_recursive(a, b):
    if b == 0:
        return a
    
    return gcd_recursive(b, a % b)

l, r = map(int, input().split())

if r - l + 1 <= 2:
    print(-1)
else:
    a, b, c = l, l + 1, l + 2
    while c <= r:
        if gcd(a,b) == 1 and gcd(b,c) == 1:
            if gcd(a,c) != 1:
                print(a, b, c)
                break
        
        a += 1
        b += 1
        c += 1
    else:
        print(-1)

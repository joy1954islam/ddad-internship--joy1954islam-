def isPalRec(st, s, e):
    if (s == e):
        return True
    if (st[s] != st[e]):
        return False

    if (s < e + 1):
        return isPalRec(st, s + 1, e - 1)

    return True


def isPalindrome(st):
    n = len(st)
    if (n == 0):
        return True

    return isPalRec(st, 0, n - 1);


# Driver Code 
st = input()
st = st.lower()
if (isPalindrome(st)):
    count = len(st)
    if count %2==0:
        print("Even Palindrome")
    else:
        print("Odd Palindrome")
else:
    print ("Not a Palindrome")


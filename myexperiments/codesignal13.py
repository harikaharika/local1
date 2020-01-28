def reverseInParentheses(s):
    while ')' in s:
        a=s.find(')')
        b=s.rfind('(')
        c=(s[b+1:a][::-1])
        s=(s[:b]+c+s[a+1:])
        print(c)
    return s
print(reverseInParentheses("foo(bar(baz))blim"))
#foo(barzab)blim
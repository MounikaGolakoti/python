def is_anagram(s,t):
    return sorted(s)==sorted(t)
s=input('Enter first name')
t=input('Enter second name')
if is_anagram(s,t):
    print('is anagram')
else:
    print('invalid anagram')
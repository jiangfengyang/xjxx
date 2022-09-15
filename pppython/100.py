'''
n = input();
m = input();
l2 = ' ' * len(m);
li = [];
k = 1;
while k :
    l = n.find(m);
    if l >= 0 and n[l-1] == ' ' and n[l+len(m)] == ' ':
        li.append(l);
        n = n[:l] + l2 + n[l+len(m):];
    else :
        k = 0;
ans = '';
for i in n :
    if i != ' ' :
        ans += i ;
        k = 1;
    else :
        if k :
            ans += i;
            k = 0;
print(ans);
if li :
    for i in li :
        print(i,end=' ');
else :
    print("未出现！");
'''
n = input();
m = input();
k = '';
ans = '';
j = 0;
li = [];
for i in range(len(n)):
    if 'a' <= n[i] <= 'z' or 'A' <= n[i] <= 'Z' :
        k += n[i];
    else :
        if m == k :
            li.append(i - len(m));
        else :
            ans += k + n[i] ;
        k = '';
print(ans);
if li :
    for i in li :
        print(i,end=' ');
else :
    print('未出现！') ; 
    
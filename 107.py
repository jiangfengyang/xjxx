a = list(map(int,input().split()));
key = int(input());
s = [];
for i in range(0,len(a)-1,2):
    s.append([a[i],a[i+1]]);
head = a[-1];
k = head;
flag = False;
while k != -1 :
    if s[k][0] == key:
        flag = True;
        if(k == head):
            head = s[k][1];
        elif  (s[k][1] == -1):
            s[last][1] = -1;
        else :
            s[last][1] = s[k][1];
    last = k;
    k = s[k][1];    
    
k = head ;
if flag :
    while k != -1 :
        print(s[k][0],end=' ');
        k = s[k][1];
else :
    print('未找到');

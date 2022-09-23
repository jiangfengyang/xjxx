a = list(map(int,input().split()));
key = int(input());
s = [];
for i in range(0,len(a)-1,2):
    s.append([a[i],a[i+1]]);
head = a[-1];
k = head;

while k != -1 :
    tmp = s[k][1];
    if k == head and key < s[k][0] :
        s.append([key,head]);
        head = len(s)-1;
    if(s[k][0] < key and s[tmp][0] > key) :
        s.append([key,s[k][1]]);
        s[k][1] = len(s) - 1;
    if(tmp == -1 and key > s[k][0]) :
        s.append([key,-1]);
        s[k][1] = len(s)-1;
    k = tmp;
    
k = head ;
while k != -1 :
    print(s[k][0],end=' ');
    k = s[k][1];

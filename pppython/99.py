m = input();
for j in m :
    n = ord(j);
    #print(n);
    ans = '' ;
    while n :
        if n % 2 :
            ans += '1';
        else :
            ans += '0';
        n = n // 2;
    if len(ans) == 7:
        ans += '0' ;
    #print(ans);
    ans = ans[::-1];
    #print(ans);
    ans2 = '';
    for i in ans[4:] :
        if i == '0' :
            ans2 += '1';
        else :
            ans2 += '0';
    ans3 = '';
    ans3 += ans2[1];
    ans3 += ans2[2];
    ans3 += ans2[3];
    ans3 += ans2[0];
    #print(ans2);
    #print(ans3);
    ans = ans[0:4] + ans3;
    ans = int(ans,2);
    print(chr(ans),end='');

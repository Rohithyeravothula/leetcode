string mergeStrings(string a, string b) {
    string ans("");
    int i=0,j=0;
    int la, lb;
    la=a.size();
    lb=b.size();
    //string test("hello");
    //ans += test.at(0);
    //cout << ans;
    while(i<la && j<lb){
        ans += a.at(i);
        ans += b.at(j);
        i++;
        j++;
    }

    while(i<la){
        ans += a.at(i);
        i++;
    }
    while(j<lb){
        ans += b.at(j);
        j++;
    }

    return ans;
}

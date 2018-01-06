#include <vector>
#include <iostream>

using namespace std;
vector <int> getOneBits(int n) {
    vector <int> ans;
    int pos=0;
    int c=0;
    while(n){
        if (n&1 == 1){
            ans.push_back(pos);
            c+=1;
        }
        pos++;
        n=n>>1;
    }
    int i=0;
    for(i=0;i<pos;i++)
    ans[i] = pos-ans[i];
    ans.push_back(c);
    //std::reverse(ans.begin(), ans.end());
    return ans;
}


int main(){
    vector <int> ans = getOneBits(14);
    int i;
    for(i=0;i<ans.size();i++)
    cout << ans[i];
    return 0;
}

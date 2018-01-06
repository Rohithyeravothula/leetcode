#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;
/*
 * Complete the function below.
 */
string electionWinner(vector <string> votes) {
    map <string, int> vote_counts;
    int i,l;
    l = votes.size();
    for(i=0;i<l;i++){
        map<string, int>::iterator it = vote_counts.find(votes[i]);
        if(it == vote_counts.end())
            vote_counts.insert(pair<string, int>(votes[i], 0));
        else
            vote_counts[votes[i]] += 1;
    }
    map<string, int>::iterator it = vote_counts.begin();
    for(map<string, int>::iterator it2 = vote_counts.begin(); it2!=vote_counts.end(); ++it2){
        if(it2 -> second > it->second)
        it->second = it2 -> second;
    }
    vector <string> ans;
    for(map<string, int>::iterator it2 = vote_counts.begin(); it2!=vote_counts.end(); ++it2){
        if(it2 -> second == it->second)
            ans.push_back(it2 -> first);
    }

    sort(ans.begin(), and.end());
    return ans.first();
}

int main(){
    vector <string> votes;
    votes.push_back("aa");
    votes.push_back("bb");
    votes.push_back("cc");
    votes.push_back("aa");
    string ans = electionWinner(votes);
    return 0;
}


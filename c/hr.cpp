#include <iostream>
#include <vector>
#include <string>
#include <stack>
using namespace std;



bool Brackets(char opening, char closing)
{
	if( opening == '(' && closing == ')' ) return true;
	else if ( opening == '[' && closing == ']' ) return true;
	else if ( opening == '{' && closing == '}' ) return true;
	return false;
}

vector <string> braces(vector <string> values) {
    int index;
    vector <string> ans;
    for(index=0;index<values.size();index++){
        string curval = values[index];
        int i,l=curval.size();
        stack <char> stk;
        l = curval.size();

        for(i = 0; i < curval.length(); i++)
        {
            if( curval[i] == '(' || curval[i] == '{' || curval[i] == '[' )
                stk.push(curval[i]);
            else if( curval[i] == '(' || curval[i] == '}' || curval[i] == ']' )
                {
                if( stk.empty() || !Brackets( stk.top(), curval[i] ) )
                    break;
                else
                    stk.pop();
                }
            }
        cout << stk.empty();
        }
        return ans;
}

/*
 * Complete the function below.
 */


int main(){
    vector <string> query("()", "((");
    vector <string> ans = braces(query);
    int i;
    return 0;
}

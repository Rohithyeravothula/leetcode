#include<iostream>
#include<stack>
#include<string>
using namespace std;

bool check_match(char left, char right)
{
	if(left == '(' && right == ')')
        return true;
	else if(left == '{' && right == '}')
        return true;
	else if(left == '[' && right == ']')
        return true;
	return false;
}

bool check(string curval)
{
	stack<char> stk;
	int i, l;
	l = curval.size();
	for(i =0;i<l;i++)
	{
		if(curval[i] == '(' || curval[i] == '{' || curval[i] == '[')
			stk.push(curval[i]);
		else if(curval[i] == ')' || curval[i] == '}' || curval[i] == ']')
		{
			if(stk.empty() || !check_match(stk.top(),curval[i]))
				return false;
			else
				stk.pop();
		}
	}
	if (stk.empty())
        return true;
    return false;
}

vector <string> braces(vector <string> values) {
    vector <string> ans;
    int i,l;
    l = values.size();
    for(i=0;i<l;i++){
        if(check(values[i]))
            ans.push_back("YES");
        else
            ans.push_back("NO");
    }
    return ans;
}


int main()
{
	/*Code to test the function check*/
	string expression;
	cout<<"Enter an expression:  "; // input expression from STDIN/Console
	cin>>expression;
	if(check(expression))
		cout<<"Balanced\n";
	else
		cout<<"Not Balanced\n";
}

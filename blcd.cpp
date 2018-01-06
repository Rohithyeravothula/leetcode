#include<iostream>
#include<stack>
#include<string>
using namespace std;

bool check_match(char left,char right)
{
	if(left == '(' && right == ')') return true;
	else if(left == '{' && right == '}') return true;
	else if(left == '[' && right == ']') return true;
	return false;
}

bool check(string curval)
{
	stack<char>  stk;
	for(int i =0;i<curval.length();i++)
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
	return stk.empty() ? true:false;
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

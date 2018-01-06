#include <iostream>
#include <stack>
#include <string>

using namespace std;

// checks whether or not two characters are opening and closing
bool Brackets(char opening, char closing)
{
	if( opening == '(' && closing == ')' ) return true;
	else if ( opening == '[' && closing == ']' ) return true;
	else if ( opening == '{' && closing == '}' ) return true;
	return false;
}

// checks for when
bool BalancedParentheses(string b)
{
	stack<char> a;
	for(int i = 0; i < b.length(); i++)
	{
		if( b[i] == '(' || b[i] == '{' || b[i] == '[' )
			a.push(b[i]);
		else if( b[i] == '(' || b[i] == '}' || b[i] == ']' )
		{
			if( a.empty() || !Brackets( a.top(), b[i] ) )
				return false;
			else
				a.pop();
		}
	}
	return a.empty();
}

int main()
{
	// tests BalancedParentheses function
	string c;
	cout << "Enter an expression: ";
	cin >> c;
	if(BalancedParentheses(c))
		cout << "Nice! Balanced!" << endl;
	else
		cout << "Wow...not balanced." << endl;
}

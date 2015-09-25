#include <iostream>
#include <cassert>
#include <string>

using namespace std;

int atoi(string pStr)
{ 
    if (pStr.empty()) return 0;

    int running_total = 0;

    static int ZERO = static_cast<int>('0');
    static int NINE = static_cast<int>('9');
    for(int i = 0; i< pStr.size(); ++i)
    {
        int ch = static_cast<int>(pStr[i]);
        if( ch >= ZERO and ch <= NINE )
            running_total = running_total * 10 + (ch - ZERO);
        else
            break;
    } 

    return running_total;
        
}

int main()
{
    assert( atoi("124") == 124);
    assert( atoi("124x") == 124);
    assert( atoi("1s23") == 1);
    assert( atoi("") == 0);
    assert( atoi("-ksjdhf") == 0);

    cout << "All tests passed!" << endl;
    return 0;
}
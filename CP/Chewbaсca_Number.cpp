/*Luke Skywalker gave Chewbacca an integer number x. Chewbacca isn't good at numbers but he loves inverting digits in them. Inverting digit t means replacing it with digit 9 - t.

Help Chewbacca to transform the initial number x to the minimum possible positive number by inverting some (possibly, zero) digits. The decimal representation of the final number shouldn't start with a zero.

Input
The first line contains a single integer x (1 ≤ x ≤ 1018) — the number that Luke Skywalker gave to Chewbacca.

Output
Print the minimum possible positive number that Chewbacca can obtain after inverting some digits. The number shouldn't contain leading zeroes.*/

#include<bits/stdc++.h>
using namespace std;

int main()
{
    string x;
    cin>>x;

    for(int i=0;i<x.length();i++)
    {   int d=x[i]-'0';
        int inv=9-d;

        if(i==0 && inv==0)continue;

        x[i]=char(min(d,inv)+'0');
    }
    cout<<x;
    return 0;
}
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int power_2(int num)
{
    if(__builtin_popcount(num)==1)
    return 1;

    else
    return 0;
}
int main()
{
    int num;
    cin>>num;
    cout<<power_2(num);
    return 0;
}
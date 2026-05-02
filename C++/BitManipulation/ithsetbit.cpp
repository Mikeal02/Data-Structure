#include<iostream>
using namespace std;
int i_setbit(int number,int index)
{
    return (number & (1LL << index))!=0;
}
int main()
{
    int num,index;
    cout<<"enter the number:";
    cin>>num;
    cout<<endl<<"Enter the ith bit:";
    cin>>index;

    cout<<i_setbit(num,index);
    return 0;
}
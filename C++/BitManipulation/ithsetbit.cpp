#include<iostream>
using namespace std;
int i_setbit(int number,int index)
{
    string binary="";
    while(number>0)
    {
        binary+=number%2==0?'0':'1';
        number/=2;
    }

    if(index>=binary.length())return 0;

    return binary[index]=='1';
    //return (number & (1LL << index))!=0;

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
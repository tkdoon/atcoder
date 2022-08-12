#include<iostream>
#include <cmath>
using namespace std;

int main (){
    int A,B;
    cin>>A>>B;
    cout<<ceil((B-A)/(A-1.0))+1<<endl;
}
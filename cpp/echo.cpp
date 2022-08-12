#include<iostream>
#include <cmath>
using namespace std;

int main(){
    int n,j=0;
    string s;
    cin>>n>>s;
    if(n%2==1){
        cout<<"No";
    }
    else
    {for(int i=0;i<n/2;i++){
        if(s[i]==s[n/2+i]){j+=1;}
        else{j=0;}
    }
    if(j==n/2){cout<<"Yes";}
    else{cout<<"No";}}}
    
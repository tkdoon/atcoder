#include<iostream>
#include <cmath>
using namespace std;

int main (){
    int x[100][100],p,q;
    for(int i=0;i<100;i++){
        for(int j=0;j<100;j++){
        x[i][j]=0;
    }}
    x[1][2]=1;
    x[2][1]=1;
    for(int i=2;i<100;i++){
        for(int j=2;j<100;j++){
            x[i][j]=x[i-2][j-1]+x[i-1][j-2];
        }}
    cin>>p,q;
    cout<<x[p][q];
    

}
#include<iostream>
#include <cmath>
using namespace std;

int main (){
    double d;
    int n;
    int x[7],y[7];
    cin>>n;
    for(int i=0;i<n;i++){
        cin>>x[i]>>y[i];
    }
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            d+=pow(pow(x[i]-x[j],2.000000)+pow(y[i]-y[j],2.000000),0.50000);
        }
    }
    printf("%f\n",d/n);
}
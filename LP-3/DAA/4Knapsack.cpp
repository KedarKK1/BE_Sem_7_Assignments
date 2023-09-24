// Write a program to solve a 0-1 Knapsack problem using dynamic programming or branch and
// bound strategy.
// assignment no 4

#include<bits/stdc++.h>
using namespace std;

int knapsack(int* p,int* ti,int index,int t){
    if(index==0 or t==0) return 0;
    if(ti[index-1]<=t){ return max((knapsack(p, ti, index-1, t-ti[index-1])+p[index-1]), (knapsack(p, ti, index-1, t)));}
    else{
        return knapsack(p,ti,index-1,t);
    }

}
int main(){
    int t;
    cout<<"Enter total time:";t=50; // cin>>t;
    int n;
    cout<<"Enter no of entity:";n=3; // cin>>n;
    // int profit[n],ti[n];
    vector<pair<int,int>> v;
    int profit[3]={60,100,120};
    int ti[3]={10,20,30};
    // for(int i=0;i<;n;i++){
    //     cout<<"Profit: ";cin>>profit[i];
    //     cout<<"Time: ";cin>>ti[i];
    // }
    cout<<knapsack(profit,ti,n,t)<<endl;
    return 0;
}
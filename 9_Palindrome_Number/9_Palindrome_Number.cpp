#include <iostream>
 
using namespace std;


int main(){
	int x ;
	cin >> x;
	int i = x;
	int result = 0;
	if(x<0){
		cout << "False";
	}
	else{
		while(i !=0){
			result=result*10 + i%10;
			i /=10;
		}
		cout <<result<< x <<endl;
		cout << (result==x) << endl; // endl »Ø³µ £ºË³Ðò Êä³ö1£»endl 2£»result
		if(result == x){
			if(x > INT_MAX || x < INT_MIN){
			cout << "False";
			}
			else{
			cout << "True";
			}
		}
		else{
			cout << "False";
            }
        }
			
	}
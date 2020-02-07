#include <boost/multiprecision/cpp_int.hpp>
#include <iostream>
#include <string>
#include <cmath>
#include <boost/lexical_cast.hpp>

#define N 100

using boost::multiprecision::cpp_int;

cpp_int sum_(cpp_int A){
	cpp_int sum = 0;
	//convert auto int to string
	while(A > 0){
		sum+=A%10;
        	A/=10;
	}        
	return sum;
}


int main(){
	int A = 0;

	cpp_int max = 0;
	cpp_int sum = 0;
	for(cpp_int i = 0; i < N; i++){
		for(cpp_int j = 0; j < N; j++){
			cpp_int prod = i;
			for (int k = 0; k < j-1; j++){
				prod = prod*i;
			}
			std::cout << "prod : " << prod << std::endl;
			sum = sum_(prod);
			max = std::max(sum,max);
			std::cout << "sum : " << sum << std::endl;			
	
		}
	}	
	std::cout << max << std::endl;
}


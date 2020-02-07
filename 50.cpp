#include <vector>
#include <iostream>
#include <math.h>
#include <algorithm>


#define max_prime 1000000

int isPrime(const int& number){
	int end = sqrt(number)+1;
	
	for (int i = 3; i < end; i+=2){
		if (number%i == 0){
			return 0;		
		}
	}
	return 1;	
}

int main(){
	std::vector<int> Prime_number;
	Prime_number.push_back(2);
	Prime_number.push_back(3);
	Prime_number.push_back(5);
	Prime_number.push_back(7);
	for (int i = 9; i < max_prime; i+=2){
		if (isPrime(i)){
			Prime_number.push_back(i);
		}		
	}
	/*for(auto it_A = Prime_number.begin(); it_A != Prime_number.end(); ++it_A){
		std::cout << *it_A << std::endl;
	}*/
	
	int sum  = 0;
	int nombre = 0;
	int end = Prime_number.size();
	int indice = 0;
	int max = 0;
	int max_sum = 0;
	do{
		for(int i = indice; i < end; i++){
			sum += Prime_number[i];
			nombre++;
			if (sum > max_prime){
				nombre = 0;
				sum = 0;
				indice++;
				break;
			}
			if ((sum%2 != 0) && isPrime(sum) && nombre>max){
				max_sum = sum;
				max = nombre;
			}
		}
	}
	while(indice!=end);
	std::cout << max_sum << " max : " << max << std::endl;
	

	return 0;
	
		
}

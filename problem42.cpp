#include <iostream>
#include <fstream>
#include <vector>
#include <bits/stdc++.h> 
#include <boost/algorithm/string.hpp>
#include <algorithm>
#include <omp.h>


void function(int& r, const std::string& std){
	int end = static_cast<int>(std.size());
	for (int i = 0; i < end; i++){
		r += static_cast<int>(std[i]) - 64;
	}
}


int main(){
	std::string x;

	std::vector<std::string> ListofString;

	std::ifstream myfile;

	myfile.open("words.txt");
	while (myfile >> x) {
 		ListofString.push_back(x);
	}
	std::string input(x); 
    	std::vector<std::string> result; 
    	boost::split(result, input, boost::is_any_of(","));
	myfile.close();
	

	//
	int maxi = 0;
	std::vector<std::string> result_word;
	for (std::vector<std::string>::iterator it = result.begin() ; it != result.end(); ++it){
		boost::erase_all(*it, "\"");
		maxi = std::max(static_cast<int>((*it).size()),maxi);
	}
	/*for (std::vector<std::string>::iterator it = result.begin() ; it != result.end(); ++it){
		std::cout << *it << std::endl;
	}*/
	int n = 20;
	int elt;
	std::vector<int> triangle_Num;
	for( int i = 0; i != n; i++){
		elt = i*(i+1)/2;
		triangle_Num.push_back(elt);
	}
	/*for(std::vector<int>::iterator it_A = triangle_Num.begin() ; it_A != triangle_Num.end(); ++it_A){
		std::cout << *it_A << std::endl;
	}*/
	//work


	int s = 0;
	int r;
	for (std::vector<std::string>::iterator it = result.begin() ; it != result.end(); ++it){
		r = 0;
		function(r, *it);
		for(std::vector<int>::iterator it_A = triangle_Num.begin() ; it_A != triangle_Num.end(); ++it_A){
			if (r == *it_A){
				s+= 1;
				break;			
			}
			
		}
	}
	std::cout << s << std::endl;
	
    


	return 0;
};

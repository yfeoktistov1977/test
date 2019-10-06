#include<string>
#include<map>
#include<list>
#include <iostream>

struct cd {
	int c,d;
};

void test_stl(void)
{
	std::map<long, std::list<struct cd> > smap;
	std::list<struct cd> a,b;
	cd e; 

	smap[44] = a;
    std::map<long, std::list<struct cd> >::iterator it = smap.find(44);
    std::list<struct cd> l = it->second;
    
    std::cout << "Value" << it->first<< " ";

	return;
}

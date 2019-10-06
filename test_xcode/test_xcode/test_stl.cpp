#include<string>
#include<map>
#include<list>

struct cd {
	int c,d;
};

void test_stl(void)
{
	std::map<long, std::list<struct cd> > smap;
	std::list<struct cd> a,b;
	cd e; 

	smap[44] = a;

	//smap[44]->second->push_back(e);

	return;
}

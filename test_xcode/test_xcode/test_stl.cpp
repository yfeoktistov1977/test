#include<string>
#include<map>
#include<list>
#include <iostream>
#include <utility>
#include <algorithm>

struct cd {
	int c,d;
};

using namespace std;
void test_stl(void)
{
	std::map<long, std::list<struct cd> > smap;
	std::list<struct cd> a,b;

	smap[44] = a;
    std::map<long, std::list<struct cd> >::iterator it = smap.find(44);
    std::list<struct cd> l = it->second;

    std::cout << "Value" << it->first<< " ";

	return;
}


void permute(string elems, int mid, int end)
{
    static int count;
    if (mid == end - 1) {
        cout << ++count << " : " << elems << endl;
        return;
    }
    else {
    for (int i = mid; i < end; i++) {
            swap(elems[mid], elems[i]);
            permute(elems, mid + 1, end);
        }
    }
}

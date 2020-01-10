//
//  main.cpp
//  test_xcode
//
//  Created by YURY FEOKTISTOV on 06/10/2019.
//  Copyright © 2019 YURY FEOKTISTOV. All rights reserved.
//

#include <iostream>
#include "test_stl.h"

int main(int argc, const char * argv[]) {
    // insert code here...
    
    std::cout << "Hello, World!\n";
    
    test_stl();
    permute("123", 0, 3);
    
    return 0;
    
}

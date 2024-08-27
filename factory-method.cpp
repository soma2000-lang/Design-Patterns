//provides families of abract  pattern ,creates families of dependant objects wit
// without specifying their concrete classes

// hw the products are created , reaveal just the products and not their
// their implementations

#include <iostream>
class ProductA{


    public: virtual ~ProductA() {}
    virtual const char* getname()=0;
};

// this factory produces factory B



#ifndef MY_VERSION_SYSTEM_
#define MY_VERSION_SYSTEM_
#include <sstream>
#include <cinttypes>


class MyVer
{

public:
    int major = 0;
    int minor = 4;
    int patch = 49;

    std::string toString() const
    {
        std::stringstream ss;
        ss << major << "." << minor << "." << patch;
        return ss.str();
    }
};



#endif // MY_VERSION_SYSTEM_

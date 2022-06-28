
#ifndef MY_VERSION_SYSTEM_
#define MY_VERSION_SYSTEM_
#include <sstream>
#include <cinttypes>


class MyVer
{

public:
    std::uint8_t major = 0;
    std::uint8_t minor = 4;
    std::uint8_t patch = 49;

    std::string toString() const
    {
        std::stringstream ss;
        ss << major << "." << minor << "." << patch;
        return ss.str();
    }
};



#endif // MY_VERSION_SYSTEM_

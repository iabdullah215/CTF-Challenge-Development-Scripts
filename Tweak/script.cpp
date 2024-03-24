#include <iostream>
#include <string>
using namespace std;

string Flag(const string& odd, const int key[], int length) 
{
    string flag = odd;

    for (int i = 0; i < length; ++i) 
    {
        flag[i] = 'a' + (flag[i] - 'a' + key[i] + 26) % 26;
    }
    
    return flag;
}

int main() 
{
    const int key[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    string flag_ = Flag("fhapfuebzeitrlrdgaph", key, sizeof(key) / sizeof(key[0]));
    cout << "Your Flag Is: " << flag_ << endl;

    return 0;
}

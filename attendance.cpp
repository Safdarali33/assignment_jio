#include <bits/stdc++.h>
using namespace std;

int main() {
    int abs = 0, late = 0;
    string s;
    cin >> s;
    for (auto i = 0; i < s.size(); ++i) {
        if (s[i] == 'A') {
            ++abs;
        } else if (s[i] == 'L') {
            if (i > 0 && s[i - 1] == 'L') {
                ++late;
            } else {
                late = 1;
            }
        }
        if(abs>1){

            break;
            
        }
    }
    if (abs > 1 || late > 2) {
        cout<<"False";
    }
    else{
        cout<<"True";
    }

    return 0;
}

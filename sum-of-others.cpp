#include <iostream>
#include <vector>
#include <sstream>

using namespace std;

int main() {
    string line;
    while (getline(cin, line)) {
        int num, total = 0;
        vector<int> nums;
        bool found = false;

        stringstream ss;
        ss << line;
        while (!ss.eof()) {
            ss >> num;
            nums.push_back(num);
            // cout << "push back " << num << endl;
        }
   
        for (int i=0; i<nums.size(); i++) {
            total += nums[i];
            // cout << "total is currently " << total << endl; 
        }
        
        int j=0;
        while (!found) {
            // cout << "running while loop" << endl;
            if (total - nums[j] == nums[j]) {
                cout << nums[j] << endl; 
                found = true;
            }
            j++;
        } 
    }
}

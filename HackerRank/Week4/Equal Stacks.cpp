#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);


int equalStacks(vector<int> h1, vector<int> h2, vector<int> h3) 
{
    /* Equal stacks logic
       Ashray_Kumar_5008756
    */
    
    int total = 0;
    int total1 = 0;
    int total2 = 0;
    int x = 0;
    int y = 0;
    int z = 0;
    int b;
    
    for (b = h1.size()-1; b >=0; --b)
    {
        total = total + h1[b];
    }
    
    for(b = h2.size()-1; b>=0; --b)
    {
        total1 = total1 + h2[b];
    }
    
    for(b = h3.size()-1; b>=0; --b)
    {
        total2 = total2 + h3[b];
    }
    
    while (total!=total2 || total!=total1 || total1!=total2) 
    {
        if (total2 == 0 || total1 == 0 || total == 0) 
        {
            return 0;
        
        }
        else if (total >= total2 && total >= total1) 
        {
            total = total - h1[x++];
        
        }
        else if (total1 >= total && total1 >= total2)
        {
            total1 = total1 - h2[y++];
            
        }
        
        else 
            
        {
            total2 = total2 - h3[z++];
            
        }
        
    }
    return total;
    
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string first_multiple_input_temp;
    getline(cin, first_multiple_input_temp);

    vector<string> first_multiple_input = split(rtrim(first_multiple_input_temp));

    int f1 = stoi(first_multiple_input[0]);

    int f2 = stoi(first_multiple_input[1]);

    int f3 = stoi(first_multiple_input[2]);

    string h1_temp_temp;
    getline(cin, h1_temp_temp);

    vector<string> h1_temp = split(rtrim(h1_temp_temp));

    vector<int> h1(f1);

    for (int i = 0; i < f1; i++) {
        int h1_item = stoi(h1_temp[i]);

        h1[i] = h1_item;
    }

    string h2_temp_temp;
    getline(cin, h2_temp_temp);

    vector<string> h2_temp = split(rtrim(h2_temp_temp));

    vector<int> h2(f2);

    for (int i = 0; i < f2; i++) {
        int h2_item = stoi(h2_temp[i]);

        h2[i] = h2_item;
    }

    string h3_temp_temp;
    getline(cin, h3_temp_temp);

    vector<string> h3_temp = split(rtrim(h3_temp_temp));

    vector<int> h3(f3);

    for (int i = 0; i < f3; i++) {
        int h3_item = stoi(h3_temp[i]);

        h3[i] = h3_item;
    }

    int result = equalStacks(h1, h2, h3);

    fout << result << "\n";

    fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}

vector<string> split(const string &str) {
    vector<string> tokens;

    string::size_type start = 0;
    string::size_type end = 0;

    while ((end = str.find(" ", start)) != string::npos) {
        tokens.push_back(str.substr(start, end - start));

        start = end + 1;
    }

    tokens.push_back(str.substr(start));

    return tokens;
}

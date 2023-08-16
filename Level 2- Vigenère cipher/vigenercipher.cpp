#include <iostream>
#include <string>
#include <cctype>
#include <algorithm>

using namespace std;

string vigenercipher(string x, string key) {
    string lst_final = "";
    string code = x;
    int j = 0;

    for (int i = 0; i < x.size(); i++) {
        if (isalpha(x[i])) {
            code[i] = key[(i + j) % key.size()];
            lst_final += char((int(x[i]) - int(code[i]) + 26) % 26 + 97);
        } else {
            lst_final += char(int(x[i]));
            j--;
        }
    }

    return lst_final;
}

int main() {
    string x = "Kg fcwd qh vin pnzy hjcocnt, cjjwg ku wnth nnyvng kxa cjjwg. Urfjm xwy yjg rbbufqwi \"vjg_djxn_ofs_dg_rmncbgi\" yq iq uqtxwlm. Oca zxw qcaj vjg tctnplyj hqs cjn pjcv ejbvdnt. Yt hkpe cjn gcnv, aqv okauy bknn ongm vt zvvgs vcpkh bqtft cjntj.";
    cout << "Encrypted text: " << x << endl;

    string key = "jcjcffcccb";
    cout << "Key: " << key << endl;

    transform(x.begin(), x.end(), x.begin(), ::toupper);
    transform(key.begin(), key.end(), key.begin(), ::toupper);

    cout << "Decrypted text: " << vigenercipher(x, key) << endl;

    return 0;
}

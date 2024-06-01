#include<iostream>
 
using namespace std;
void encrypt(char text[], int key) {
    char ch;
    int ab;
    for(ab = 0; text[ab] != '\0'; ++ab){
        ch = text[ab];
        if(ch >= 'a' && ch <= 'z'){
            ch = ch + key;
            if(ch > 'z'){
                ch = ch - 'z' + 'a' - 1;
             }
             text[ab] = ch;
             }
             else if(ch >= 'A' && ch <= 'Z'){
             ch = ch + key;
             if(ch > 'Z'){
                ch = ch - 'Z' + 'A' - 1;
            }
            text[ab] = ch;
        }
    }
    cout << "Encrypted text: " << text;
}

void decrypt(char text[], int key) {
    char ch;
    int ab;
    for(ab = 0; text[ab] != '\0'; ++ab){
        ch = text[ab];
        if(ch >= 'a' && ch <= 'z'){
            ch = ch - key;
            if(ch < 'a'){
                ch = ch + 'z' - 'a' + 1;
             }
             text[ab] = ch;
             }
             else if(ch >= 'A' && ch <= 'Z'){
                ch = ch - key;
                if(ch > 'a'){
                    ch = ch + 'Z' - 'A' + 1;
                }
                text[ab] = ch;
            }   
    }   
    cout << "Decrypted text: " << text;
}

int main()
{
    char text[100];
    int key, choice;
    cout << "Enter a text: ";
    cin.getline(text, 100);
    cout << "Enter key: ";
    cin >> key;
    cout << "Enter 1 to encrypt or 2 to decrypt: ";
    cin >> choice;
    if (choice == 1) {
        encrypt(text, key);
       }
     else if (choice == 2) 
      {
        decrypt(text, key);
      }
     else 
      {
        cout << "Invalid choice." << endl;
    }
    return 0;
}

#include <iostream>
#include <fstream>
#include <cstdlib>
#include <climits>

using namespace std;

int main(){
    ifstream fin("Current_Reservoir_Levels.tsv");
    if (fin.fail()) {
        cerr << "File cannot be opened for reading." << endl;
        exit(1); // exit if failed to open the file
    }

    string junk;        // new string variable
    getline(fin, junk); // read one line from the file 
    //declared variables
    string date, input_date;
    double eastSt, eastEl, westSt, westEl;

    cout << "Please enter a date: ";
    cin >> input_date;
    while (fin >> date >> eastSt >> eastEl >> westSt >> westEl) { 
        // this loop reads the file line-by-line
        // extracting 5 values on each iteration 
        
        fin.ignore(INT_MAX, '\n'); //skips to the end of line, 
                            //ignorring the remaining columns 
    
        //// YOUR CODE GOES HERE
        if (input_date == date){
            cout << "East basin storage: " << eastSt << " billion gallons";
        }

    }

    fin.close();
}
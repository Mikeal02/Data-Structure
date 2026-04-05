/*
 * DATE: April 5, 2026
 * PATTERN: Simulation, String Scan
 *
 * APPROACHES:
 * 1. BRUTE FORCE:
 * - Step 1: Model full AST of statements—overkill for ++/-- detection.
 * - TIME: O(n * len) per statement | SPACE: O(1)
 *
 * 2. BETTER:
 * - Step 1: Check first and last char of each token, or compare to "X++" / "--X" patterns.
 * - TIME: O(n) statements | SPACE: O(1)
 *
 * 3. OPTIMAL:
 * - Step 1: If substring "++" appears, increment else decrement (problem-specific shortcuts).
 * - TIME: O(n * k) with k string length | SPACE: O(1)
 *
 * AHA-MOMENT: Only two statement shapes; detecting "++" in the 3-char string decides increment vs decrement.
 */

#include<bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin>>n;
    int x=0;
    string s;
    while(n--)
    {
        cin>>s;
        if(s.find('++')!=string::npos)
        x++;
        else
        x--;

    }
    cout<<x<<endl;
}
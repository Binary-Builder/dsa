class Solution {
    public boolean isPalindrome (int x){
        if ( x < 0 || (x > 0 && x % 10 == 0)) { // if negative OR ends with 0
            return false;
        }
        int y = 0;
        for ( ; y < x; x /= 10){
            y = y * 10 + x % 10; // checking two halves
        }
        return x == y || x == y/10; //if no. is odd, remove the middle number and then compare
    }
}
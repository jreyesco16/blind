class Solution {
public:
    int getSum(int a, int b) {
        int i = 0;
        while (b != 0) {
            std::cout << "i: " <<  i << "\n";
            int carry = a & b;
            a = a ^ b;
            b = (unsigned)carry << 1;

            i+=1;
        }
        return a;
    }
};
#include <cassert>
#include <iostream>
// solution that is straight forward but fails on two counts:
// 1. O(n^2) means it is slow on large data sets. -- solved by calculating the sums in constant time. Do not use for loops for lsum and rsum
// 2. data overflows on large ints -- solved by changing data types
int equi(int A[], int n)
{
    // traverse the array
    for(int k = 0; k < n; ++k){

        int lsum = 0;
        int rsum = 0;
        // 0 .. k-1 sums up the elements of A[]
        for(int m = 0; m < k; ++m)   lsum += A[m];
        // k + 1 .. n-1 sums up the elements of A[]
        for(int j = k + 1; j < n; ++j)  rsum += A[j];
        // does the comparison
        if (lsum == rsum) return k;
    }
    // found nothing
    return -1;
}


int equi2(int A[], int n)
{
    // checks if the array is empty
    if(n == 0) return -1;

    // compute for total sum
    long long sum = 0;
    for(int i = 0; i < n; i++) sum += (long long) A[i];

    long long lsum = 0;
    // traverse the array
    for(int i = 0; i < n; i++)
    {
        // different computation of rsum
        long long rsum = sum - lsum - A[i];
        // check if we have a balance
        if (rsum == lsum) return i;
        // compute for lsum
        lsum += (long long) A[i];
    }

    return -1;

}


int main()
{
    int A[] = {-7,1,5,2,-4,3,0};
    int B[] = {-1, 3, -4, 5, 1, -6, 2, 1};
    std::cout<< equi(A, 7) << std::endl;
    std::cout<< equi2(A, 7) << std::endl;
    
    return 0;
}
// you can write to stdout for debugging purposes, e.g.
// printf("this is a debug message\n");

int getSum(int A[], int start, int end)
{
    int sum = 0;
    int _start = start;
    int _end = end;
    if(_end == _start) return sum;
    
    for(int i = _start; _start < _end; i++)
    {   
        sum += A[i]; 
    }
    
    return sum;    
}

int solution(int A[], int N) {
    // write your code in C99
    int found = 0;
    int p = 0;
    while (!found && p++ < N)
    {
        int left = 0;
        int right = 0;
        if(p == 0)
        {
            right = getSum(A, 0, N);
        }
        else
        {
            left = getSum(A, 0, p);
            right = getSum(A, p, N);
        }
        
        if(left == right)   found = 1;
    }
    return p;
}
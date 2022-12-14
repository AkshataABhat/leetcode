#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        # code here
        z,o,t=0,0,0
        for i in range(len(arr)):
            if(arr[i]==0):
                z+=1
            elif(arr[i]==1):
                o+=1
            else:
                t+=1
        
        for i in range(0,z):
            arr[i]=0
        for i in range(z,z+o):
            arr[i]=1
        for i in range(z+o,z+o+t):
            arr[i]=2
        return arr
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends
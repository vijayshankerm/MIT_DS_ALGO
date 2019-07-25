"\\ # Algorithmic Thinking, Peak Finding" 

 #include<iostream>
    using namespace std;
     
    int findPeak(int arr[],int low,int high ,int size)
    {
    	int mid = low + (high -low)/2;
     
    	if(arr[mid]<arr[mid-1])
    		return findPeak(arr,low,mid-1,mid-low);
    	else if(arr[mid]<arr[mid+1])
    		return findPeak(arr,mid+1,high,high-mid);
     
    	return arr[mid];
    }
     
    int main()
    {
    	int arr[10] = {7,8,9,17,24,35,46,7,8,9};
    	int n = sizeof(arr)/sizeof(arr[0]);
    	cout<<findPeak(arr,0,n-1,n-1)<<endl;
    }
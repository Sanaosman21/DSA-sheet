class Solution:
    def quick_sort(self,arr,low,high):
        if low<high:
            p=self.partition(arr,low,high)
            self.partition(arr,low,p-1)
            self.partition(arr,p+1,high)
    def partition(self,arr,low,high):
        i=low
        j=high
        pivot=arr[low]
        while(i<j):
            while(i<=high and pivot>=arr[i]):
                i+=1
            while(j>=low and pivot<arr[j]):
                j-=1
            if i<j:
                arr[i],arr[j]=arr[j],arr[i]
        arr[low],arr[j]=arr[j],arr[low]
        return j 
arr=[6,3,8,5,2,7,4]
sol=Solution()
sol.quick_sort(arr,0,len(arr)-1)
print(arr)
#include <stdio.h>


int getInvCount(int arr[], int n)
{
  int inv_count = 0;
  int i, j;
 
  for(i = 0; i < n - 1; i++){
    for(j = i+1; j < n; j++){
      if(arr[i] > arr[j]){
        inv_count++;}
 }}
  return inv_count;
}
 
/* Driver progra to test above functions */
int main(int argv, char** args)
{
  //int arr[] = {23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9};
  int arr[] = {25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1};
  printf(" Number of inversions are %d \n", getInvCount(arr, 5));
  getchar();
  return 0;
}

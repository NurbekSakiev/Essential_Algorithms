import java.io.*;
import java.util.*;
import java.lang.*;

public class InsertionSort {

    public static void insertionSortPart2(int[] ar)
    {       
           // Fill up the code for the required logic here
           // Manipulate the array as required
           // The code for Input/Output is already provided
        int size = ar.length;
        for (int j = 0; j<size-1; j++) {
            for (int k = j+1; k>0; k--) {
                if (ar[k-1]>ar[k]) {
                    int temp = ar[k];
                    ar[k] = ar[k-1];
                    ar[k-1] = temp;
                    
                }
            }
            printArray(ar);
            
        }
    }  
    
      
    public static void main(String[] args) {
       Scanner in = new Scanner(System.in);
       int s = in.nextInt();
       int[] ar = new int[s];
       for(int i=0;i<s;i++){
            ar[i]=in.nextInt(); 
       }
       insertionSortPart2(ar);    
                    
    }    
    private static void printArray(int[] ar) {
      for(int n: ar){
         System.out.print(n+" ");
      }
        System.out.println("");
   }
}
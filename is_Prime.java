import java.math.*;
import java.util.*;
import java.lang.*;
public class ALGs {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(RaiseToPower(7,6));
		System.out.println(IsPrime(19,15));
	}
	public static double RaiseToPower(int base, int power) {
		int num =1;
		int second=0;
		double res = 1;
		while (num+1<power) {
			num*=2;
		}
		num/=2;
		while (power>second) {
			second+=num;
			res *=Math.pow(base,num);
			num/=2;
		}
		return res;
	}
	
	public static boolean IsPrime(int num, int max_tests) {
		
		Random rand = new Random();
		for (int i=1;i<max_tests;i++) {
			int randomNum = rand.nextInt(num)+1;
			System.out.println(randomNum);
			if (Math.pow(randomNum, num-1)%num!=1) {
				return false;
			}
		}
		return true;
	}

}
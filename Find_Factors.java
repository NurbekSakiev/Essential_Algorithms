
import java.awt.*;
import java.awt.List;
import java.util.*;
import java.lang.*;
public class FindFactors {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(findFactors(100));
	}

	public static ArrayList findFactors(int num) {
		ArrayList factors = new ArrayList();
		int i = 2;
		while (i<num) {
			while(num % i == 0) {
				factors.add(i);
				num/=i;
			}
			i++;
		}
		if (num>1) {
			factors.add(num);
		}
		return factors;
		
	}
}
public class LinkedList {

	public int value;
	public LinkedList next;
	
	
	public void Link(int data) {
		this.value = data;
	}
	
	public void display(){
		System.out.println("Data "+value);
	}

}
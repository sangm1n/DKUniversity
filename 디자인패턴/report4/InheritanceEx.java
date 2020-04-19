package chapter5;

class Person {
	private int weight;
	int age;
	protected int height;
	public String name;
	
	public void setWeight(int weight) {
		this.weight = weight;
	}
	
	public int getWeight() {
		return weight;
	}
}

class Student extends Person {
	public void set() {
		age = 25;
		name = "이상민";
		height = 175;
		// weight = 65;
		setWeight(65);
	}
}

public class InheritanceEx {
	public static void main(String[] args) {
		Student s = new Student();
		s.set();
		System.out.print("나이: " + s.age + "\n이름: " + s.name
				+ "\n키: " + s.height + "\n몸무게: " + s.getWeight());
	}
}

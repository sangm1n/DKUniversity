package chapter5;

class Point {
	private int x, y;
	
	public Point() {
		this.x = this.y = 0;
	}
	
	public Point(int x, int y) {
		this.x = x;
		this.y = y;
	}
	
	public void set(int x, int y) {
		this.x = x;
		this.y = y;
	}
	
	public void showPoint() {
		System.out.println("(" + x + ", " + y + ")");
	}
}

// Point 클래스를 상속받은 ColorPoint 클래스
class ColorPoint extends Point {
	private String color;
	
	public void setColor(String color) {
		this.color = color;
	}
	
	public ColorPoint() {
		this.color = null;
	}
	
	public ColorPoint(int x, int y, String color) {
		super(x, y);
		this.color = color;
	}
	
	public void showColorPoint() {
		System.out.print(color);
		showPoint();
	}
}

public class ColorPointEx {
	public static void main(String[] args) {
		Point p = new Point();
		p.set(1,  2);;
		p.showPoint();
		
		ColorPoint cp = new ColorPoint();
		cp.set(3, 4);
		cp.setColor("red");
		cp.showColorPoint();
	}
}

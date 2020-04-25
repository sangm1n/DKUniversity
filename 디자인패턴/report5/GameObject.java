package chapter6;

// 추상 클래스
public abstract class GameObject {
	protected int distance;		// 한 번 이동 거리
	protected int x, y;			// 현재 위치 (화면 맵 상의 위치)
	
	// 초기 위치와 이동 거리 설정
	public GameObject(int startX, int startY, int distance) {
		this.x = startX;
		this.y = startY;
		this.distance = distance;
	}
	public int getX() {
		return x;
	}
	public int getY() {
		return y;
	}
	// 이 객체가 객체 p와 충돌했으면 true 리턴
	public boolean collide(GameObject p) {
		if(this.x == p.getX() && this.y == p.getY())
			return true;
		else
			return false;
	}
	// 이동한 후의 새로운 위치로 x, y 변경
	public abstract void move();
	// 객체의 모양을 나타내는 문자 리턴
	public abstract char getShape();
}

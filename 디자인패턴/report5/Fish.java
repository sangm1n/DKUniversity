package chapter6;

public class Fish extends GameObject {
	public Fish(int startX, int startY, int distance) {
		super(startX, startY, distance);
	}

	@Override
	public void move() {
		// 1~4 사이 랜덤한 정수 추출
		int num = (int)(Math.random()*4 + 1);
		
		// 현재 좌표를 빈 칸으로 초기화
		Game.background[x][y] = '□';
		
		// 추출된 정수마다 동작 설정
		switch(num) {
		// y=0(맨 왼쪽)에 있지 않은 경우에만 왼쪽으로 이동
		case 1:
			if (y != 0)
				y = y - distance;
			break;
		// x=9(맨 아래)에 있지 않은 경우에만 아래로 이동
		case 2:
			if (x != 9)
				x = x + distance;
			break;
		// x=0(맨 위)에 있지 않은 경우에만 위로 이동
		case 3:
			if (x != 0)
				x = x - distance;
			break;
		// y=19(맨 오른쪽)에 있지 않은 경우에만 오른쪽으로 이동
		case 4:
			if (y != 19)
				y = y + distance;
			break;
		}
		
		// 이동한 좌표에 getShape() 함수를 통해 F 표시
		Game.background[x][y] = getShape();

	}

	@Override
	public char getShape() {
		return 'F';
	}
}

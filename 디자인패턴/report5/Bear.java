package chapter6;

import java.util.Scanner;

public class Bear extends GameObject {
	public Bear(int startX, int startY, int distance) {
		super(startX, startY, distance);
	}

	@Override
	public void move() {
		System.out.print("왼쪽(a), 아래(s), 위(d), 오른쪽(f) 입력 >> ");
		
		Scanner scan = new Scanner(System.in);
		// charAt(0)을 통해 하나의 문자 입력
		char input = scan.next().charAt(0);
		
		// 현재 좌표를 빈 칸으로 초기화
		Game.background[x][y] = '□';
		
		// 입력받은 문자마다 switch문을 통해 동작 설정
		switch(input) {
		// y=0(맨 왼쪽)에 있지 않은 경우에만 왼쪽으로 이동
		case 'a':
			if (y != 0)
				y = y - distance;
			break;
		// x=9(맨 아래)에 있지 않은 경우에만 아래로 이동
		case 's':
			if (x != 9)
				x = x + distance;
			break;
		// x=0(맨 위)에 있지 않은 경우에만 위로 이동
		case 'd':
			if (x != 0)
				x = x - distance;
			break;
		// y=19(맨 오른쪽)에 있지 않은 경우에만 오른쪽으로 이동
		case 'f':
			if (y != 19)
				y = y + distance;
			break;
		}
		
		// 이동한 좌표에 getShape() 함수를 통해 ■ 표시
		Game.background[x][y] = getShape();
	}

	@Override
	public char getShape() {
		return '■';
	}
	
}

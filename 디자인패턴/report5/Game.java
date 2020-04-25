package chapter6;

import java.util.Scanner;

public class Game {
	// 10행 20열의 이차원 배열 생성
	static char background[][] = new char[10][20];	
	int height = 10;
	int width = 20;
	Bear bear;
	Fish fish;
	
	// 전체적인 게임을 진행하는 메소드
	public void runGame() {
		startShow();
		
		while(true) {
			int i;	
			// fish가 움직였는지 카운트해주는 변수
			int count = 0;			
			
			int random[] = new int[2];
			// 0~4 사이 중복을 제외하여 랜덤한 수 2개 추출
			for (i = 0; i < 2; i++) {
				random[i] = (int)(Math.random() * 5);
				
				for (int j = 0; j < i; j++) {
					if (random[i] == random[j]) {
						i--;
						break;
					}
				}
			}
			
			// 5번을 한 시퀀스로 수행
			for (int j = 0; j < 5; j++) {
				gameShow();
				
				bear.move();
				// bear가 움직였는데 collide 메소드가 true 리턴 시 게임 종료
				if((bear.collide(fish))) {
					endShow();
					System.out.println("Congratulation ! Bear eat the Fish !!");
					return;
				}
				
				// 랜덤하게 추출된 두 수와 인덱스인 j가 같은 경우 fish 위치 이동
				for (int k = 0; k < 2; k++) {
					if (j == random[k]) {
						count++;
						fish.move();
					}
				}
			}
		}
	}
	
	// 게임이 시작되고 처음으로 보여지는 격자판
	public void startShow() {
		int bHeight, bWidth, fHeight, fWidth;
		// bear와 fish의 위치를 10행 20열 중 랜덤하게 위치할 수 있도록 설정
		while(true) {
			bHeight = (int)(Math.random() * 10);
			bWidth = (int)(Math.random() * 20);
			fHeight = (int)(Math.random() * 10);
			fWidth = (int)(Math.random() * 20);
			
			// bear와 fish의 시작점이 겹치지 않도록
			if (bHeight != fHeight && bWidth != fWidth)
				break;
		}
		
		bear = new Bear(bHeight, bWidth, 1);
		fish = new Fish(fHeight, fWidth, 1);
		
		// 격자판을 빈 칸으로 초기화
		for(int i = 0; i < height; i++) {
			for(int j = 0; j < width; j++) {
				background[i][j] = '□';
			}
		}
		
		// bear와 fish 시작 위치에 객체의 모양을 나타내는 문자 표현
		background[bear.x][bear.y] = bear.getShape();
		background[fish.x][fish.y] = fish.getShape();

	}
	
	// 게임이 진행될 때마다 보여지는 격자판
	public void gameShow() {
		for(int i = 0; i < height; i++) {
			for(int j = 0; j < width; j++) {
				System.out.print(background[i][j]);
			}
			System.out.println();
		}
		System.out.println();
	}
	
	// bear가 fish 위치에 도달했을 경우 보여지는 격자판
	public void endShow() {
		// bear를 나타내는 문자 표현만 나타나도록
		background[bear.x][bear.y] = bear.getShape();
		
		for(int i = 0; i < height; i++) {
			for(int j = 0; j < width; j++) {
				System.out.print(background[i][j]);
			}
			System.out.println();
		}
		System.out.println();
	}
}


package chapter3;


/*
 *  2020.04.03 카드 번호맞추기 게임

 *  by. sangmin
 */

import java.util.Scanner;

public class Homework2 {
	public static void main(String[] args) {
		startGame();
	}
	
	// 게임을 시작하는 startGame 메소드
	static void startGame() {
		// 0~100 사이 난수 생성
		int result = (int)(Math.random()*100);
		
		System.out.println("Hidden number is created. Try it!");
		System.out.print("Input Number (For loop : 1 / While loop : 2 / Do-while loop : 3) \n"
				+ ">> ");	
		
		Scanner scanner = new Scanner(System.in);	
		int num = scanner.nextInt();
		
		// 사용자의 입력에 따라 각기 다른 반복문 메소드 사용
		// 인자로 생성된 난수 값 전달
		if (num == 1) 
			forLoop(result);
		else if (num == 2) 
			whileLoop(result);
		else if (num == 3) 
			dowhileLoop(result);
	}
	
	// 게임 진행 여부를 묻는 continueGame 메소드
	static void continueGame() {		
		while(true) {
			System.out.print("More Game(y/n) >> ");
			Scanner scanner = new Scanner(System.in);
			String ans = scanner.next();
			
			// y 입력 시 startGame 메소드 실행하여 게임 재시작
			if (ans.equals("y")) {
				startGame();
				break;
			}
			// n 입력 시 프로그램 종료
			else if (ans.equals("n")) {
				System.out.println("End Game");
				break;
			}
			// y와 n 이외의 문자 입력 시 while문 계속 반복
			else 
				continue;
		}
	}
	
	// for문을 사용한 forLoop 메소드
	static void forLoop(int result) {	
		System.out.println("You selected For loop !");
		
		// 난수인 result 값과 사용자가 입력하는 val 값이 같을때까지 무한 반복
		for (;;) {
			Scanner scanner = new Scanner(System.in);
			System.out.print("Input number >> ");
			int val = scanner.nextInt();
			
			if (val > result) {
				System.out.println(" --> Lower !");
				continue;
			}
			else if (val < result) {
				System.out.println(" --> Higher !");
				continue;
			}
			// 정답을 맞춘 경우 게임 진행 여부를 묻는 continueGame 메소드 실행
			else {
				System.out.println(" --> Correct !");
				continueGame();
				break;
			}
		}
	}
	
	// while문을 사용한 whileLoop 메소드
	static void whileLoop(int result) {	
		System.out.println("You selected While loop !");
		
		// 난수인 result 값과 사용자가 입력하는 val 값이 같을때까지 무한 반복
		while(true) {
			Scanner scanner = new Scanner(System.in);
			System.out.print("Input number >> ");
			int val = scanner.nextInt();
			
			if (val > result) {
				System.out.println(" --> Lower !");
				continue;
			}
			else if (val < result) {
				System.out.println(" --> Higher !");
				continue;
			}
			// 정답을 맞춘 경우 게임 진행 여부를 묻는 continueGame 메소드 실행
			else {
				System.out.println(" --> Correct !");
				continueGame();
				break;
			}
		}
	}
	
	// do-while문을 사용한 dowhileLoop 메소드
	static void dowhileLoop(int result) {	
		System.out.println("You selected Do-while loop !");
		
		// 난수인 result 값과 사용자가 입력하는 val 값이 같을때까지 무한 반복
		do {	
			Scanner scanner = new Scanner(System.in);
			System.out.print("Input number >> ");
			int val = scanner.nextInt();
			
			if (val > result) {
				System.out.println(" --> Lower !");
				continue;
			}
			else if (val < result) {
				System.out.println(" --> Higher !");
				continue;
			}
			// 정답을 맞춘 경우 게임 진행 여부를 묻는 continueGame 메소드 실행
			else {
				System.out.println(" --> Correct !");
				continueGame();
				break;
			}
		} while(true);
	}
}

package chapter4;

/*
 *  2020.04.11 끝말잇기 게임
 *  by. sangmin
 */

import java.util.Scanner;

public class WordGame {
	public static void main(String[] args) {
		// 시작 단어
		String word = "아버지";				
		Scanner scanner = new Scanner(System.in);
		
		System.out.println("끝말잇기 게임을 시작합니다...");
		System.out.print("게임에 참가하는 인원은 몇명입니까 >> ");
		int num = scanner.nextInt();		
		
		run(num, word);
	}
	
	// 인원 수와 시작 단어를 매개변수로 하는 메소드
	public static void run(int num, String word) {
		// 입력받은 수만큼 객체 생성
		Player[] people = new Player[num];
		Scanner scanner = new Scanner(System.in);
		
		// 참가자 이름을 Player 객체의 name 변수에 저장 
		for (int i = 0; i < num; i++) {
			System.out.print("참가자의 이름을 입력하세요 >> ");
			people[i] = new Player();
			people[i].name = scanner.next();
		}
		
		System.out.println("시작하는 단어는 아버지입니다");
				
		// while문을 반복하기 위한 check 변수
		boolean check = true;
		
		while(check) {
			for (int i = 0; i < num; i++) {
				System.out.print(people[i].name + " >> ");
				people[i].getWordFromUser();
				
				// 단어의 맨 끝자리 인덱스
				int lastIndex = word.length() - 1;
				// lastIndex를 통해 단어의 마지막 글자를 lastChar 변수에 저장
				char lastChar = word.charAt(lastIndex);
				
				check = people[i].checkSuccess(lastChar);
				
				// check가 false인 경우 while문 빠져나옴
				if (check == false) {
					System.out.println(people[i].name + "이(가) 졌습니다");
					break;
				}
				// word 변수를 입력한 단어로 바꿔줌
				word = people[i].input;
			}
		}
	}
}

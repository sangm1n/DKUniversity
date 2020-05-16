package chapter4;

import java.util.Scanner;

public class Player {
	Scanner scanner = new Scanner(System.in);
	
	public String name;
	public String input;
	
	// 입력받은 단어를 리턴해주는 메소드
	public String getWordFromUser() {
		input = scanner.next();
		return input;
	}
	
	// 매개변수로 마지막 글자를 입력받아 T/F 리턴해주는 메소드
	public boolean checkSuccess(char lastChar) {
		// 매개변수로 받은 마지막 글자와 입력한 첫글자가 같은 경우 true
		if (lastChar == input.charAt(0))
			return true;
		// 그렇지 않으면 false
		else
			return false;
	}
}

/*
 *  2020.03.23 가위바위보게임
 *  by. sangmin
 */
import java.util.Scanner;

public class Homework {
	public static void main(String[] args) {
		System.out.println("<<<<< 가위 바위 보 게임 (비길 시 다시) >>>>>\n");
		
		// 반복문을 실행하기 위한 조건 변수 go
		int go = 0;
		
		while(go == 0) {
			System.out.print("person-A >> ");					
			Scanner scanner = new Scanner(System.in);
			String pA = scanner.next();
			
			// A가 가위, 바위, 보 중 하나를 입력한 경우
			if (pA.equals("가위") | pA.equals("바위") | pA.equals("보")) {
				while(true) {
					System.out.print("person-B >> ");
					String pB = scanner.next();
					
					// B가 가위, 바위, 보 중 하나를 입력한 경우
					if (pB.equals("가위") | pB.equals("바위") | pB.equals("보")) {
						// switch문에서 비기지 않은 경우 go 변수에 1을 대입하여 게임 종료
						// 비긴 경우 go 변수는 그대로 0이므로 계속해서 게임 반복
						switch(pA) {
						case "가위":
							switch(pB) {
							case "가위":
								System.out.println("결과 : 비겼습니다.");
								break;
							case "바위":
								System.out.println("결과 : B가 이겼습니다.");
								go = 1;
								break;
							case "보":
								System.out.println("결과 : A가 이겼습니다.");
								go = 1;
								break;
							}
							break;
						case "바위":
							switch(pB) {
							case "가위":
								System.out.println("결과 : A가 이겼습니다.");
								go = 1;
								break;
							case "바위":
								System.out.println("결과 : 비겼습니다.");
								break;
							case "보":
								System.out.println("결과 : B가 이겼습니다.");
								go = 1;
								break;
							}
							break;
						case "보":
							switch(pB) {
							case "가위":
								System.out.println("결과 : B가 이겼습니다.");
								go = 1;
								break;
							case "바위":
								System.out.println("결과 : A가 이겼습니다.");
								go = 1;
								break;
							case "보":
								System.out.println("결과 : 비겼습니다");
								break;
							}
							break;
						}
						break;
					}
					// B가 가위, 바위, 보 이외의 문자를 입력한 경우 반복문 계속 수행
					else
						continue;
				}
			}			
			// A가 가위, 바위, 보 이외의 문자를 입력한 경우 반복문 계속 수행
			else
				continue;
		}
	}
}

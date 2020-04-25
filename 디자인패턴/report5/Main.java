package chapter6;

/*
 *  2020.04.21 Bear and Fish Game

 *  by. sangmin
 */


public class Main {
	public static void main(String[] args) {
		System.out.println("========== start 'Bear eat Fish' game !! ==========");
		System.out.print("   ■ is bear, your mission is reach the F(fish)");
		System.out.println();
		
		// Game 객체를 만들어 runGame() 메소드 호출
		Game g = new Game();
		g.runGame();
	}
}

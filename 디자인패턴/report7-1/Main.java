package chapter8_1;

/*
 *  2020.05.02 Foobar Motor Company

 *  by. sangmin
 */

public class Main {
	public static void main(String []args) {
		SpeedMonitor monitor = new SpeedMonitor();
		Speedometer speedo = new Speedometer();
		speedo.addObserver(monitor);
		speedo.setCurrentSpeed(50);
		speedo.setCurrentSpeed(70);
		speedo.setCurrentSpeed(40);
		speedo.setCurrentSpeed(100);
		speedo.setCurrentSpeed(65);
	}
}

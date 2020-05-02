package chapter8_2;

/*
 *  2020.05.02 Foobar Motor Company

 *  by. sangmin
 */

public class Main {
	public static void main(String []args) {
		SpeedMonitor2 monitor = new SpeedMonitor2();
		Speedometer2 speedo = new Speedometer2();
		speedo.registerObserver(monitor);
		speedo.setCurrentSpeed(50);
		speedo.setCurrentSpeed(70);
		speedo.setCurrentSpeed(40);
		speedo.setCurrentSpeed(100);
		speedo.setCurrentSpeed(69);
	}
}
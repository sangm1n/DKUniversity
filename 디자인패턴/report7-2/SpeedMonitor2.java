package chapter8_2;

public class SpeedMonitor2 implements Observer {
	public static final int SPEED_TO_ALERT = 70;
	
	public void update(int speed) {
		if (speed > SPEED_TO_ALERT)
			System.out.println("** ALERT ** Driving too fast ! (" + speed + ")");
		else
			System.out.println("... nice and steady ... (" + speed + ")");
	}
}

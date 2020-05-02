package chapter8_1;

import java.util.Observable;

public class Speedometer extends Observable {
	int currentSpeed;
	
	public void setCurrentSpeed(int speed) {
		this.currentSpeed = speed;
		setChanged();
		notifyObservers();
	}
	public int getCurrentSpeed() {
		return this.currentSpeed;
	}
}
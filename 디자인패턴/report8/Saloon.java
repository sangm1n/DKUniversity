package chapter9;

import chapter7.AbstractCar;
import chapter7.Engine;

public class Saloon extends AbstractCar {
	public Saloon(Engine engine) {
		super(engine);
	}
	public int getPrice() {
		return 6000;
	}
}

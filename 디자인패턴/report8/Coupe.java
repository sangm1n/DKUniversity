package chapter9;

import chapter7.AbstractCar;
import chapter7.Engine;

public class Coupe extends AbstractCar {
	public Coupe(Engine engine) {
		super(engine);
	}
	public int getPrice() {
		return 7000;
	}
}

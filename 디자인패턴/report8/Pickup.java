package chapter9;

import chapter7.AbstractCar;
import chapter7.Engine;

public class Pickup extends AbstractVan {
	public Pickup(Engine engine) {
		super(engine);
	}
	public int getPrice() {
		return 9000;
	}
}
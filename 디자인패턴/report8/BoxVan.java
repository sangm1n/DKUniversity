package chapter9;

import chapter7.AbstractCar;
import chapter7.Engine;

public class BoxVan extends AbstractVan {
	public BoxVan(Engine engine) {
		super(engine);
	}
	public int getPrice() {
		return 10000;
	}
}
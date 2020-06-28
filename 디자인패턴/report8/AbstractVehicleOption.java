package chapter9;

import chapter7.AbstractVehicle;
import chapter7.Engine;

public abstract class AbstractVehicleOption extends AbstractVehicle {
	public AbstractVehicleOption(Engine engine, Colour colour) {
		super(engine, colour);
	}
}

package chapter9;

import chapter7.Vehicle;

public class AirConditionedVehicle extends AbstractVehicleOption {
	private Vehicle vehicle;
	
	public AirConditionedVehicle(Vehicle vehicle) {
		super(vehicle.getEngine(), vehicle.getColour());
		this.vehicle = vehicle;
	}
	public int getPrice() {
		return 600 + this.vehicle.getPrice();
	}
}

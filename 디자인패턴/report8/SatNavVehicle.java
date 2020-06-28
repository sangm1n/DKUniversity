package chapter9;

import chapter7.Vehicle;

public class SatNavVehicle extends AbstractVehicleOption {
	private Vehicle vehicle;
	
	public SatNavVehicle(Vehicle vehicle) {
		super(vehicle.getEngine(), vehicle.getColour());
		this.vehicle = vehicle;
	}
	public int getPrice() {
		return 1500 + this.vehicle.getPrice();
	}
}
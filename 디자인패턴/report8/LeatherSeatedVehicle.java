package chapter9;

import chapter7.Vehicle;

public class LeatherSeatedVehicle extends AbstractVehicleOption {
	private Vehicle vehicle;
	
	public LeatherSeatedVehicle(Vehicle vehicle) {
		super(vehicle.getEngine(), vehicle.getColour());
		this.vehicle = vehicle;
	}
	public int getPrice() {
		return 1200 + this.vehicle.getPrice();
	}
}
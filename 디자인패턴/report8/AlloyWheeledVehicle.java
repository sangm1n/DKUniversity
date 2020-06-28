package chapter9;

import chapter7.Vehicle;

public class AlloyWheeledVehicle extends AbstractVehicleOption {
	private Vehicle vehicle;
	
	public AlloyWheeledVehicle(Vehicle vehicle) {
		super(vehicle.getEngine(), vehicle.getColour());
		this.vehicle = vehicle;
	}
	public int getPrice() {
		return 250 + this.vehicle.getPrice();
	}
}
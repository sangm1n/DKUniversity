package chapter9;

import chapter7.Vehicle;
import chapter7.StandardEngine;

/*
 *  2020.05.06 Decorator Pattern

 *  by. sangmin
 */

public class Client {
	public static void main(String[] args) {
		Vehicle myCar = new Saloon(new StandardEngine(1300));
		myCar.paint(Vehicle.Colour.BLUE);
		System.out.println(myCar);
		
		myCar = new AirConditionedVehicle(myCar);
		System.out.println(myCar);
		
		myCar = new AlloyWheeledVehicle(myCar);
		System.out.println(myCar);

		myCar = new LeatherSeatedVehicle(myCar);
		System.out.println(myCar);

		myCar = new MetallicPaintedVehicle(myCar);
		System.out.println(myCar);

		myCar = new SatNavVehicle(myCar);
		System.out.println(myCar);
	}
}

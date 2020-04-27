package chapter7;

public class StandardGearboxStrategy implements GearBoxStrategy {
	public void ensureCorrectGear(Engine engine, int speed) {
		System.out.println("Working out correct gear at " + speed + "mph for a STANDARD gearbox");
	}
}

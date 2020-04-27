package chapter7;

public abstract class AbstractCar extends AbstractVehicle {
	GearBoxStrategy GBS;
	
	public AbstractCar(Engine engine) {
		super(engine);
		GBS = new StandardGearboxStrategy();
	}
	public void setGearboxStrategy(GearBoxStrategy gs) {
		this.GBS = gs;
	}
	public GearBoxStrategy getGearboxStrategy() {
		return GBS;
	}
	public void setSpeed(int speed) {
		GBS.ensureCorrectGear(getEngine(), speed);
	}
}

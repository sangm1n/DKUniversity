package chapter7;

public interface Vehicle {
	public enum Colour {UNPAINTED, BLUE, BLACK, GREEN, RED, SILVER, WHITE, YELLOW};
	public Engine getEngine();
	public Vehicle.Colour getColour();
	public void paint(Vehicle.Colour colour);
	public int getPrice();
}
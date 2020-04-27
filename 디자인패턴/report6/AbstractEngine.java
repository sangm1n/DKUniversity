package chapter7;

public abstract class AbstractEngine implements Engine {
	private int size;
	private boolean turbo;
	
	public AbstractEngine(int size, boolean turbo) {
		this.size = size;
		this.turbo = turbo;
	}
	public int getSize() {
		return this.size;
	}
	public boolean isTurbo() {
		return this.turbo;
	}
}


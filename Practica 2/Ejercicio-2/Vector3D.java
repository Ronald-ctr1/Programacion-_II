public class Vector3D {
    private double x, y, z;

    public Vector3D() {
        this.x = 0;
        this.y = 0;
        this.z = 0;
    }

    public Vector3D(double x, double y, double z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    public Vector3D add(Vector3D other) {
        return new Vector3D(this.x + other.x, this.y + other.y, this.z + other.z);
    }

    public Vector3D multiply(double scalar) {
        return new Vector3D(this.x * scalar, this.y * scalar, this.z * scalar);
    }

    public double magnitude() {
        return Math.sqrt(x * x + y * y + z * z);
    }

    public Vector3D normalize() {
        double mag = magnitude();
        if (mag == 0) {
            return new Vector3D(0, 0, 0);  
        }
        return new Vector3D(x / mag, y / mag, z / mag);
    }

    public double dot(Vector3D other) {
        return this.x * other.x + this.y * other.y + this.z * other.z;
    }

    public Vector3D cross(Vector3D other) {
        return new Vector3D(
            this.y * other.z - this.z * other.y,
            this.z * other.x - this.x * other.z,
            this.x * other.y - this.y * other.x
        );
    }

    public boolean isOrthogonalTo(Vector3D other) {
        return Math.abs(this.dot(other)) < 1e-9;
    }

    public boolean formsRectangleWith(Vector3D other) {
        double diagonal1 = this.add(other).magnitude();
        double diagonal2 = this.add(other.multiply(-1)).magnitude();
        return Math.abs(diagonal1 - diagonal2) < 1e-9;
    }

    public Vector3D projectionOn(Vector3D other) {
        double otherMagSquared = other.magnitude() * other.magnitude();
        if (otherMagSquared == 0) {
            return new Vector3D(0, 0, 0);
        }
        double scalar = this.dot(other) / otherMagSquared;
        return other.multiply(scalar);
    }

    public Vector3D orthogonalComponent(Vector3D other) {
        return this.add(projectionOn(other).multiply(-1));
    }

    @Override
    public String toString() {
        return String.format("(%.3f, %.3f, %.3f)", x, y, z);
    }
}

"""Convert the report's maximum engine speed from RPM into angular speed."""

import math


def speed_from_rpm(rpm):
    """Return rotational speed as (rad/s, revolutions/s)."""
    if rpm < 0:
        raise ValueError("Speed in RPM cannot be negative.")
    return rpm * 2 * math.pi / 60, rpm / 60


def main():
    rpm = 6800.0  # Maximum speed used in the report.
    omega, hz = speed_from_rpm(rpm)
    print("ENGINE ROTATIONAL SPEED")
    print(f"Engine speed: {rpm:.0f} rpm")
    print(f"Angular speed: {omega:.4f} rad/s")
    print(f"Rotational frequency: {hz:.4f} Hz")
    print("Excitation harmonics are not assessed in this conversion.")


if __name__ == "__main__":
    main()

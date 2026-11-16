"""Approximate a piston as a uniform solid cylinder, as in the report."""

import math


def piston_properties(density, diameter, height, offset):
    """Return mass and axial inertias: (kg, kg*m^2, kg*m^2).

    The last value shifts the cylinder's axial inertia to a parallel axis.
    This idealization is not a full crank-slider dynamic model.
    """
    if density <= 0 or diameter <= 0 or height <= 0 or offset < 0:
        raise ValueError("Density and dimensions must be positive; offset cannot be negative.")
    radius = diameter / 2
    mass = density * math.pi * radius**2 * height
    center_inertia = 0.5 * mass * radius**2
    shifted_inertia = center_inertia + mass * offset**2
    return mass, center_inertia, shifted_inertia


def main():
    density = 2710.0  # kg/m^3
    diameter = 0.072  # m
    height = 0.054  # m
    offset = 0.4  # m, illustrative value used in the report
    mass, center, shifted = piston_properties(density, diameter, height, offset)
    print("PISTON: IDEAL SOLID CYLINDER")
    print(f"Mass: {mass:.6f} kg")
    print(f"Inertia about cylinder axis: {center:.9f} kg*m^2")
    print(f"Inertia about shifted parallel axis: {shifted:.9f} kg*m^2")
    print("Example offset is an assumption, not a verified engine measurement.")


if __name__ == "__main__":
    main()

"""Approximate a counterweight as a uniform solid cylinder."""

import math


def counterweight_properties(density, diameter, thickness, offset):
    """Return mass, axial central inertia and shifted parallel-axis inertia."""
    if min(density, diameter, thickness) <= 0 or offset < 0:
        raise ValueError("Density and dimensions must be positive; offset cannot be negative.")
    radius = diameter / 2
    mass = density * math.pi * radius**2 * thickness
    center_inertia = 0.5 * mass * radius**2
    return mass, center_inertia, center_inertia + mass * offset**2


def main():
    density = 7750.0  # kg/m^3
    diameter = 0.05  # m
    thickness = 0.06  # m
    offset = 0.04  # m
    mass, center, shifted = counterweight_properties(density, diameter, thickness, offset)
    print("COUNTERWEIGHT: IDEAL SOLID CYLINDER")
    print(f"Mass: {mass:.6f} kg")
    print(f"Inertia about cylinder axis: {center:.9f} kg*m^2")
    print(f"Inertia about shifted parallel axis: {shifted:.9f} kg*m^2")


if __name__ == "__main__":
    main()

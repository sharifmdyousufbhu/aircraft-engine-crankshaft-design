"""Calculate the torsional stiffness of an ideal circular shaft."""

import math


def torsional_stiffness(shear_modulus, outer_diameter, length, inner_diameter=0.0):
    """Return (polar second moment in m^4, stiffness in N*m/rad)."""
    if shear_modulus <= 0 or outer_diameter <= 0 or length <= 0:
        raise ValueError("Modulus, diameter and length must be positive.")
    if inner_diameter < 0 or inner_diameter >= outer_diameter:
        raise ValueError("Inner diameter must be nonnegative and less than outer diameter.")
    polar_second_moment = math.pi * (outer_diameter**4 - inner_diameter**4) / 32
    return polar_second_moment, shear_modulus * polar_second_moment / length


def main():
    shear_modulus = 80e9  # Pa
    diameter = 0.05  # m
    length = 0.15  # m
    polar_moment, stiffness = torsional_stiffness(shear_modulus, diameter, length)
    print("IDEAL CIRCULAR SHAFT TORSIONAL STIFFNESS")
    print(f"Polar second moment: {polar_moment:.9e} m^4")
    print(f"Torsional stiffness: {stiffness:.3f} N*m/rad")


if __name__ == "__main__":
    main()

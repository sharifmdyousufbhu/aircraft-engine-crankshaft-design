"""Calculate the ideal circular-shaft torsional stress in the report."""

import math


def torsional_stress(torque, diameter):
    """Return (polar second moment in m^4, peak nominal shear stress in Pa)."""
    if diameter <= 0 or torque < 0:
        raise ValueError("Diameter must be positive and torque must be nonnegative.")
    polar_second_moment = math.pi * diameter**4 / 32
    shear_stress = torque * (diameter / 2) / polar_second_moment
    return polar_second_moment, shear_stress


def main():
    torque = 57.0  # N*m, as written in the report
    diameter = 0.05  # m
    ultimate_tensile_strength = 850e6  # Pa, report's assumed value
    estimated_tensile_endurance = ultimate_tensile_strength / 2
    polar_moment, shear_stress = torsional_stress(torque, diameter)
    ratio = estimated_tensile_endurance / shear_stress
    print("IDEAL SOLID-SHAFT TORSIONAL STRESS")
    print(f"Torque: {torque:.1f} N*m")
    print(f"Polar second moment: {polar_moment:.9e} m^4")
    print(f"Nominal torsional shear stress: {shear_stress / 1e6:.3f} MPa")
    print(f"Report's simple tensile-endurance/shear-stress ratio: {ratio:.1f}")
    print("The ratio is not a valid fatigue safety assessment for this crankshaft.")
    print("Combined stresses, fatigue criteria and service conditions require engineering review.")


if __name__ == "__main__":
    main()

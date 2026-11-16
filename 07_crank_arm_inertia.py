"""Estimate crank-arm mass and idealized inertia, following the report."""


def crank_arm_properties(density, length, width, thickness):
    """Return mass and m*L^2/3 (slender rod about an end axis).

    This is the report's idealization; the detailed arm shape, its actual
    rotation axis and the separate 0.010 m offset are not represented.
    """
    if min(density, length, width, thickness) <= 0:
        raise ValueError("Density and dimensions must be positive.")
    mass = density * length * width * thickness
    return mass, mass * length**2 / 3


def main():
    density = 7750.0  # kg/m^3
    length = 0.061  # m
    width = 0.02  # m
    thickness = 0.054  # m
    mass, inertia = crank_arm_properties(density, length, width, thickness)
    print("CRANK ARM: RECTANGULAR MASS, SLENDER-ROD INERTIA")
    print(f"Mass: {mass:.6f} kg")
    print(f"Approximate end-axis inertia: {inertia:.9f} kg*m^2")
    print("The report's 0.010 m offset is not modeled by this idealization.")


if __name__ == "__main__":
    main()

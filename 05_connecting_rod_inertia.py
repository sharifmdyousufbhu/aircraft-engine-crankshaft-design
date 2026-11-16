"""Approximate connecting-rod mass and inertia using the report's method."""


def connecting_rod_properties(density, length, width, thickness, offset):
    """Return mass and approximate shifted-axis inertia.

    Mass uses a rectangular solid. The central inertia uses m*L^2/12,
    a slender-rod approximation about an axis perpendicular to its length.
    """
    if min(density, length, width, thickness) <= 0 or offset < 0:
        raise ValueError("Density and dimensions must be positive; offset cannot be negative.")
    mass = density * length * width * thickness
    center_inertia = mass * length**2 / 12
    return mass, center_inertia, center_inertia + mass * offset**2


def main():
    density = 2710.0  # kg/m^3
    length = 0.10  # m
    width = 0.02  # m
    thickness = 0.03  # m
    offset = 0.5  # m, illustrative value used in the report
    mass, center, shifted = connecting_rod_properties(density, length, width, thickness, offset)
    print("CONNECTING ROD: RECTANGULAR MASS, SLENDER-ROD INERTIA")
    print(f"Mass: {mass:.6f} kg")
    print(f"Approximate inertia about center: {center:.9f} kg*m^2")
    print(f"Approximate inertia about shifted axis: {shifted:.9f} kg*m^2")
    print("Example geometry and offset are not verified engine measurements.")


if __name__ == "__main__":
    main()

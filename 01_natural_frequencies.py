"""Natural frequencies of the two-inertia example in the project report.

This is a small, idealized model. Its values do not establish the natural
frequencies of an actual aircraft engine.
"""

import math


def natural_frequencies(j1, j2, k1, k2):
    """Return lower and higher natural frequencies in rad/s.

    J is in kg*m^2 and K is in N*m/rad. The model uses stiffness matrix
    [[k1+k2, -k2], [-k2, k2]] and inertia matrix diag(j1, j2).
    An analytical solution of the corresponding symmetric 2x2 problem
    keeps this example independent of third-party libraries.
    """
    if j1 <= 0 or j2 <= 0:
        raise ValueError("Moments of inertia must be positive.")
    if k1 <= 0 or k2 <= 0:
        raise ValueError("Spring constants must be positive.")
    a = (k1 + k2) / j1
    b = -k2 / math.sqrt(j1 * j2)
    d = k2 / j2
    difference = math.hypot(a - d, 2 * b)
    eigenvalues = ((a + d - difference) / 2, (a + d + difference) / 2)
    if min(eigenvalues) < 0:
        raise ValueError("The parameters produced a negative eigenvalue.")
    return tuple(math.sqrt(value) for value in eigenvalues)


def main():
    # These are the report's explicitly supplied inputs. They are not derived
    # from the recalculated component inertias in the other files.
    j1 = j2 = 0.1692394
    k1 = k2 = 327249.0
    print("TWO-INERTIA NATURAL FREQUENCIES (REPORT INPUTS)")
    for mode, omega in enumerate(natural_frequencies(j1, j2, k1, k2), start=1):
        print(f"Mode {mode}: {omega:.3f} rad/s  ({omega / (2 * math.pi):.3f} Hz)")
    print("These values are for an idealized two-inertia model only.")


if __name__ == "__main__":
    main()

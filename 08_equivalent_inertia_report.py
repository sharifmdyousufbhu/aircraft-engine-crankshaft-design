"""Reproduce the equivalent-inertia arithmetic written in the report.

This is retained for traceability, not endorsed as an engineering model.
The report subtracts counterweight inertia. A proper dynamic equivalent
inertia for a crank-slider system needs a separately justified derivation.
"""


def reported_equivalent_inertia(piston, crank_arm, connecting_rod, counterweight):
    """Return exactly the report's arithmetic, including its subtraction."""
    return piston + crank_arm + connecting_rod - counterweight


def main():
    # Values copied from the equivalent-inertia example in the PDF, rather
    # than the separately corrected component calculations in files 04-07.
    piston = 0.096435  # kg*m^2
    crank_arm = 0.000633  # kg*m^2
    connecting_rod = 0.07341  # kg*m^2
    counterweight = 0.0012386  # kg*m^2
    inertia = reported_equivalent_inertia(piston, crank_arm, connecting_rod, counterweight)
    print("EQUIVALENT INERTIA: REPORT ARITHMETIC ONLY")
    print(f"Report formula result: {inertia:.7f} kg*m^2")
    print("This reproduces the report's subtraction; it is not a validated dynamic model.")
    print("The component values here are not the recalculated values in scripts 04-07.")


if __name__ == "__main__":
    main()

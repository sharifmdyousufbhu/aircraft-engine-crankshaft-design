# Aircraft Engine Crankshaft: Preliminary Calculations

This repository contains Python examples reconstructed from the calculations in an Idaho State University academic project report on the crankshaft of a Rotax 503UL DCDI aircraft engine. The examples cover an idealized two-inertia model, shaft stiffness, component inertias, engine speed, and simple torsional stress.

**Project status:** These are report-based educational calculations, not a verified crankshaft design or a complete vibration simulation. The scripts use assumed geometry and simplified shapes. They must not be used to design, manufacture, certify, or operate aircraft components.

## Contents

| File | What it calculates |
| --- | --- |
| `01_natural_frequencies.py` | Two natural frequencies for the report's two-inertia, two-spring model. |
| `02_engine_rotation.py` | Engine speed in revolutions per minute, radians per second, and hertz. |
| `03_shaft_torsional_stiffness.py` | Polar second moment and ideal shaft torsional stiffness. |
| `04_piston_inertia.py` | Approximate piston mass and inertia using a solid cylinder. |
| `05_connecting_rod_inertia.py` | Approximate connecting-rod mass and inertia. |
| `06_counterweight_inertia.py` | Approximate counterweight mass and inertia using a solid cylinder. |
| `07_crank_arm_inertia.py` | Approximate crank-arm mass and inertia. |
| `08_equivalent_inertia_report.py` | Reproduces the report's equivalent-inertia arithmetic, with a warning. |
| `09_torsional_stress.py` | Nominal shear stress in an ideal solid circular shaft. |
| `run_all.py` | Runs the nine calculation examples in order. |
| `sample_output.txt` | Example output from running all nine scripts. |

## Project report

The report is a separate PDF. If it is available to you and you have permission to share it, add it to this repository as `Crankshaft_Project_Report.pdf`. Review the cover page and third-party material before making the repository public.

## Requirements

- Python 3.8 or newer.
- No extra Python libraries are required; all scripts use the Python standard library.

The report's original examples use NumPy in places. These reconstructed scripts use standard-library formulas to make them easier to run. They are not the original source files.

## How to run the calculations

Open a terminal in the folder containing these files. On Windows, run:

```powershell
py run_all.py
```

Or, on systems where Python is started with `python` or `python3`:

```bash
python run_all.py
```

To run one example at a time, use its file name, for example:

```powershell
py 01_natural_frequencies.py
```

In VS Code, open the folder with **File → Open Folder**, select a Python interpreter, then use **Terminal → New Terminal** and run one of the commands above.

## Source, corrections, and important limitations

These files were reconstructed from code snippets and calculations embedded in the project report. The original stand-alone Python files were not provided. Some variable references and outputs in the report are inconsistent, so the runnable calculations do not reproduce every printed number in the PDF:

1. **Piston:** The report's snippet defines an aluminum density but refers to a steel-density variable for the central inertia. `04_piston_inertia.py` consistently uses the stated aluminum density for both mass and inertia.
2. **Connecting rod:** The report's snippet gives a thickness but passes a variable named `height` to the mass calculation. `05_connecting_rod_inertia.py` uses the stated thickness of 0.03 m. The resulting mass and inertia therefore differ from the report's output.
3. **Counterweight:** The report's counterweight snippet uses a `mass` variable without calculating it in that snippet. `06_counterweight_inertia.py` calculates the mass from the counterweight's stated density and dimensions before applying the parallel-axis formula.
4. **Crank arm:** The reported formula approximates the arm as a slender rod about one end. The separate 0.010 m offset mentioned in the report is not represented by that formula.
5. **Equivalent inertia:** The report adds piston, rod, and crank-arm inertias, then subtracts the counterweight inertia. `08_equivalent_inertia_report.py` preserves that arithmetic only to show what the report calculated. The subtraction is not a validated dynamic derivation; a crank-slider model requires an appropriate physical derivation. The report's component values used in that file are not the corrected outputs of scripts 04–07.
6. **Natural frequencies:** `01_natural_frequencies.py` uses the report's explicitly supplied values `J1 = J2 = 0.1692394 kg*m^2` and `K1 = K2 = 327249 N*m/rad`. It does **not** use the recalculated component values from scripts 04–07. Therefore, it reproduces the stated idealized model rather than validating those component calculations.
7. **Torsional stress:** Using the report's stated 57 N*m torque and 50 mm diameter gives approximately 2.322 MPa, whereas the report lists 2.28 MPa. The report divides an estimated tensile endurance limit by nominal torsional shear stress; that ratio is shown only to trace its arithmetic and is **not** a valid fatigue safety assessment.
8. **Vibration limits:** Engine speed in hertz is not the same as a complete excitation spectrum. Combustion, firing orders, harmonics, damping, support conditions, changing loads, and other effects are not analyzed here.

The piston and connecting-rod offsets of 0.4 m and 0.5 m are report example inputs, not verified engine dimensions. The solid-cylinder and slender-rod approximations do not fully represent reciprocating or rotating engine components.

## Academic context

The source report is an Idaho State University academic project. Confirm authorship, permissions, and the accuracy of all project claims before sharing publicly.

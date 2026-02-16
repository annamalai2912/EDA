
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

def standard_resistor_case():
    """
    Standard Resistor Case Study (Unit 5 Syllabus).
    Simulate a batch of 1000 resistors (Nominal = 1000 Ohms, Tolerance = 5%).
    Analyze the distribution.
    """
    print("\n--- Standard Resistor Simulation (Case Study 2) ---")
    np.random.seed(123)
    n = 1000
    nominal = 1000
    tolerance = 0.05
    
    # Generate Normal Distribution
    # 5% (tolerance) corresponds to roughly 3 Sigma for most manufacturers
    sigma = (nominal * tolerance) / 3
    resistors = np.random.normal(nominal, sigma, n)
    
    # Check bounds
    lsl, usl = nominal * (1 - tolerance), nominal * (1 + tolerance)
    out_of_spec = np.sum((resistors < lsl) | (resistors > usl))
    
    print(f"Nominal: {nominal}, Tolerance: {descriptor:.1f}%")
    print(f"LSL: {lsl}, USL: {usl}")
    print(f"Out of Spec Resistors: {out_of_spec} / {n}")
    
    # EDA
    plt.figure()
    plt.hist(resistors, bins=50, alpha=0.7, color='orange', edgecolor='black')
    plt.axvline(lsl, color='r', linestyle='--', label='LSL (Lower Spec Limit)')
    plt.axvline(usl, color='r', linestyle='--', label='USL (Upper Spec Limit)')
    plt.title(f"Standard Resistor Distribution (N={n})")
    plt.legend()
    plt.savefig('resistor_simulation.png')
    print("Saved resistor simulation plot.")

def heat_flow_meter_case():
    """
    Heat Flow Meter Case Study (Unit 5 Syllabus).
    Simulate calibration curve: Relationship between Heat Flux (q) and EMF (V).
    q = C * V + Error
    """
    print("\n--- Heat Flow Meter Simulation (Case Study 3) ---")
    np.random.seed(456)
    n = 20
    
    V = np.linspace(0, 10, n) # EMF (mV)
    C = 2.5 # Calibration Constant (W/m2/mV)
    
    # Simple linear relationship + Some noise
    q = C * V + np.random.normal(0, 0.5, n)
    
    # Add non-linearity (Sensor Drift/Saturation) at high values
    q[-5:] = q[-5:] - np.linspace(0, 2, 5) # Drift downwards
    
    # Analyze Residuals (EDA Approach)
    slope, intercept, _, _, _ = stats.linregress(V, q)
    predicted = slope * V + intercept
    residuals = q - predicted
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10))
    
    ax1.scatter(V, q, color='blue')
    ax1.plot(V, predicted, 'r--', label=f'Fit: q={slope:.2f}V + {intercept:.2f}')
    ax1.set_title("Calibration Curve (Heat Flux vs EMF)")
    ax1.set_xlabel("EMF (V)")
    ax1.set_ylabel("Heat Flux (q)")
    ax1.legend()
    
    ax2.scatter(V, residuals, color='green')
    ax2.axhline(0, color='black', linestyle='--')
    ax2.set_title("Residual Plot (Check for Non-Linearity)")
    ax2.set_ylabel("Residuals (Observed - Predicted)")
    
    plt.tight_layout()
    plt.savefig('heat_flow_residuals.png')
    print("Saved heat flow residual plot. Notice the drift at the end!")

if __name__ == "__main__":
    descriptor = 5.0
    standard_resistor_case()
    heat_flow_meter_case()

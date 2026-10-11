"""Chapter registry: slug -> (code, title, quota).
Quotas are the number of questions kept per chapter in the final bank (600 P / 600 C / 300 M).
They follow how many questions each chapter received across JEE Main Jan 2025, Apr 2025 and Jan 2026
(a proxy for weightage in the current syllabus), capped by what is available; chapters dropped from
the JEE Main syllabus in 2024 get a small fixed quota."""

PHYSICS = [
    ("units-measurements", "UNT", "Units, Dimensions & Errors", 28),
    ("kinematics", "KIN", "Kinematics", 24),
    ("laws-of-motion", "LOM", "Laws of Motion & Friction", 15),
    ("work-energy-power", "WEP", "Work, Energy & Power", 20),
    ("centre-of-mass-collisions", "COM", "Centre of Mass & Collisions", 9),
    ("rotational-motion", "ROT", "Rotational Motion", 40),
    ("gravitation", "GRV", "Gravitation", 14),
    ("properties-of-matter", "POM", "Elasticity, Fluids, Surface Tension & Viscosity", 37),
    ("heat-transfer", "HET", "Calorimetry, Thermal Expansion & Heat Transfer", 14),
    ("thermodynamics", "THD", "Thermodynamics", 32),
    ("kinetic-theory", "KTG", "Kinetic Theory of Gases", 11),
    ("oscillations", "SHM", "Oscillations (SHM)", 16),
    ("waves-sound", "WAV", "Waves & Sound", 16),
    ("electrostatics", "ELS", "Electrostatics", 44),
    ("capacitors", "CAP", "Capacitors", 20),
    ("current-electricity", "CUR", "Current Electricity", 34),
    ("magnetism", "MAG", "Magnetic Effects of Current & Magnetism", 32),
    ("emi", "EMI", "Electromagnetic Induction", 16),
    ("alternating-current", "ACC", "Alternating Current", 13),
    ("em-waves", "EMW", "Electromagnetic Waves", 17),
    ("ray-optics", "RAY", "Ray Optics & Optical Instruments", 52),
    ("wave-optics", "WOP", "Wave Optics", 25),
    ("dual-nature", "DUL", "Dual Nature of Matter & Radiation", 22),
    ("atoms-nuclei", "ATN", "Atoms & Nuclei", 27),
    ("semiconductors", "SEM", "Semiconductors & Electronic Devices", 15),
    ("experimental-physics", "EXP", "Experimental Skills", 7),
]

CHEMISTRY = [
    ("mole-concept", "MOL", "Mole Concept & Stoichiometry", 22),
    ("atomic-structure", "ATS", "Atomic Structure", 29),
    ("chemical-thermodynamics", "CTH", "Chemical Thermodynamics", 34),
    ("chemical-equilibrium", "CEQ", "Chemical Equilibrium", 13),
    ("ionic-equilibrium", "ION", "Ionic Equilibrium", 16),
    ("electrochemistry", "ELC", "Redox & Electrochemistry", 38),
    ("chemical-kinetics", "KIN", "Chemical Kinetics", 30),
    ("solutions", "SOL", "Solutions & Colligative Properties", 29),
    ("solid-state", "SLD", "Solid State", 4),
    ("gaseous-state", "GAS", "Gaseous State", 3),
    ("surface-chemistry", "SRF", "Surface Chemistry", 5),
    ("periodic-table", "PER", "Periodic Table & Periodicity", 27),
    ("chemical-bonding", "BND", "Chemical Bonding & Molecular Structure", 28),
    ("coordination-compounds", "COO", "Coordination Compounds", 47),
    ("d-f-block", "DFB", "d- and f-Block Elements", 30),
    ("p-block", "PBL", "p-Block Elements", 19),
    ("s-block", "SBL", "s-Block Elements", 6),
    ("metallurgy", "MET", "General Principles of Metallurgy", 5),
    ("inorganic-misc", "INM", "Hydrogen, Environmental Chemistry & Salt Analysis", 10),
    ("iupac-isomerism", "ISO", "IUPAC Nomenclature & Isomerism", 12),
    ("goc", "GOC", "General Organic Chemistry", 51),
    ("hydrocarbons", "HYD", "Hydrocarbons", 16),
    ("haloalkanes-haloarenes", "HAL", "Haloalkanes & Haloarenes", 21),
    ("alcohols-phenols-ethers", "ALC", "Alcohols, Phenols & Ethers", 19),
    ("aldehydes-ketones", "ALD", "Aldehydes & Ketones", 17),
    ("carboxylic-acids", "CAR", "Carboxylic Acids & Derivatives", 4),
    ("amines", "AMN", "Amines & Diazonium Salts", 29),
    ("biomolecules", "BIO", "Biomolecules", 25),
    ("polymers-everyday", "POL", "Polymers & Chemistry in Everyday Life", 3),
    ("practical-organic", "PRO", "Practical Organic Chemistry", 8),
]

MATHS = [
    ("sets-relations-functions", "SRF", "Sets, Relations & Functions", 25),
    ("complex-numbers", "CMP", "Complex Numbers", 11),
    ("quadratic-equations", "QDR", "Quadratic Equations & Inequalities", 10),
    ("sequences-series", "SEQ", "Sequences & Series", 19),
    ("permutations-combinations", "PNC", "Permutations & Combinations", 13),
    ("binomial-theorem", "BIN", "Binomial Theorem", 13),
    ("matrices-determinants", "MAT", "Matrices & Determinants", 20),
    ("trigonometry", "TRG", "Trigonometry & Inverse Trigonometry", 16),
    ("straight-lines", "STL", "Straight Lines", 11),
    ("circles", "CIR", "Circles", 7),
    ("conic-sections", "CON", "Parabola, Ellipse & Hyperbola", 28),
    ("limits-continuity-differentiability", "LCD", "Limits, Continuity & Differentiability", 14),
    ("application-of-derivatives", "AOD", "Differentiation & Application of Derivatives", 8),
    ("indefinite-integration", "INT", "Indefinite Integration", 5),
    ("definite-integration", "DEF", "Definite Integration", 15),
    ("area-under-curves", "ARE", "Area Under Curves", 12),
    ("differential-equations", "DIF", "Differential Equations", 13),
    ("vectors", "VEC", "Vectors", 15),
    ("three-d-geometry", "TDG", "3D Geometry", 21),
    ("probability", "PRB", "Probability", 13),
    ("statistics", "STA", "Statistics", 6),
    ("mathematical-reasoning", "MRE", "Mathematical Reasoning", 5),
]

SUBJECTS = {
    "physics": ("P", PHYSICS, 600),
    "chemistry": ("C", CHEMISTRY, 600),
    "maths": ("M", MATHS, 300),
}

if __name__ == "__main__":
    for name, (_, chapters, target) in SUBJECTS.items():
        total = sum(c[3] for c in chapters)
        print(f"{name}: {total} (target {target})")
        assert total == target, name

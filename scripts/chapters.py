"""Chapter registry: slug -> (subject, code, title, quota).
Quotas allocate 400 physics / 400 chemistry / 200 maths questions in proportion to
how heavily each chapter is examined (marks per chapter over recent JEE Main sessions)."""

PHYSICS = [
    ("units-measurements", "UNT", "Units, Dimensions & Errors", 8),
    ("kinematics", "KIN", "Kinematics", 16),
    ("laws-of-motion", "LOM", "Laws of Motion & Friction", 16),
    ("work-energy-power", "WEP", "Work, Energy & Power", 14),
    ("centre-of-mass-collisions", "COM", "Centre of Mass & Collisions", 12),
    ("rotational-motion", "ROT", "Rotational Motion", 24),
    ("gravitation", "GRV", "Gravitation", 14),
    ("properties-of-matter", "POM", "Elasticity, Fluids, Surface Tension & Viscosity", 18),
    ("heat-transfer", "HET", "Calorimetry, Thermal Expansion & Heat Transfer", 10),
    ("thermodynamics", "THD", "Thermodynamics", 18),
    ("kinetic-theory", "KTG", "Kinetic Theory of Gases", 12),
    ("oscillations", "SHM", "Oscillations (SHM)", 18),
    ("waves-sound", "WAV", "Waves & Sound", 16),
    ("electrostatics", "ELS", "Electrostatics", 24),
    ("capacitors", "CAP", "Capacitors", 12),
    ("current-electricity", "CUR", "Current Electricity", 26),
    ("magnetism", "MAG", "Magnetic Effects of Current & Magnetism", 22),
    ("emi", "EMI", "Electromagnetic Induction", 14),
    ("alternating-current", "ACC", "Alternating Current", 10),
    ("em-waves", "EMW", "Electromagnetic Waves", 8),
    ("ray-optics", "RAY", "Ray Optics & Optical Instruments", 20),
    ("wave-optics", "WOP", "Wave Optics", 14),
    ("dual-nature", "DUL", "Dual Nature of Matter & Radiation", 14),
    ("atoms-nuclei", "ATN", "Atoms & Nuclei", 20),
    ("semiconductors", "SEM", "Semiconductors & Electronic Devices", 16),
    ("experimental-physics", "EXP", "Experimental Skills", 4),
]

CHEMISTRY = [
    ("mole-concept", "MOL", "Mole Concept & Stoichiometry", 12),
    ("atomic-structure", "ATS", "Atomic Structure", 14),
    ("chemical-thermodynamics", "CTH", "Chemical Thermodynamics", 16),
    ("chemical-equilibrium", "CEQ", "Chemical Equilibrium", 12),
    ("ionic-equilibrium", "ION", "Ionic Equilibrium", 14),
    ("electrochemistry", "ELC", "Redox & Electrochemistry", 20),
    ("chemical-kinetics", "KIN", "Chemical Kinetics", 14),
    ("solutions", "SOL", "Solutions & Colligative Properties", 14),
    ("solid-state", "SLD", "Solid State", 6),
    ("gaseous-state", "GAS", "Gaseous State", 6),
    ("surface-chemistry", "SRF", "Surface Chemistry", 2),
    ("periodic-table", "PER", "Periodic Table & Periodicity", 10),
    ("chemical-bonding", "BND", "Chemical Bonding & Molecular Structure", 28),
    ("coordination-compounds", "COO", "Coordination Compounds", 26),
    ("d-f-block", "DFB", "d- and f-Block Elements", 16),
    ("p-block", "PBL", "p-Block Elements", 30),
    ("s-block", "SBL", "s-Block Elements", 6),
    ("metallurgy", "MET", "General Principles of Metallurgy", 6),
    ("inorganic-misc", "INM", "Hydrogen, Environmental Chemistry & Salt Analysis", 8),
    ("iupac-isomerism", "ISO", "IUPAC Nomenclature & Isomerism", 12),
    ("goc", "GOC", "General Organic Chemistry", 26),
    ("hydrocarbons", "HYD", "Hydrocarbons", 14),
    ("haloalkanes-haloarenes", "HAL", "Haloalkanes & Haloarenes", 12),
    ("alcohols-phenols-ethers", "ALC", "Alcohols, Phenols & Ethers", 16),
    ("aldehydes-ketones", "ALD", "Aldehydes & Ketones", 16),
    ("carboxylic-acids", "CAR", "Carboxylic Acids & Derivatives", 8),
    ("amines", "AMN", "Amines & Diazonium Salts", 12),
    ("biomolecules", "BIO", "Biomolecules", 12),
    ("polymers-everyday", "POL", "Polymers & Chemistry in Everyday Life", 4),
    ("practical-organic", "PRO", "Practical Organic Chemistry", 8),
]

MATHS = [
    ("sets-relations-functions", "SRF", "Sets, Relations & Functions", 8),
    ("complex-numbers", "CMP", "Complex Numbers", 11),
    ("quadratic-equations", "QDR", "Quadratic Equations & Inequalities", 8),
    ("sequences-series", "SEQ", "Sequences & Series", 10),
    ("permutations-combinations", "PNC", "Permutations & Combinations", 8),
    ("binomial-theorem", "BIN", "Binomial Theorem", 8),
    ("matrices-determinants", "MAT", "Matrices & Determinants", 12),
    ("trigonometry", "TRG", "Trigonometry & Inverse Trigonometry", 8),
    ("straight-lines", "STL", "Straight Lines", 8),
    ("circles", "CIR", "Circles", 8),
    ("conic-sections", "CON", "Parabola, Ellipse & Hyperbola", 12),
    ("limits-continuity-differentiability", "LCD", "Limits, Continuity & Differentiability", 14),
    ("application-of-derivatives", "AOD", "Differentiation & Application of Derivatives", 12),
    ("indefinite-integration", "INT", "Indefinite Integration", 4),
    ("definite-integration", "DEF", "Definite Integration", 12),
    ("area-under-curves", "ARE", "Area Under Curves", 8),
    ("differential-equations", "DIF", "Differential Equations", 10),
    ("vectors", "VEC", "Vectors", 8),
    ("three-d-geometry", "TDG", "3D Geometry", 10),
    ("probability", "PRB", "Probability", 13),
    ("statistics", "STA", "Statistics", 6),
    ("mathematical-reasoning", "MRE", "Mathematical Reasoning", 2),
]

SUBJECTS = {
    "physics": ("P", PHYSICS, 400),
    "chemistry": ("C", CHEMISTRY, 400),
    "maths": ("M", MATHS, 200),
}

if __name__ == "__main__":
    for name, (_, chapters, target) in SUBJECTS.items():
        total = sum(c[3] for c in chapters)
        print(f"{name}: {total} (target {target})")
        assert total == target, name

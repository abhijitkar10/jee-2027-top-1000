"""Chapter registry: slug -> (subject, code, title, count).
Counts are the delivered questions per chapter. They started as weightage-based quotas
(marks per chapter over recent JEE Main sessions) and were then adjusted to what could be
sourced and verified."""

PHYSICS = [
    ("units-measurements", "UNT", "Units, Dimensions & Errors", 11),
    ("kinematics", "KIN", "Kinematics", 25),
    ("laws-of-motion", "LOM", "Laws of Motion & Friction", 21),
    ("work-energy-power", "WEP", "Work, Energy & Power", 14),
    ("centre-of-mass-collisions", "COM", "Centre of Mass & Collisions", 7),
    ("rotational-motion", "ROT", "Rotational Motion", 17),
    ("gravitation", "GRV", "Gravitation", 19),
    ("properties-of-matter", "POM", "Elasticity, Fluids, Surface Tension & Viscosity", 27),
    ("heat-transfer", "HET", "Calorimetry, Thermal Expansion & Heat Transfer", 3),
    ("thermodynamics", "THD", "Thermodynamics", 13),
    ("kinetic-theory", "KTG", "Kinetic Theory of Gases", 15),
    ("oscillations", "SHM", "Oscillations (SHM)", 12),
    ("waves-sound", "WAV", "Waves & Sound", 11),
    ("electrostatics", "ELS", "Electrostatics", 19),
    ("capacitors", "CAP", "Capacitors", 6),
    ("current-electricity", "CUR", "Current Electricity", 26),
    ("magnetism", "MAG", "Magnetic Effects of Current & Magnetism", 22),
    ("emi", "EMI", "Electromagnetic Induction", 13),
    ("alternating-current", "ACC", "Alternating Current", 19),
    ("em-waves", "EMW", "Electromagnetic Waves", 14),
    ("ray-optics", "RAY", "Ray Optics & Optical Instruments", 14),
    ("wave-optics", "WOP", "Wave Optics", 19),
    ("dual-nature", "DUL", "Dual Nature of Matter & Radiation", 16),
    ("atoms-nuclei", "ATN", "Atoms & Nuclei", 30),
    ("semiconductors", "SEM", "Semiconductors & Electronic Devices", 3),
    ("experimental-physics", "EXP", "Experimental Skills", 4),
]

CHEMISTRY = [
    ("mole-concept", "MOL", "Mole Concept & Stoichiometry", 16),
    ("atomic-structure", "ATS", "Atomic Structure", 15),
    ("chemical-thermodynamics", "CTH", "Chemical Thermodynamics", 18),
    ("chemical-equilibrium", "CEQ", "Chemical Equilibrium", 11),
    ("ionic-equilibrium", "ION", "Ionic Equilibrium", 10),
    ("electrochemistry", "ELC", "Redox & Electrochemistry", 29),
    ("chemical-kinetics", "KIN", "Chemical Kinetics", 18),
    ("solutions", "SOL", "Solutions & Colligative Properties", 20),
    ("solid-state", "SLD", "Solid State", 0),
    ("gaseous-state", "GAS", "Gaseous State", 1),
    ("surface-chemistry", "SRF", "Surface Chemistry", 0),
    ("periodic-table", "PER", "Periodic Table & Periodicity", 19),
    ("chemical-bonding", "BND", "Chemical Bonding & Molecular Structure", 36),
    ("coordination-compounds", "COO", "Coordination Compounds", 35),
    ("d-f-block", "DFB", "d- and f-Block Elements", 26),
    ("p-block", "PBL", "p-Block Elements", 29),
    ("s-block", "SBL", "s-Block Elements", 1),
    ("metallurgy", "MET", "General Principles of Metallurgy", 2),
    ("inorganic-misc", "INM", "Hydrogen, Environmental Chemistry & Salt Analysis", 11),
    ("iupac-isomerism", "ISO", "IUPAC Nomenclature & Isomerism", 10),
    ("goc", "GOC", "General Organic Chemistry", 13),
    ("hydrocarbons", "HYD", "Hydrocarbons", 4),
    ("haloalkanes-haloarenes", "HAL", "Haloalkanes & Haloarenes", 10),
    ("alcohols-phenols-ethers", "ALC", "Alcohols, Phenols & Ethers", 12),
    ("aldehydes-ketones", "ALD", "Aldehydes & Ketones", 8),
    ("carboxylic-acids", "CAR", "Carboxylic Acids & Derivatives", 3),
    ("amines", "AMN", "Amines & Diazonium Salts", 14),
    ("biomolecules", "BIO", "Biomolecules", 16),
    ("polymers-everyday", "POL", "Polymers & Chemistry in Everyday Life", 3),
    ("practical-organic", "PRO", "Practical Organic Chemistry", 10),
]

MATHS = [
    ("sets-relations-functions", "SRF", "Sets, Relations & Functions", 9),
    ("complex-numbers", "CMP", "Complex Numbers", 9),
    ("quadratic-equations", "QDR", "Quadratic Equations & Inequalities", 8),
    ("sequences-series", "SEQ", "Sequences & Series", 11),
    ("permutations-combinations", "PNC", "Permutations & Combinations", 9),
    ("binomial-theorem", "BIN", "Binomial Theorem", 8),
    ("matrices-determinants", "MAT", "Matrices & Determinants", 12),
    ("trigonometry", "TRG", "Trigonometry & Inverse Trigonometry", 8),
    ("straight-lines", "STL", "Straight Lines", 8),
    ("circles", "CIR", "Circles", 8),
    ("conic-sections", "CON", "Parabola, Ellipse & Hyperbola", 12),
    ("limits-continuity-differentiability", "LCD", "Limits, Continuity & Differentiability", 14),
    ("application-of-derivatives", "AOD", "Differentiation & Application of Derivatives", 12),
    ("indefinite-integration", "INT", "Indefinite Integration", 1),
    ("definite-integration", "DEF", "Definite Integration", 13),
    ("area-under-curves", "ARE", "Area Under Curves", 8),
    ("differential-equations", "DIF", "Differential Equations", 10),
    ("vectors", "VEC", "Vectors", 9),
    ("three-d-geometry", "TDG", "3D Geometry", 11),
    ("probability", "PRB", "Probability", 14),
    ("statistics", "STA", "Statistics", 6),
    ("mathematical-reasoning", "MRE", "Mathematical Reasoning", 0),
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

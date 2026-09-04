from rdkit import Chem
from rdkit.Chem import Descriptors

# 1. Input & Parsing Matrix
smiles_input = "CCO"
mol = Chem.MolFromSmiles(smiles_input)

if mol:
    # 2. Standardized Global Key Generation
    inchi_string = Chem.MolToInChI(mol)
    print(f"Standardized InChI Line: {inchi_string}")
    
    # 3. Fixed-Length Hashed InChIKey (For 24/7 Fast Search Indexes)
    inchikey_string = Chem.InChIToInChIKey(inchi_string)
    print(f"Global InChIKey Hash  : {inchikey_string}")
    
    # 4. Computing Core Molecular Descriptors (Quantitative Analytics)
    mol_weight = Descriptors.MolWt(mol)          # Calculate precise Molecular Weight
    log_p = Descriptors.MolLogP(mol)            # Calculate octanol-water partition coefficient
    h_donors = Descriptors.NumHDonors(mol)       # Hydrogen bond donors count
    h_acceptors = Descriptors.NumHAcceptors(mol) # Hydrogen bond acceptors count
    
    print("\n📊 Molecular Blueprint Analytical Metrics:")
    print(f"   - Exact Molecular Weight : {mol_weight:.3f} g/mol")
    print(f"   - Calculated LogP Metric  : {log_p:.3f}")
    print(f"   - H-Bond Donors / Acceptors: {h_donors} / {h_acceptors}")

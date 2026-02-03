#!/usr/bin/env python3
"""
Quick test to verify replication package works correctly
"""
import pandas as pd
import os

def test_data_files():
    """Test that data files exist and can be loaded"""
    print("="*70)
    print("TESTING DATA FILES")
    print("="*70)
    
    # Check cleaned_data_full.csv
    path1 = 'data/cleaned_data_full.csv'
    assert os.path.exists(path1), f"Missing: {path1}"
    df1 = pd.read_csv(path1)
    print(f"✓ cleaned_data_full.csv loaded: N={len(df1)}, {df1.shape[1]} columns")
    
    # Check cleaned_data.csv
    path2 = 'data/cleaned_data.csv'
    assert os.path.exists(path2), f"Missing: {path2}"
    df2 = pd.read_csv(path2)
    print(f"✓ cleaned_data.csv loaded: N={len(df2)}, {df2.shape[1]} columns")
    
    # Verify TAM items exist
    tam_items = [col for col in df2.columns if col.startswith(('PU', 'PEOU', 'PE', 'PS', 'BI'))]
    assert len(tam_items) == 15, f"Expected 15 TAM items, found {len(tam_items)}"
    print(f"✓ All 15 TAM items present: {tam_items}")
    
    print("\n✓ Data files test PASSED\n")
    return True

def test_directories():
    """Test that all required directories exist"""
    print("="*70)
    print("TESTING DIRECTORY STRUCTURE")
    print("="*70)
    
    dirs = ['data', 'notebooks', 'outputs', 'figures']
    for d in dirs:
        assert os.path.exists(d), f"Missing directory: {d}"
        print(f"✓ {d}/ exists")
    
    print("\n✓ Directory structure test PASSED\n")
    return True

def test_notebooks():
    """Test that all notebooks exist"""
    print("="*70)
    print("TESTING NOTEBOOKS")
    print("="*70)
    
    notebooks = [
        'notebooks/01_descriptives_and_correlations.ipynb',
        'notebooks/02_exploratory_factor_analysis.ipynb',
        'notebooks/03_regression_analysis.ipynb'
    ]
    
    for nb in notebooks:
        assert os.path.exists(nb), f"Missing notebook: {nb}"
        print(f"✓ {os.path.basename(nb)} exists")
    
    print("\n✓ Notebooks test PASSED\n")
    return True

def test_documentation():
    """Test that documentation files exist"""
    print("="*70)
    print("TESTING DOCUMENTATION")
    print("="*70)
    
    docs = ['README.md', 'requirements.txt', 'LICENSE']
    for doc in docs:
        assert os.path.exists(doc), f"Missing: {doc}"
        print(f"✓ {doc} exists")
    
    print("\n✓ Documentation test PASSED\n")
    return True

if __name__ == '__main__':
    print("\n" + "="*70)
    print("REPLICATION PACKAGE VERIFICATION")
    print("="*70 + "\n")
    
    try:
        test_directories()
        test_data_files()
        test_notebooks()
        test_documentation()
        
        print("="*70)
        print("✓✓✓ ALL TESTS PASSED ✓✓✓")
        print("="*70)
        print("\nReplication package is ready to use!")
        print("\nNext steps:")
        print("  1. Install requirements: pip install -r requirements.txt")
        print("  2. Start Jupyter: jupyter notebook")
        print("  3. Run notebooks in order: 01, 02, 03")
        print("="*70 + "\n")
        
    except AssertionError as e:
        print(f"\n❌ TEST FAILED: {e}\n")
        exit(1)
    except Exception as e:
        print(f"\n❌ UNEXPECTED ERROR: {e}\n")
        exit(1)

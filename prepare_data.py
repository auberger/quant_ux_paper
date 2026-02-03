#!/usr/bin/env python3
"""
Prepare properly formatted data files for replication package
"""
import pandas as pd

# Load the full data
df_full = pd.read_csv('../analysis/data/cleaned_data_full.csv')

print(f"Loaded full data: N={len(df_full)}, {df_full.shape[1]} columns")

# Create mapping by finding columns that match patterns
# This is more robust than hardcoding exact strings
item_mapping = {}

# Find TAM item columns
for col in df_full.columns:
    if 'help older adults be more physically active' in col:
        item_mapping[col] = 'PU1'
    elif 'improve older adults' in col and 'daily well-being' in col:
        item_mapping[col] = 'PU2'
    elif 'meaningfully complement daily routines' in col:
        item_mapping[col] = 'PU3'
    elif 'easy to understand' in col:
        item_mapping[col] = 'PEOU1'
    elif 'with only a short explanation' in col:
        item_mapping[col] = 'PEOU2'
    elif 'basic interaction' in col and 'intuitive' in col:
        item_mapping[col] = 'PEOU3'
    elif 'find this system enjoyable' in col:
        item_mapping[col] = 'PE1'
    elif 'feel fun for older adults' in col:
        item_mapping[col] = 'PE2'
    elif 'make movement feel more playful' in col:
        item_mapping[col] = 'PE3'
    elif 'used safely by older adults' in col:
        item_mapping[col] = 'PS1'
    elif 'feel comfortable if an older relative' in col:
        item_mapping[col] = 'PS2'
    elif 'suitable for older adults who may have balance' in col:
        item_mapping[col] = 'PS3'
    elif 'would recommend this system' in col:
        item_mapping[col] = 'BI1'
    elif 'responsible for activities' in col and 'support introducing' in col:
        item_mapping[col] = 'BI2'
    elif 'speak positively about this system' in col:
        item_mapping[col] = 'BI3'

print(f"\nFound {len(item_mapping)} TAM items")

# Rename columns for TAM items
df_renamed = df_full.copy()
renamed_count = 0
for old_name, new_name in item_mapping.items():
    if old_name in df_renamed.columns:
        df_renamed = df_renamed.rename(columns={old_name: new_name})
        renamed_count += 1
        print(f"✓ Renamed: {new_name}")
    else:
        print(f"✗ Missing: {new_name} - '{old_name[:50]}...'")

print(f"\nRenamed {renamed_count}/{len(item_mapping)} items")

# Save full data with renamed TAM items
df_renamed.to_csv('../replication_package/data/cleaned_data_full.csv', index=False)
print(f"\n✓ Saved: cleaned_data_full.csv with {df_renamed.shape[1]} columns")

# Create item-only data for EFA
tam_items = ['PU1', 'PU2', 'PU3', 'PEOU1', 'PEOU2', 'PEOU3', 
             'PE1', 'PE2', 'PE3', 'PS1', 'PS2', 'PS3', 
             'BI1', 'BI2', 'BI3']

# Check which items are actually in the renamed dataframe
available_tam_items = [item for item in tam_items if item in df_renamed.columns]
print(f"\nAvailable TAM items: {len(available_tam_items)}/{len(tam_items)}")

# Add Respondent ID if it exists
cols_to_keep = ['Respondent ID'] if 'Respondent ID' in df_renamed.columns else []
cols_to_keep.extend(available_tam_items)

df_items = df_renamed[cols_to_keep]
df_items.to_csv('../replication_package/data/cleaned_data.csv', index=False)
print(f"✓ Saved: cleaned_data.csv with {df_items.shape[1]} columns ({len(available_tam_items)} TAM items)")

print("\n" + "="*70)
print("✓ Data preparation complete!")
print("="*70)

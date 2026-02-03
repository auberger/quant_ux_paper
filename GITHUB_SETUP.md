# 🚀 GitHub Repository Setup Guide

**Repository:** https://github.com/auberger/quant_ux_paper.git  
**Date:** February 3, 2026

---

## ✅ What's Already Done

- [x] Repository created on GitHub
- [x] Paper updated with repository URL
- [x] `.gitignore` file created
- [x] All documentation updated with correct URLs

---

## 📤 Push Replication Package to GitHub

### Step 1: Initialize Git (if needed)
```bash
cd /Users/auberger/Documents/Github_repos/UX_paper/replication_package

# Check if already a git repo
git status

# If not, initialize
git init
```

### Step 2: Add Remote
```bash
# Add your GitHub repository as remote
git remote add origin https://github.com/auberger/quant_ux_paper.git

# Verify remote
git remote -v
```

### Step 3: Commit All Files
```bash
# Add all files
git add .

# Check what will be committed
git status

# Commit with descriptive message
git commit -m "Initial commit: Complete replication package for Movement Island TAM study

- 3 Jupyter notebooks (descriptives, EFA, regression)
- Cleaned datasets (N=16, anonymized)
- Complete documentation and codebook
- Requirements and license files
- Verification test script"
```

### Step 4: Push to GitHub
```bash
# Push to main branch (or master, depending on your default)
git push -u origin main

# If main doesn't exist, create it first:
git branch -M main
git push -u origin main
```

---

## 🔍 Verify Upload

After pushing, check your repository:
1. Visit: https://github.com/auberger/quant_ux_paper
2. Verify all files are present:
   - ✓ data/ folder with both CSV files
   - ✓ notebooks/ folder with 3 .ipynb files
   - ✓ README.md displays on main page
   - ✓ LICENSE file
   - ✓ requirements.txt

3. Check README renders correctly on GitHub

---

## 📝 Optional: Create GitHub Release

For extra professionalism, create a release:

```bash
# Tag this version
git tag -a v1.0 -m "Version 1.0: Initial publication release"
git push origin v1.0
```

Then on GitHub:
1. Go to repository → Releases
2. Click "Create a new release"
3. Select tag: v1.0
4. Title: "v1.0 - Initial Publication Release"
5. Description: Copy from PACKAGE_SUMMARY.md
6. Publish release

---

## 🎯 Final Checklist

Before announcing:
- [ ] All files pushed to GitHub
- [ ] README displays correctly on repository page
- [ ] Notebooks are viewable (GitHub renders .ipynb files)
- [ ] Data files are accessible
- [ ] Paper (main.tex) contains correct URL
- [ ] Test clone from fresh location:
  ```bash
  cd ~/Desktop
  git clone https://github.com/auberger/quant_ux_paper.git
  cd quant_ux_paper
  python test_package.py
  ```

---

## 📧 Share Your Work

Once published, you can share:
- **In paper:** Already done via Data Availability section
- **With reviewers:** Include GitHub URL in submission notes
- **On CV/Resume:** Link to demonstrate reproducibility practices
- **Academic profiles:** Add to ResearchGate, ORCID, etc.

---

## 🔄 Future Updates

If you need to update the repository later:

```bash
cd /Users/auberger/Documents/Github_repos/UX_paper/replication_package

# Make your changes, then:
git add .
git commit -m "Description of changes"
git push
```

---

## ⚠️ Troubleshooting

### Authentication Issues
If you get authentication errors:
1. Use personal access token (not password)
2. Or set up SSH keys
3. See: https://docs.github.com/en/authentication

### Large Files
If files are too large (>100MB):
- GitHub has file size limits
- Your package should be well under this (~10MB total)
- If needed, use Git LFS for large files

### Notebook Outputs
Decision point: Keep notebook outputs in repo?
- ✅ **Keep:** Users can verify their results match yours
- ❌ **Remove:** Makes repo cleaner, users regenerate
- Current .gitignore: **Keeps outputs** (commented out exclusions)

---

**Status:** Ready to push! 🎉

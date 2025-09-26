# 🚀 How to Start Diamond Sorter

## Quick Start Options

### Option 1: Direct Run (Recommended)
```bash
python src/core/DiamondSorter.py
```

### Option 2: Simple Launcher
```bash
python launch.py
```

### Option 3: Windows Batch File
Double-click `run.bat` or run:
```cmd
run.bat
```

### Option 4: Main Entry Point
```bash
python main.py
```

### Option 5: Advanced Launcher
```bash
python start.py
```

## 🔧 If You Get Import Errors

### Install Dependencies
```bash
python install.py
```

### Or Install Manually
```bash
pip install PyQt5==5.15.10 requests beautifulsoup4
```

### Or Use Minimal Requirements
```bash
pip install -r requirements-minimal.txt
```

## 🎯 Troubleshooting

### Problem: "No module named 'pystray'"
**Solution**: This is an optional dependency. The app should work without it.

### Problem: "No module named 'PyQt5'"
**Solution**: Install PyQt5:
```bash
pip install PyQt5==5.15.10
```

### Problem: "Cannot import DiamondSorter"
**Solution**: Use the direct launcher:
```bash
python launch.py
```

### Problem: "File not found"
**Solution**: Make sure you're in the Diamond-Sorter-main directory.

## 📋 What Each File Does

- **`src/core/DiamondSorter.py`** - Main application file
- **`launch.py`** - Simple launcher with error handling
- **`main.py`** - Main entry point with import handling
- **`start.py`** - Advanced launcher with dependency checking
- **`run.bat`** - Windows batch file for quick start
- **`install.py`** - Dependency installer
- **`install.bat`** - Windows installer

## ✅ Recommended Workflow

1. **First time**: Run `python install.py` to install dependencies
2. **Daily use**: Run `python launch.py` or `python src/core/DiamondSorter.py`
3. **If issues**: Try `python main.py` for better error messages

## 🎉 Success!

Once running, you should see the Diamond Sorter application window with all its features available!

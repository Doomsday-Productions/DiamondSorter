#!/usr/bin/env python3
"""
Diamond Sorter Launcher
Simple launcher script for the reorganized Diamond Sorter project.
"""

import sys
import os
from pathlib import Path

def main():
    """Main launcher function."""
    print("🔷 Diamond Sorter - Starting...")
    
    # Add src to Python path
    src_path = Path(__file__).parent / "src"
    if src_path.exists():
        sys.path.insert(0, str(src_path))
    
    # Check if main.py exists
    main_file = Path(__file__).parent / "main.py"
    if not main_file.exists():
        print("❌ Error: main.py not found!")
        print("Please ensure you're running this from the project root directory.")
        return 1
    
    try:
        # Import and run the main application
        from main import main as run_main
        run_main()
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("Please install dependencies: pip install -r requirements.txt")
        return 1
    except Exception as e:
        print(f"❌ Error starting application: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())

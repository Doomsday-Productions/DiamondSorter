#!/usr/bin/env python3
"""
Diamond Sorter - Main Application Entry Point
"""

import sys
import os
import warnings
import logging
from io import StringIO

# Add src to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Suppress all warnings and debug messages
warnings.filterwarnings("ignore")
os.environ['QT_LOGGING_RULES'] = '*.debug=false;*.warning=false;*.info=false'

# Suppress all print statements that contain DEBUG or BUG
class DebugFilter:
    def __init__(self):
        self.original_stdout = sys.stdout
        self.original_stderr = sys.stderr
        self.debug_output = StringIO()
    
    def write(self, text):
        # Filter out DEBUG and BUG messages
        if any(keyword in text for keyword in ['DEBUG:', 'BUG:', 'push Q', 'pop widget', 'setting property', 'new topwidget', 'add action', 'savedResultsTextBox is buddy', 'QWidget::setMinimumSize', 'Scrollbars styled', 'Scrolling functionality', 'Window sized', 'QLayout:', 'Scroll area refreshed']):
            self.debug_output.write(text)
        else:
            self.original_stdout.write(text)
    
    def flush(self):
        self.original_stdout.flush()
    
    def __getattr__(self, name):
        return getattr(self.original_stdout, name)

# Apply the debug filter
debug_filter = DebugFilter()
sys.stdout = debug_filter
sys.stderr = debug_filter

# Suppress logging
logging.getLogger().setLevel(logging.CRITICAL)
logging.getLogger("PyQt5").setLevel(logging.CRITICAL)
logging.getLogger("PyQt5.QtCore").setLevel(logging.CRITICAL)
logging.getLogger("PyQt5.QtGui").setLevel(logging.CRITICAL)
logging.getLogger("PyQt5.QtWidgets").setLevel(logging.CRITICAL)

def main():
    """Main application entry point."""
    try:
        # Check for PyQt5 first
        try:
            from PyQt5.QtWidgets import QApplication
        except ImportError:
            print("❌ PyQt5 not found. Installing...")
            import subprocess
            subprocess.check_call([sys.executable, "-m", "pip", "install", "PyQt5==5.15.10"])
            from PyQt5.QtWidgets import QApplication
        
        # Create QApplication first
        app = QApplication(sys.argv)
        app.setApplicationName("Diamond Sorter")
        app.setApplicationVersion("1.0")
        
        # Show splash screen
        from src.splash_screen import show_splash_screen
        splash = show_splash_screen(app, 5000)  # Show for 5 seconds
        
        # Try to import the main DiamondSorter application
        try:
            from src.core.DiamondSorter import DiamondSorter
        except ImportError as e:
            print(f"❌ Cannot import DiamondSorter: {e}")
            print("Trying alternative import...")
            # Try direct import from the file
            import importlib.util
            spec = importlib.util.spec_from_file_location("DiamondSorter", "src/core/DiamondSorter.py")
            DiamondSorter_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(DiamondSorter_module)
            DiamondSorter = DiamondSorter_module.DiamondSorter
        
        # Wait a bit to ensure splash screen is visible
        import time
        time.sleep(2)
        
        # Create and show main window
        window = DiamondSorter()
        window.show()
        
        # Close splash screen after main window is shown
        time.sleep(1)
        splash.close()
        
        # Start event loop
        sys.exit(app.exec_())
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("\n🔧 Troubleshooting:")
        print("1. Install dependencies: python install.py")
        print("2. Or try minimal install: pip install PyQt5 requests beautifulsoup4")
        print("3. Check if you're in the correct directory")
        input("\nPress Enter to exit...")
        return 1
    except Exception as e:
        print(f"❌ Error starting application: {e}")
        print("\n🔧 Troubleshooting:")
        print("1. Make sure all dependencies are installed")
        print("2. Check if the main application file exists")
        print("3. Try running: python src/core/DiamondSorter.py")
        input("\nPress Enter to exit...")
        return 1

if __name__ == "__main__":
    main()

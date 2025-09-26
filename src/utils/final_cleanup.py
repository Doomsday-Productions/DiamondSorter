#!/usr/bin/env python3
"""
Final cleanup script to organize remaining files in root directory
"""

import os
import shutil
from pathlib import Path

def final_cleanup():
    """Final cleanup of root directory."""
    print("🧹 Final cleanup of root directory...")
    
    # Files that should be moved to src/utils/
    utility_files = [
        "__init__.py",
        "__main.py", 
        "_diamondsorter.py",
        "about.py",
        "add_cookies_from_scan_to_db.py",
        "add_to_app.py",
        "authentication.py",
        "browser.py",
        "cf.py",
        "config_developer.py",
        "cryptolens_python2.py",
        "disclaimer.py",
        "domain_sorter.py",
        "email_sorter.py",
        "installer.py",
        "list_dependencies.py",
        "loader.py",
        "login_screen.py",
        "merged_example.py",
        "method1.py",
        "method2.py",
        "output.py",
        "password_log_formats.py",
        "sdg.py",
        "sorting_files_tab.py",
        "test.py",
        "url_tools.py",
        "url_tools1.py",
        "Ui_url_tools.py"
    ]
    
    for file in utility_files:
        if os.path.exists(file):
            shutil.move(file, "src/utils/")
            print(f"✅ Moved {file} to src/utils/")
    
    # Move remaining UI files
    ui_files = [
        "form.ui",
        "forms.py",
        "general_tab.py",
        "ui_form.py"
    ]
    
    for file in ui_files:
        if os.path.exists(file):
            shutil.move(file, "src/ui/")
            print(f"✅ Moved {file} to src/ui/")
    
    # Move main application files
    if os.path.exists("DiamondSorter.py"):
        shutil.move("DiamondSorter.py", "src/core/")
        print("✅ Moved DiamondSorter.py to src/core/")
    
    if os.path.exists("DiamondSorter.pyw"):
        shutil.move("DiamondSorter.pyw", "src/core/")
        print("✅ Moved DiamondSorter.pyw to src/core/")
    
    if os.path.exists("main.py"):
        shutil.move("main.py", "src/core/")
        print("✅ Moved main.py to src/core/")
    
    # Move third-party modules
    if os.path.exists("darkdetect"):
        shutil.move("darkdetect", "src/features/modules/")
        print("✅ Moved darkdetect to src/features/modules/")
    
    if os.path.exists("qframelesswindow"):
        shutil.move("qframelesswindow", "src/features/modules/")
        print("✅ Moved qframelesswindow to src/features/modules/")
    
    if os.path.exists("modules"):
        shutil.move("modules", "src/features/modules/")
        print("✅ Moved modules to src/features/modules/")
    
    if os.path.exists("references"):
        shutil.move("references", "src/features/references/")
        print("✅ Moved references to src/features/references/")
    
    # Move remaining directories
    if os.path.exists("other-examples"):
        shutil.move("other-examples", "src/features/")
        print("✅ Moved other-examples to src/features/")
    
    if os.path.exists("Created Resources"):
        shutil.move("Created Resources", "data/")
        print("✅ Moved Created Resources to data/")
    
    if os.path.exists("ui_files"):
        shutil.move("ui_files", "src/ui/")
        print("✅ Moved ui_files to src/ui/")
    
    if os.path.exists("resources"):
        shutil.move("resources", "assets/")
        print("✅ Moved resources to assets/")
    
    # Move remaining data files
    if os.path.exists("data"):
        for file in os.listdir("data"):
            if file not in ["databases", "temp", "output"]:
                src_path = os.path.join("data", file)
                if os.path.isfile(src_path):
                    shutil.move(src_path, "data/")
                elif os.path.isdir(src_path):
                    shutil.move(src_path, "data/")
        print("✅ Organized data directory")
    
    # Remove empty directories
    empty_dirs = ["icons", "images", "ui"]
    for dir_name in empty_dirs:
        if os.path.exists(dir_name):
            try:
                if not os.listdir(dir_name):
                    os.rmdir(dir_name)
                    print(f"✅ Removed empty directory: {dir_name}")
                else:
                    print(f"⚠️  Directory {dir_name} not empty, keeping it")
            except OSError:
                print(f"⚠️  Could not remove directory: {dir_name}")
    
    # Move the organization script to scripts
    if os.path.exists("organize_project.py"):
        shutil.move("organize_project.py", "scripts/")
        print("✅ Moved organize_project.py to scripts/")
    
    if os.path.exists("final_cleanup.py"):
        shutil.move("final_cleanup.py", "scripts/")
        print("✅ Moved final_cleanup.py to scripts/")
    
    print("\n✅ Final cleanup completed!")

def print_final_structure():
    """Print the final project structure."""
    print("\n📁 Final Project Structure:")
    print("=" * 50)
    
    for root, dirs, files in os.walk('.'):
        # Skip hidden directories and __pycache__
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
        
        level = root.replace('.', '').count(os.sep)
        indent = ' ' * 2 * level
        print(f"{indent}{os.path.basename(root)}/")
        
        subindent = ' ' * 2 * (level + 1)
        for file in files[:5]:  # Limit to first 5 files
            print(f"{subindent}{file}")
        if len(files) > 5:
            print(f"{subindent}... and {len(files) - 5} more files")

if __name__ == "__main__":
    final_cleanup()
    print_final_structure()

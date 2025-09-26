#!/usr/bin/env python3
"""
Project Organization Script for Diamond Sorter
Organizes the project structure and cleans up the root directory
"""

import os
import shutil
from pathlib import Path

def create_directory_structure():
    """Create the organized directory structure."""
    directories = [
        # Core application
        "src/core",
        "src/ui", 
        "src/utils",
        "src/data",
        "src/features/sorter",
        "src/features/checker", 
        "src/features/browser",
        "src/features/chat",
        "src/features/modules",
        "src/features/references",
        
        # Configuration and assets
        "config",
        "assets/icons",
        "assets/images", 
        "assets/styles",
        "assets/fonts",
        
        # Documentation and tests
        "docs",
        "tests",
        "scripts",
        
        # Data and output
        "data/databases",
        "data/temp",
        "data/output",
        "logs"
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"✅ Created directory: {directory}")

def organize_core_files():
    """Organize core application files."""
    core_files = {
        "DiamondSorter.py": "src/core/",
        "DiamondSorter.pyw": "src/core/",
        "main.py": "src/core/app_main.py",
        "forms.py": "src/core/",
        "ui_form.py": "src/ui/",
        "form.ui": "src/ui/",
    }
    
    for source, dest in core_files.items():
        if os.path.exists(source):
            shutil.copy2(source, dest)
            print(f"✅ Moved {source} to {dest}")

def organize_ui_files():
    """Organize UI-related files."""
    ui_files = [
        "about.py",
        "browser.py", 
        "login_screen.py",
        "general_tab.py",
        "password_log_formats.py",
        "sorting_files_tab.py",
        "domain_sorter.py",
        "email_sorter.py",
        "url_tools.py",
        "url_tools1.py",
        "Ui_url_tools.py",
        "output.py",
        "disclaimer.py"
    ]
    
    for file in ui_files:
        if os.path.exists(file):
            shutil.copy2(file, "src/ui/")
            print(f"✅ Moved {file} to src/ui/")

def organize_utility_files():
    """Organize utility and helper files."""
    utility_files = [
        "cf.py",
        "authentication.py",
        "cryptolens_python2.py",
        "config_developer.py",
        "installer.py",
        "loader.py",
        "list_dependencies.py",
        "merged_example.py",
        "method1.py",
        "method2.py",
        "sdg.py",
        "test.py",
        "add_cookies_from_scan_to_db.py",
        "add_to_app.py",
        "_diamondsorter.py",
        "__main.py"
    ]
    
    for file in utility_files:
        if os.path.exists(file):
            shutil.copy2(file, "src/utils/")
            print(f"✅ Moved {file} to src/utils/")

def organize_feature_modules():
    """Organize feature modules."""
    # Move DiamondChecker to features/checker
    if os.path.exists("DiamondChecker"):
        if os.path.exists("src/features/checker"):
            shutil.rmtree("src/features/checker")
        shutil.move("DiamondChecker", "src/features/checker")
        print("✅ Moved DiamondChecker to src/features/checker")
    
    # Move DiamondBrowser to features/browser
    if os.path.exists("DiamondBrowser"):
        if os.path.exists("src/features/browser"):
            shutil.rmtree("src/features/browser")
        shutil.move("DiamondBrowser", "src/features/browser")
        print("✅ Moved DiamondBrowser to src/features/browser")
    
    # Move DiamondSorter_Chat to features/chat
    if os.path.exists("DiamondSorter_Chat"):
        if os.path.exists("src/features/chat"):
            shutil.rmtree("src/features/chat")
        shutil.move("DiamondSorter_Chat", "src/features/chat")
        print("✅ Moved DiamondSorter_Chat to src/features/chat")

def organize_assets():
    """Organize asset files."""
    # Move icons
    if os.path.exists("icons"):
        for file in os.listdir("icons"):
            shutil.copy2(os.path.join("icons", file), "assets/icons/")
        print("✅ Moved icons to assets/icons/")
    
    # Move images
    if os.path.exists("images"):
        for file in os.listdir("images"):
            shutil.copy2(os.path.join("images", file), "assets/images/")
        print("✅ Moved images to assets/images/")
    
    # Move styles
    if os.path.exists("ui"):
        for file in os.listdir("ui"):
            if file.endswith('.css'):
                shutil.copy2(os.path.join("ui", file), "assets/styles/")
        print("✅ Moved CSS files to assets/styles/")

def organize_data_files():
    """Organize data and database files."""
    data_files = [
        "cashout.db",
        "chatapp.db", 
        "cookie_data.db",
        "*.db"
    ]
    
    for pattern in data_files:
        if '*' in pattern:
            import glob
            for file in glob.glob(pattern):
                shutil.move(file, "data/databases/")
                print(f"✅ Moved {file} to data/databases/")
        elif os.path.exists(pattern):
            shutil.move(pattern, "data/databases/")
            print(f"✅ Moved {pattern} to data/databases/")

def organize_config_files():
    """Organize configuration files."""
    config_files = [
        "settings.json",
        "auth.json", 
        "version.txt",
        "diamondsorter.spec",
        "EULA.rtf",
        "LICENSE",
        "r.txt"
    ]
    
    for file in config_files:
        if os.path.exists(file):
            shutil.move(file, "config/")
            print(f"✅ Moved {file} to config/")

def organize_third_party_modules():
    """Organize third-party modules and references."""
    if os.path.exists("modules"):
        shutil.move("modules", "src/features/modules")
        print("✅ Moved modules to src/features/modules")
    
    if os.path.exists("references"):
        shutil.move("references", "src/features/references")
        print("✅ Moved references to src/features/references")
    
    if os.path.exists("qframelesswindow"):
        shutil.move("qframelesswindow", "src/features/modules/")
        print("✅ Moved qframelesswindow to src/features/modules/")
    
    if os.path.exists("darkdetect"):
        shutil.move("darkdetect", "src/features/modules/")
        print("✅ Moved darkdetect to src/features/modules/")

def organize_scripts():
    """Organize build and utility scripts."""
    script_files = [
        "cleanup.py",
        "dev_setup.py", 
        "setup.py",
        "run.py",
        "Install Requirements.bat"
    ]
    
    for file in script_files:
        if os.path.exists(file):
            shutil.move(file, "scripts/")
            print(f"✅ Moved {file} to scripts/")

def clean_root_directory():
    """Clean up the root directory by removing empty directories and organizing remaining files."""
    # Remove empty directories
    empty_dirs = [
        "icons",
        "images", 
        "ui",
        "ui_files",
        "data",
        "other-examples",
        "Created Resources"
    ]
    
    for dir_name in empty_dirs:
        if os.path.exists(dir_name):
            try:
                if not os.listdir(dir_name):  # Check if directory is empty
                    os.rmdir(dir_name)
                    print(f"✅ Removed empty directory: {dir_name}")
                else:
                    print(f"⚠️  Directory {dir_name} not empty, keeping it")
            except OSError:
                print(f"⚠️  Could not remove directory: {dir_name}")
    
    # Move remaining important files
    remaining_files = [
        "DIAMOND.ico",
        "favicon72x72.png",
        "qwindows.dll",
        "resources_rc.py",
        "THEME_README.md"
    ]
    
    for file in remaining_files:
        if os.path.exists(file):
            shutil.move(file, "assets/")
            print(f"✅ Moved {file} to assets/")

def create_init_files():
    """Create __init__.py files for Python packages."""
    init_files = [
        "src/__init__.py",
        "src/core/__init__.py",
        "src/ui/__init__.py", 
        "src/utils/__init__.py",
        "src/data/__init__.py",
        "src/features/__init__.py",
        "src/features/sorter/__init__.py",
        "src/features/checker/__init__.py",
        "src/features/browser/__init__.py",
        "src/features/chat/__init__.py",
        "src/features/modules/__init__.py",
        "src/features/references/__init__.py",
        "config/__init__.py",
        "assets/__init__.py",
        "docs/__init__.py",
        "tests/__init__.py",
        "scripts/__init__.py"
    ]
    
    for init_file in init_files:
        Path(init_file).parent.mkdir(parents=True, exist_ok=True)
        with open(init_file, 'w') as f:
            f.write(f'# {Path(init_file).parent.name} package\n')
        print(f"✅ Created {init_file}")

def main():
    """Main organization function."""
    print("🔷 Diamond Sorter - Project Organization")
    print("=" * 50)
    
    # Create directory structure
    print("\n📁 Creating directory structure...")
    create_directory_structure()
    
    # Organize files
    print("\n📦 Organizing core files...")
    organize_core_files()
    
    print("\n🎨 Organizing UI files...")
    organize_ui_files()
    
    print("\n🔧 Organizing utility files...")
    organize_utility_files()
    
    print("\n⚙️ Organizing feature modules...")
    organize_feature_modules()
    
    print("\n🖼️ Organizing assets...")
    organize_assets()
    
    print("\n💾 Organizing data files...")
    organize_data_files()
    
    print("\n⚙️ Organizing config files...")
    organize_config_files()
    
    print("\n📚 Organizing third-party modules...")
    organize_third_party_modules()
    
    print("\n📜 Organizing scripts...")
    organize_scripts()
    
    print("\n🧹 Cleaning root directory...")
    clean_root_directory()
    
    print("\n🐍 Creating Python package files...")
    create_init_files()
    
    print("\n✅ Project organization completed!")
    print("\n📁 New project structure:")
    print_project_structure()

def print_project_structure():
    """Print the organized project structure."""
    for root, dirs, files in os.walk('.'):
        # Skip hidden directories and __pycache__
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
        
        level = root.replace('.', '').count(os.sep)
        indent = ' ' * 2 * level
        print(f"{indent}{os.path.basename(root)}/")
        
        subindent = ' ' * 2 * (level + 1)
        for file in files[:10]:  # Limit to first 10 files
            print(f"{subindent}{file}")
        if len(files) > 10:
            print(f"{subindent}... and {len(files) - 10} more files")

if __name__ == "__main__":
    main()

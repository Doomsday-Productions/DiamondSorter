#!/usr/bin/env python3
"""
Cleanup script for Diamond Sorter project.
Removes unnecessary files and organizes the project structure.
"""

import os
import shutil
from pathlib import Path

def cleanup_project():
    """Clean up the project by removing unnecessary files."""
    
    # Files to remove from root directory
    files_to_remove = [
        'DiamondSorter.py',
        'DiamondSorter.pyw', 
        'ui_form.py',
        'forms.py',
        'general_tab.py',
        'password_log_formats.py',
        'sorting_files_tab.py',
        'domain_sorter.py',
        'email_sorter.py',
        'url_tools.py',
        'url_tools1.py',
        'Ui_url_tools.py',
        'about.py',
        'browser.py',
        'login_screen.py',
        'output.py',
        'disclaimer.py',
        'add_cookies_from_scan_to_db.py',
        'add_to_app.py',
        'authentication.py',
        'cf.py',
        'cryptolens_python2.py',
        'config_developer.py',
        'installer.py',
        'loader.py',
        'list_dependencies.py',
        'merged_example.py',
        'method1.py',
        'method2.py',
        'sdg.py',
        'test.py',
        'r.txt',
        'diamondsorter.spec',
        'EULA.rtf',
        'Install Requirements.bat',
        'resources_rc.py',
        'settings.json',
        'auth.json',
        'version.txt',
        '_diamondsorter.py',
        '__main.py',
        '__init__.py',
        'form.ui'
    ]
    
    # Directories to remove (after moving contents)
    dirs_to_remove = [
        'DiamondSorter_Chat',
        'DiamondChecker', 
        'DiamondBrowser',
        'icons',
        'images',
        'data',
        'ui_files',
        'ui',
        'modules',
        'references',
        'other-examples',
        'Created Resources',
        'src',
        'darkdetect',
        'qframelesswindow',
        'scripts'
    ]
    
    print("🧹 Starting project cleanup...")
    
    # Remove files
    for file in files_to_remove:
        if os.path.exists(file):
            try:
                os.remove(file)
                print(f"✅ Removed file: {file}")
            except Exception as e:
                print(f"❌ Failed to remove {file}: {e}")
    
    # Remove directories
    for dir_name in dirs_to_remove:
        if os.path.exists(dir_name):
            try:
                shutil.rmtree(dir_name)
                print(f"✅ Removed directory: {dir_name}")
            except Exception as e:
                print(f"❌ Failed to remove {dir_name}: {e}")
    
    # Clean up __pycache__ directories
    for root, dirs, files in os.walk('.'):
        for dir_name in dirs:
            if dir_name == '__pycache__':
                try:
                    shutil.rmtree(os.path.join(root, dir_name))
                    print(f"✅ Removed __pycache__: {os.path.join(root, dir_name)}")
                except Exception as e:
                    print(f"❌ Failed to remove __pycache__: {e}")
    
    print("\n🎉 Cleanup completed!")
    print("\n📁 Current project structure:")
    print_project_structure()

def print_project_structure():
    """Print the current project structure."""
    for root, dirs, files in os.walk('.'):
        # Skip hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        level = root.replace('.', '').count(os.sep)
        indent = ' ' * 2 * level
        print(f"{indent}{os.path.basename(root)}/")
        
        subindent = ' ' * 2 * (level + 1)
        for file in files[:10]:  # Limit to first 10 files
            print(f"{subindent}{file}")
        if len(files) > 10:
            print(f"{subindent}... and {len(files) - 10} more files")

if __name__ == "__main__":
    cleanup_project()

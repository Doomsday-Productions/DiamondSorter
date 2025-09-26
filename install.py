#!/usr/bin/env python3
"""
Diamond Sorter - Dependency Installer
Handles dependency installation with error recovery
"""

import sys
import subprocess
import os
import importlib
import time
import threading

def animated_loading(message, duration=2):
    """Display an animated loading message."""
    def animate():
        dots = 0
        start_time = time.time()
        while time.time() - start_time < duration:
            dots = (dots + 1) % 4
            print(f"\r{message}{'.' * dots}{' ' * (3 - dots)}", end="", flush=True)
            time.sleep(0.3)
        print(f"\r{message}...", end="", flush=True)
    
    # Start animation in a separate thread
    animation_thread = threading.Thread(target=animate)
    animation_thread.daemon = True
    animation_thread.start()
    
    return animation_thread

def is_package_installed(package_name):
    """Check if a package is already installed."""
    try:
        # Extract the package name (remove version specifiers)
        clean_name = package_name.split('==')[0].split('>=')[0].split('<=')[0].split('>')[0].split('<')[0]
        
        # Try to import the package
        importlib.import_module(clean_name)
        return True
    except ImportError:
        return False

def check_requirements(packages):
    """Check which packages are already installed and which need to be installed."""
    # Start animated loading
    animation_thread = animated_loading("🔍 Checking existing packages", 1.5)
    
    installed = []
    missing = []
    
    for package in packages:
        if is_package_installed(package):
            installed.append(package)
        else:
            missing.append(package)
    
    # Wait for animation to complete
    animation_thread.join()
    print()  # New line after animation
    
    return installed, missing

def install_package(package):
    """Install a single package with error handling."""
    try:
        print(f"📦 Installing {package}...", end=" ", flush=True)
        # Suppress pip output but capture any errors
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", package, "--quiet"],
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            print("✅")
            return True
        else:
            print("❌")
            print(f"   Error: {result.stderr.strip()}")
            return False
    except Exception as e:
        print("❌")
        print(f"   Error: {e}")
        return False

def install_requirements():
    """Install requirements with fallback options."""
    print("🔷 Diamond Sorter - Dependency Installer")
    print("=" * 50)
    
    # Essential packages in order of importance
    essential_packages = [
        "PyQt5==5.15.10",
        "requests==2.31.0", 
        "beautifulsoup4==4.12.2",
        "tqdm==4.66.1",
        "pyperclip==1.8.2",
        "pillow==9.5.0",
        "psutil==5.9.7"
    ]
    
    # Optional packages
    optional_packages = [
        "pandas>=1.3.0",
        "numpy>=1.21.0",
        "lxml==5.1.0",
        "cryptography==41.0.7",
        "pystray>=0.19.0"
    ]
    
    # Check what's already installed
    essential_installed, essential_missing = check_requirements(essential_packages)
    optional_installed, optional_missing = check_requirements(optional_packages)
    
    # Show what's already installed
    if essential_installed:
        print(f"✅ Already installed: {', '.join([p.split('==')[0] for p in essential_installed])}")
    if optional_installed:
        print(f"✅ Optional installed: {', '.join([p.split('==')[0] for p in optional_installed])}")
    
    # Install missing essential packages
    if essential_missing:
        print(f"\n📦 Installing {len(essential_missing)} missing essential packages...")
        essential_success = 0
        for i, package in enumerate(essential_missing, 1):
            print(f"[{i}/{len(essential_missing)}] ", end="")
            if install_package(package):
                essential_success += 1
        
        print(f"\n✅ Installed {essential_success}/{len(essential_missing)} missing essential packages")
    else:
        print("\n✅ All essential packages are already installed!")
        essential_success = len(essential_packages)
    
    # Install missing optional packages if enough essential packages are available
    if essential_success >= 3 and optional_missing:
        print(f"\n📦 Installing {len(optional_missing)} missing optional packages...")
        optional_success = 0
        for i, package in enumerate(optional_missing, 1):
            print(f"[{i}/{len(optional_missing)}] ", end="")
            if install_package(package):
                optional_success += 1
        
        print(f"✅ Installed {optional_success}/{len(optional_missing)} missing optional packages")
    elif essential_success >= 3:
        print("\n✅ All optional packages are already installed!")
    
    # Final status
    total_essential = len(essential_installed) + (essential_success if essential_missing else 0)
    if total_essential >= 3:
        print("\n🎉 Installation completed!")
        print("You can now run the application with: python main.py")
        return True
    else:
        print("\n❌ Installation failed - not enough essential packages available")
        print("Please try installing PyQt5 manually: pip install PyQt5")
        return False

def main():
    """Main installation function."""
    try:
        success = install_requirements()
        if not success:
            sys.exit(1)
    except KeyboardInterrupt:
        print("\n\n👋 Installation interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

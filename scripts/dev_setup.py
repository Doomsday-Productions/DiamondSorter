#!/usr/bin/env python3
"""
Development setup script for Diamond Sorter.
Sets up the development environment and installs dependencies.
"""

import subprocess
import sys
import os
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors."""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        print(f"Error output: {e.stderr}")
        return False

def check_python_version():
    """Check if Python version is compatible."""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8 or higher is required!")
        print(f"Current version: {version.major}.{version.minor}.{version.micro}")
        return False
    print(f"✅ Python version {version.major}.{version.minor}.{version.micro} is compatible")
    return True

def setup_development_environment():
    """Set up the development environment."""
    print("🚀 Setting up Diamond Sorter development environment...")
    
    # Check Python version
    if not check_python_version():
        return False
    
    # Create necessary directories
    directories = [
        "data",
        "logs", 
        "temp",
        "output",
        "tests/data"
    ]
    
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
        print(f"✅ Created directory: {directory}")
    
    # Install dependencies
    if not run_command("pip install -r requirements.txt", "Installing dependencies"):
        return False
    
    # Install development dependencies
    dev_deps = [
        "pytest>=6.0.0",
        "pytest-qt>=4.0.0", 
        "black>=21.0.0",
        "flake8>=3.8.0",
        "mypy>=0.800"
    ]
    
    for dep in dev_deps:
        if not run_command(f"pip install {dep}", f"Installing {dep}"):
            print(f"⚠️  Warning: Failed to install {dep}")
    
    print("\n🎉 Development environment setup completed!")
    print("\n📋 Next steps:")
    print("1. Run the application: python run.py")
    print("2. Run tests: pytest tests/")
    print("3. Format code: black src/")
    print("4. Lint code: flake8 src/")
    
    return True

def main():
    """Main setup function."""
    if not setup_development_environment():
        print("\n❌ Setup failed!")
        return 1
    
    print("\n✅ Setup completed successfully!")
    return 0

if __name__ == "__main__":
    sys.exit(main())

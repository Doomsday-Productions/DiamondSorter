"""
Diamond Sorter - Main Application
Simplified version that works with the existing UI structure.
"""

import sys
import os
import json
import re
import random
import string
import webbrowser
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import QUrl, Qt, QTimer, pyqtSignal, pyqtSlot, QThread, QThreadPool, QBasicTimer, QTimerEvent, QMessageLogContext, QtMsgType, QRect
from PyQt5.QtWidgets import (QApplication, QLineEdit, QHBoxLayout, QShortcut, QMainWindow, QListWidget, 
                            QDockWidget, QPlainTextEdit, QLCDNumber, QWidget, QVBoxLayout, QTextBrowser, 
                            QFileDialog, QTextEdit, QComboBox, QPushButton, QMessageBox, QFrame, 
                            QInputDialog, QLabel, QCheckBox, QScrollBar, QDialogButtonBox, QDialog, 
                            QGridLayout, QMenu, QAction, QTabBar, QSystemTrayIcon, QScrollArea)
from PyQt5.QtGui import QDesktopServices, QTextCursor, QTextDocument, QColor, QCursor, QTextCharFormat, QIcon, QPainter, QTextOption
import hashlib
from multiprocessing import Process, Queue
import binascii
import platform
import subprocess
from datetime import datetime
from time import sleep
import shutil
from collections import Counter, deque
from urllib.parse import urlparse
import logging
import zipfile
import ctypes
import pystray
from pystray import MenuItem as item
from tqdm import tqdm
import requests
import time
import curses
from PIL import Image
import pyperclip
from flask import session
import warnings
from PyQt5.QtGui import QKeySequence
from PyQt5 import QAxContainer
import difflib
import tkinter as tk
from tkinter import ttk

# Suppress warnings
warnings.filterwarnings("ignore", category=UserWarning, message="QLayout: Cannot add parent widget")
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning, message="Unknown property transform")
warnings.filterwarnings("ignore", category=UserWarning, message="Unknown property transform-origin")

# Constants
COUNTRY_PHONE_CODES = {
    "United States": "+1",
    "United Kingdom": "+44",
    "Canada": "+1",
    "Australia": "+61",
    "Germany": "+49",
    "France": "+33",
    "Japan": "+81",
    "China": "+86",
    "India": "+91",
    "Brazil": "+55",
    "Russia": "+7",
    "South Korea": "+82",
    "Italy": "+39",
    "Spain": "+34",
    "Mexico": "+52",
    "Netherlands": "+31",
    "Sweden": "+46",
    "Norway": "+47",
    "Denmark": "+45",
    "Finland": "+358"
}

INSTALLER_MODE = False

def get_current_working_dir():
    """Get the current working directory."""
    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
    else:
        application_path = os.path.dirname(__file__)
    return application_path

def calc_lines(txt, remove_empty_lines=True):
    """Calculate the number of lines in text."""
    if not txt.strip():
        return 0
    all_lines = txt.strip().split('\n')
    if not remove_empty_lines:
        return len(all_lines)
    else:
        return len([i for i in all_lines if bool(i.strip())])

def copytree(src, dst, skip_existing=True):
    """Copy directory tree with optional skip existing files."""
    if not os.path.exists(dst):
        os.makedirs(dst)
    for root, dirs, files in os.walk(src):
        for dir_ in dirs:
            dest_dir = os.path.join(dst, os.path.relpath(os.path.join(root, dir_), src))
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)
        for file_ in files:
            src_file = os.path.join(root, file_)
            dest_file = os.path.join(dst, os.path.relpath(src_file, src))
            if not skip_existing or not os.path.exists(dest_file):
                shutil.copy2(src_file, dest_file)

class LogFilter(logging.Filter):
    """Custom log filter to suppress specific messages."""
    def filter(self, record):
        if "Unknown property transform-origin" in record.msg or "Unknown property transform" in record.msg:
            return False
        return True

def custom_log_handler(log_context, log_type, message):
    """Custom logging handler."""
    print(message)

# Setup logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
log_filter = LogFilter()
logger.addFilter(log_filter)
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)
logging.basicConfig(format="%(levelname)s: %(message)s")
logging.Handler.logMessage = custom_log_handler
logging.getLogger("PyQt5.QtCore").setLevel(logging.WARNING)
logging.getLogger("PyQt5.QtGui").setLevel(logging.WARNING)
logging.getLogger("PyQt5.QtWidgets").setLevel(logging.WARNING)

class GlowTabBar(QTabBar):
    """Custom tab bar with glow effect."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.current_index = 0
        
    def paintEvent(self, event):
        super().paintEvent(event)
        if self.current_index >= 0:
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing)
            rect = self.tabRect(self.current_index)
            painter.setPen(QColor(0, 150, 255, 100))
            painter.setBrush(QColor(0, 150, 255, 30))
            painter.drawRoundedRect(rect.adjusted(2, 2, -2, -2), 5, 5)
    
    def setCurrentIndex(self, index):
        self.current_index = index
        self.update()

class DiamondSorter(QMainWindow):
    """Main Diamond Sorter application window."""
    finished = pyqtSignal(int)
    
    def __init__(self, directory_path=None, input_textedit=None):
        super(DiamondSorter, self).__init__()
        
        # Load UI file
        ui_file = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'form.ui')
        if os.path.exists(ui_file):
            uic.loadUi(ui_file, self)
        else:
            self.setup_basic_ui()
        
        # Set window properties
        self.setWindowTitle("Diamond Sorter")
        icon_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'assets', 'icons', 'diamond.ico')
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        
        # Apply theme
        self.apply_reaper_theme()
        
        # Setup system tray
        self.setup_system_tray()
        
        # Initialize variables
        self.result = None
        self.console_layout = QVBoxLayout(self.consolewidget) if hasattr(self, 'consolewidget') else None
        if self.console_layout:
            self.console_layout.addWidget(self.consolewidget)
        
        self.setup_buttons()
        self.ask_user_dialog_box = QtWidgets.QInputDialog()
        self.directory_path_text_element = QtWidgets.QTextEdit()
        self.Directory_Path_Text_Element = self.directory_path_text_element
        
        # Create extensions bar
        self.extensions_bar = None  # Will be implemented later
        
        # Setup text widgets
        self.input_text = self.findChild(QTextEdit, "input_text")
        self.output_text = self.findChild(QTextBrowser, "output_text")
        self.removed_data_text = self.findChild(QTextBrowser, "removed_data_text")
        
        if self.input_text:
            self.input_text.textChanged.connect(self.update_line_count)
        if self.output_text:
            self.output_text.textChanged.connect(self.update_line_count)
        if self.removed_data_text:
            self.removed_data_text.textChanged.connect(self.update_line_count)
        
        # Setup word wrap checkbox
        self.enable_wordwrap_checkbox = self.findChild(QCheckBox, "enable_wordwrap_checkbox")
        if self.enable_wordwrap_checkbox:
            self.enable_wordwrap_checkbox.stateChanged.connect(self.toggle_word_wrap)
    
    def setup_basic_ui(self):
        """Setup basic UI if form.ui is not available."""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        # Add basic widgets
        self.input_text = QTextEdit()
        self.output_text = QTextBrowser()
        
        layout.addWidget(QLabel("Input:"))
        layout.addWidget(self.input_text)
        layout.addWidget(QLabel("Output:"))
        layout.addWidget(self.output_text)
    
    def setup_buttons(self):
        """Setup button connections."""
        # This will be implemented based on the actual UI
        pass
    
    def setup_system_tray(self):
        """Setup system tray icon."""
        if QSystemTrayIcon.isSystemTrayAvailable():
            self.tray_icon = QSystemTrayIcon(self)
            icon_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'assets', 'icons', 'diamond.png')
            if os.path.exists(icon_path):
                self.tray_icon.setIcon(QIcon(icon_path))
            else:
                self.tray_icon.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_ComputerIcon))
            
            # Create context menu
            menu = QMenu()
            
            show_action = QAction("Show Application", self)
            show_action.triggered.connect(self.show)
            menu.addAction(show_action)
            
            hide_action = QAction("Hide", self)
            hide_action.triggered.connect(self.hide)
            menu.addAction(hide_action)
            
            menu.addSeparator()
            
            exit_action = QAction("Exit", self)
            exit_action.triggered.connect(self.close)
            menu.addAction(exit_action)
            
            self.tray_icon.setContextMenu(menu)
            self.tray_icon.show()
    
    def apply_reaper_theme(self):
        """Apply the Reaper theme."""
        # Load theme CSS
        theme_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'assets', 'styles', 'reaper_theme.css')
        if os.path.exists(theme_path):
            with open(theme_path, 'r') as f:
                self.setStyleSheet(f.read())
        else:
            # Apply basic dark theme
            self.setStyleSheet("""
                QMainWindow {
                    background-color: #2b2b2b;
                    color: #ffffff;
                }
                QTextEdit, QTextBrowser {
                    background-color: #3c3c3c;
                    color: #ffffff;
                    border: 1px solid #555555;
                }
                QPushButton {
                    background-color: #4a4a4a;
                    color: #ffffff;
                    border: 1px solid #666666;
                    padding: 5px;
                }
                QPushButton:hover {
                    background-color: #5a5a5a;
                }
            """)
    
    def update_line_count(self):
        """Update line count display."""
        # Implementation for line count updates
        pass
    
    def toggle_word_wrap(self, state):
        """Toggle word wrap for text widgets."""
        if self.input_text:
            self.input_text.setLineWrapMode(QTextEdit.WidgetWidth if state else QTextEdit.NoWrap)
        if self.output_text:
            self.output_text.setLineWrapMode(QTextBrowser.WidgetWidth if state else QTextBrowser.NoWrap)
        if self.removed_data_text:
            self.removed_data_text.setLineWrapMode(QTextBrowser.WidgetWidth if state else QTextBrowser.NoWrap)
    
    def closeEvent(self, event):
        """Handle window close event."""
        if hasattr(self, 'tray_icon') and self.tray_icon.isVisible():
            self.hide()
            event.ignore()
        else:
            event.accept()

def main():
    """Main application entry point."""
    app = QApplication(sys.argv)
    
    # Set application properties
    app.setApplicationName("Diamond Sorter")
    app.setApplicationVersion("1.0")
    app.setOrganizationName("Diamond Sorter")
    
    # Create and show main window
    window = DiamondSorter()
    window.show()
    
    # Start event loop
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

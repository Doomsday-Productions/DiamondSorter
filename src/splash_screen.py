#!/usr/bin/env python3
"""
Diamond Sorter - Developer Credit Splash Screen
Shows developer credits and loading animation while the application loads
"""

import sys
import time
import threading
import os
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, 
                            QProgressBar, QHBoxLayout, QFrame)
from PyQt5.QtCore import Qt, QTimer, QThread, pyqtSignal
from PyQt5.QtGui import QPixmap, QFont, QPainter, QColor, QLinearGradient, QBrush

# Multimedia components not needed for Vimeo integration

class LoadingSplashScreen(QWidget):
    """Custom splash screen with developer credits and loading animation."""
    
    def __init__(self):
        super().__init__()
        
        # Set window properties
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedSize(700, 600)  # Further increased size to prevent text cutoff
        
        # Set up the main widget without frame
        self.setStyleSheet("""
            QWidget {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #1a1a2e, stop:0.5 #16213e, stop:1 #0f3460);
                border-radius: 15px;
            }
        """)
        
        # Create layout
        layout = QVBoxLayout()
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(15)
        
        
        # Title
        title_label = QLabel("💎 DIAMOND SORTER")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("""
            QLabel {
                color: #00d4ff;
                font-size: 28px;
                font-weight: bold;
                font-family: 'Segoe UI', Arial, sans-serif;
            }
        """)
        
        # Subtitle
        subtitle_label = QLabel("Advanced Data Processing Tool")
        subtitle_label.setAlignment(Qt.AlignCenter)
        subtitle_label.setStyleSheet("""
            QLabel {
                color: #ffffff;
                font-size: 14px;
                font-family: 'Segoe UI', Arial, sans-serif;
                opacity: 0.8;
            }
        """)
        
        # Developer credits
        credits_label = QLabel("""
        <div style='text-align: center; color: #00d4ff; font-size: 12px; font-family: "Segoe UI", Arial, sans-serif; line-height: 1.4;'>
            <p><b>Developed by:</b></p>
            <p>@LogCachin</p>
            <p>📱 <a href='https://t.me/+FtjFQJNPSWxiZmYx' style='color: #00d4ff; text-decoration: none;'>Telegram Chat</a></p>
            <p>📢 <a href='https://t.me/+NqSqu1v10bwxNTcx' style='color: #00d4ff; text-decoration: none;'>Telegram Channel</a></p>
            <br>
            <p><b>Links:</b></p>
            <p>🌐 <a href='https://reaper-market.com' style='color: #00d4ff; text-decoration: none;'>reaper-market.com</a></p>
            <p>💻 <a href='https://github.com/Doomsday-Productions/' style='color: #00d4ff; text-decoration: none;'>GitHub</a></p>
        </div>
        """)
        credits_label.setOpenExternalLinks(True)
        
        # Loading animation with prominent frame
        loading_frame = QFrame()
        loading_frame.setStyleSheet("""
            QFrame {
                background: rgba(0, 0, 0, 0.6);
                border: 2px solid #00d4ff;
                border-radius: 12px;
                padding: 25px;
            }
        """)
        
        loading_layout = QVBoxLayout()
        loading_layout.setContentsMargins(25, 25, 25, 25)
        
        # Loading text
        self.loading_label = QLabel("Initializing Application...")
        self.loading_label.setAlignment(Qt.AlignCenter)
        self.loading_label.setStyleSheet("""
            QLabel {
                color: #ffffff;
                font-size: 18px;
                font-family: 'Segoe UI', Arial, sans-serif;
                font-weight: bold;
                margin-bottom: 15px;
                text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8);
            }
        """)
        
        # Progress bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                border: 3px solid #00d4ff;
                border-radius: 8px;
                text-align: center;
                background: rgba(0, 0, 0, 0.5);
                height: 35px;
                font-size: 14px;
                font-weight: bold;
                color: #ffffff;
            }
            QProgressBar::chunk {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #00d4ff, stop:0.5 #00aaff, stop:1 #0099cc);
                border-radius: 5px;
            }
        """)
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        
        # Loading dots animation
        self.loading_dots = QLabel("")
        self.loading_dots.setAlignment(Qt.AlignCenter)
        self.loading_dots.setStyleSheet("""
            QLabel {
                color: #ffffff;
                font-size: 28px;
                font-family: 'Segoe UI', Arial, sans-serif;
                font-weight: bold;
                margin-top: 10px;
                text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8);
            }
        """)
        
        loading_layout.addWidget(self.loading_label)
        loading_layout.addWidget(self.progress_bar)
        loading_layout.addWidget(self.loading_dots)
        loading_frame.setLayout(loading_layout)
        
        # Console functions section
        console_frame = QFrame()
        console_frame.setStyleSheet("""
            QFrame {
                background: rgba(0, 0, 0, 0.2);
                border-radius: 10px;
                padding: 12px;
            }
        """)
        
        console_layout = QVBoxLayout()
        console_layout.setContentsMargins(10, 10, 10, 10)
        console_layout.setSpacing(8)
        
        # Console functions title
        console_title = QLabel("🖥️ Console Functions")
        console_title.setAlignment(Qt.AlignCenter)
        console_title.setStyleSheet("""
            QLabel {
                color: rgba(0, 212, 255, 0.9);
                font-size: 12px;
                font-family: 'Segoe UI', Arial, sans-serif;
                font-weight: bold;
            }
        """)
        
        # Console commands
        console_commands = QLabel("""
        <div style='text-align: center; color: rgba(0, 212, 255, 0.7); font-size: 9px; font-family: "Consolas", "Courier New", monospace;'>
            <p><b>🔍 Checking:</b> Dependencies • System Requirements • File Integrity</p>
            <p><b>📦 Loading:</b> Core Modules • UI Components • Data Processors</p>
            <p><b>⚙️ Installing:</b> Essential Packages • Optional Features • Updates</p>
            <p><b>🚀 Launching:</b> Main Application • Services • Background Tasks</p>
        </div>
        """)
        console_commands.setAlignment(Qt.AlignCenter)
        
        console_layout.addWidget(console_title)
        console_layout.addWidget(console_commands)
        console_frame.setLayout(console_layout)
        
        # Add all widgets to main layout
        layout.addWidget(title_label)
        layout.addWidget(subtitle_label)
        layout.addSpacing(10)
        layout.addWidget(credits_label)
        layout.addSpacing(10)
        layout.addWidget(loading_frame)
        layout.addSpacing(8)
        layout.addWidget(console_frame)
        
        self.setLayout(layout)
        
        # Center the splash screen
        self.center_splash()
        
        # Start loading animation
        self.start_loading_animation()
    
    def center_splash(self):
        """Center the splash screen on the screen."""
        screen = QApplication.primaryScreen().geometry()
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2
        self.move(x, y)
    
    def start_loading_animation(self):
        """Start the loading animation."""
        self.progress_value = 0
        self.dots_count = 0
        
        # Timer for progress bar
        self.progress_timer = QTimer()
        self.progress_timer.timeout.connect(self.update_progress)
        self.progress_timer.start(50)  # Update every 50ms
        
        # Timer for dots animation
        self.dots_timer = QTimer()
        self.dots_timer.timeout.connect(self.update_dots)
        self.dots_timer.start(300)  # Update every 300ms
    
    def update_progress(self):
        """Update the progress bar."""
        self.progress_value += 1
        self.progress_bar.setValue(self.progress_value)
        
        if self.progress_value >= 100:
            self.progress_timer.stop()
    
    def update_dots(self):
        """Update the loading dots animation."""
        self.dots_count = (self.dots_count + 1) % 4
        dots = "." * self.dots_count + " " * (3 - self.dots_count)
        self.loading_dots.setText(dots)
    
    def set_loading_text(self, text):
        """Update the loading text."""
        self.loading_label.setText(text)
        
        # Update console functions based on loading stage
        if "core modules" in text.lower():
            self.update_console_status("🔍 Checking Dependencies...")
        elif "ui components" in text.lower():
            self.update_console_status("📦 Loading UI Components...")
        elif "data processors" in text.lower():
            self.update_console_status("⚙️ Installing Data Processors...")
        elif "interface" in text.lower():
            self.update_console_status("🚀 Launching Interface...")
        elif "startup" in text.lower():
            self.update_console_status("✅ Finalizing Startup...")
    
    def update_console_status(self, status):
        """Update the console status display."""
        # This method can be used to update console status if needed
        pass
    
    
    def finish_loading(self):
        """Finish the loading animation."""
        self.progress_bar.setValue(100)
        self.loading_dots.setText("✓")
        self.loading_dots.setStyleSheet("""
            QLabel {
                color: #00ff00;
                font-size: 18px;
                font-family: 'Segoe UI', Arial, sans-serif;
                font-weight: bold;
            }
        """)
    
    

def show_splash_screen(app, duration=3000):
    """Show the splash screen for the specified duration."""
    splash = LoadingSplashScreen()
    splash.show()
    
    # Process events to show the splash screen
    app.processEvents()
    
    # Simulate loading process
    loading_steps = [
        ("Loading core modules...", 500),
        ("Initializing UI components...", 800),
        ("Setting up data processors...", 600),
        ("Preparing interface...", 700),
        ("Finalizing startup...", 400)
    ]
    
    for step_text, step_duration in loading_steps:
        splash.set_loading_text(step_text)
        app.processEvents()
        time.sleep(step_duration / 1000)
    
    # Finish loading
    splash.finish_loading()
    app.processEvents()
    
    # Keep splash screen visible for a moment
    time.sleep(500 / 1000)
    
    return splash

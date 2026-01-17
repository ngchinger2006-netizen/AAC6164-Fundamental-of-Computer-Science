# AAC6164 - Linux Monitoring System

# Course
AAC6164 - Fundamental of Computer Science

# Students
- Name: Ng Ching Er (Student A)
- Name: Nurul Dania Binti Fairos (Student B)

# Role
- Student A is responsible for directory monitoring and file system analysis.
- Student B is responsible for system performance monitoring.

# Project Description
This project is a Linux-based monitoring system written in Python.
It focuses on monitoring directory changes and generating reports based on file system activities.

# Features
- Monitor directory file creation
- Monitor directory file deletion
- Monitor directory file modification
- Generate directory monitoring reports

# Directory Monitoring Module
This module monitors a specific directory called "monitored_dir" and detects file system changes.

# Detected Events
- File creation
- File deletion
- File modification

## How it works
1. The system takes an initial snapshot of the directory
2. It waits for a fixed period (e.g. 60 seconds)
3. Users can create, modify, or delete files during this time
4. A second snapshot is taken and compared with the first one
5. Detected changes are written to a report file

# How to run
1. Open terminal
2. Navigate to the project directory
3. Run the program using:
   ```bash
   python3 main.py

## Output
All detected events are saved in: reports/directory_report.txt

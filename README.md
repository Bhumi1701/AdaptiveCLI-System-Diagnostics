# Adaptive CLI System Diagnostics & Configuration Tool

## Overview

The Adaptive CLI System Diagnostics & Configuration Tool is a Python-based command-line application that provides system diagnostics, hardware monitoring, network diagnostics, configuration utilities, and report generation. The application uses a menu-driven interface to help users monitor the health and performance of their computer system.

This project demonstrates concepts of system programming, modular programming, file handling, network programming, and command-line interface (CLI) development in Python.

---

## Features

- Display system information
- Monitor CPU usage
- Monitor memory (RAM) usage
- Monitor disk usage
- Display battery status
- Perform network diagnostics
  - Internet connectivity check
  - Local IP address
  - DNS lookup
  - Ping test
- Display environment variables
- List available disk partitions
- Show current working directory
- Clear temporary files
- Generate a detailed system health report
- Save the report as a text file

---

## Technologies Used

- Python 3
- psutil

### Python Standard Library Modules

- platform
- socket
- subprocess
- os
- shutil
- tempfile
- getpass
- datetime

---

## Project Structure

```
AdaptiveCLI-System-Diagnostics/
│── main.py
│── diagnostics.py
│── network.py
│── config.py
│── report.py
│── requirements.txt
│── README.md
│── LICENSE
└── .gitignore
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/Bhumi1701/AdaptiveCLI-System-Diagnostics.git
```

### Navigate to the project directory

```bash
cd AdaptiveCLI-System-Diagnostics
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python main.py
```

---

## Menu

```
==================================================
 ADAPTIVE CLI SYSTEM DIAGNOSTICS TOOL
==================================================

1. System Information
2. CPU Usage
3. Memory Usage
4. Disk Usage
5. Battery Status
6. System Health
7. Network Diagnostics
8. Environment Variables
9. Disk Partitions
10. Current Working Directory
11. Clear Temporary Files
12. Generate System Report
13. Save Report to File
0. Exit

==================================================
```

---

## Sample Output

```
===== SYSTEM HEALTH =====

CPU Usage          : 16%
Memory Usage       : 49%
Disk Usage         : 63%
Overall Health     : Excellent
```

---

## Requirements

Install the required dependency using:

```bash
pip install -r requirements.txt
```

**requirements.txt**

```
psutil>=7.0.0
```

---

## Learning Outcomes

- Command Line Interface (CLI) Development
- System Programming in Python
- Modular Programming
- File Handling
- Network Programming
- System Monitoring
- Report Generation
- Exception Handling

---

## Future Enhancements

- Export reports as PDF
- Live system monitoring
- Colored terminal interface
- CPU temperature monitoring
- Logging support
- Scheduled health reports
- Cross-platform enhancements

---

## Author

**Bhumi Thummar**

B.Tech Computer Science and Engineering

VIT Bhopal University

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

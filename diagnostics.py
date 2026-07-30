import platform
import psutil
import socket
import getpass


def get_system_info():
    """
    Returns basic system information.
    """
    info = {
        "Operating System": platform.system(),
        "OS Version": platform.version(),
        "Release": platform.release(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
        "Architecture": platform.architecture()[0],
        "Hostname": socket.gethostname(),
        "Current User": getpass.getuser(),
        "Total RAM (GB)": round(psutil.virtual_memory().total / (1024 ** 3), 2)
    }

    return info


def get_cpu_usage():
    """
    Returns CPU usage percentage.
    """
    return psutil.cpu_percent(interval=1)


def get_memory_usage():
    """
    Returns memory statistics.
    """
    memory = psutil.virtual_memory()

    return {
        "Total (GB)": round(memory.total / (1024 ** 3), 2),
        "Used (GB)": round(memory.used / (1024 ** 3), 2),
        "Available (GB)": round(memory.available / (1024 ** 3), 2),
        "Usage (%)": memory.percent
    }


def get_disk_usage():
    """
    Returns disk statistics.
    """
    disk = psutil.disk_usage('/')

    return {
        "Total (GB)": round(disk.total / (1024 ** 3), 2),
        "Used (GB)": round(disk.used / (1024 ** 3), 2),
        "Free (GB)": round(disk.free / (1024 ** 3), 2),
        "Usage (%)": disk.percent
    }


def get_battery_info():
    """
    Returns battery information if available.
    """
    battery = psutil.sensors_battery()

    if battery is None:
        return {
            "Battery": "Not Available"
        }

    return {
        "Battery Percentage": f"{battery.percent}%",
        "Power Plugged": battery.power_plugged,
        "Time Left": battery.secsleft
    }


def get_system_health():
    """
    Returns a summary of overall system health.
    """
    cpu = get_cpu_usage()
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    if cpu < 60 and memory < 70 and disk < 80:
        status = "Excellent"
    elif cpu < 80 and memory < 85 and disk < 90:
        status = "Good"
    else:
        status = "Needs Attention"

    return {
        "CPU Usage": cpu,
        "Memory Usage": memory,
        "Disk Usage": disk,
        "Overall Health": status
    }


if __name__ == "__main__":

    print("===== SYSTEM INFORMATION =====")
    for key, value in get_system_info().items():
        print(f"{key}: {value}")

    print("\n===== CPU =====")
    print(get_cpu_usage(), "%")

    print("\n===== MEMORY =====")
    print(get_memory_usage())

    print("\n===== DISK =====")
    print(get_disk_usage())

    print("\n===== BATTERY =====")
    print(get_battery_info())

    print("\n===== HEALTH =====")
    print(get_system_health())
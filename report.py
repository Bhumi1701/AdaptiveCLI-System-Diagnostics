from datetime import datetime
from diagnostics import (
    get_system_info,
    get_cpu_usage,
    get_memory_usage,
    get_disk_usage,
    get_battery_info,
    get_system_health,
)
from network import (
    check_internet,
    get_local_ip,
)


def generate_report():
    """
    Generates a complete system health report.
    """

    system_info = get_system_info()
    cpu = get_cpu_usage()
    memory = get_memory_usage()
    disk = get_disk_usage()
    battery = get_battery_info()
    health = get_system_health()
    internet = "Connected" if check_internet() else "Not Connected"
    ip = get_local_ip()

    report = []

    report.append("=" * 60)
    report.append("SYSTEM DIAGNOSTICS REPORT")
    report.append("=" * 60)
    report.append(f"Generated On : {datetime.now()}")
    report.append("")

    report.append("SYSTEM INFORMATION")
    report.append("-" * 60)
    for key, value in system_info.items():
        report.append(f"{key:20}: {value}")

    report.append("")
    report.append("CPU")
    report.append("-" * 60)
    report.append(f"CPU Usage           : {cpu}%")

    report.append("")
    report.append("MEMORY")
    report.append("-" * 60)
    for key, value in memory.items():
        report.append(f"{key:20}: {value}")

    report.append("")
    report.append("DISK")
    report.append("-" * 60)
    for key, value in disk.items():
        report.append(f"{key:20}: {value}")

    report.append("")
    report.append("BATTERY")
    report.append("-" * 60)
    for key, value in battery.items():
        report.append(f"{key:20}: {value}")

    report.append("")
    report.append("NETWORK")
    report.append("-" * 60)
    report.append(f"Internet Status     : {internet}")
    report.append(f"Local IP Address    : {ip}")

    report.append("")
    report.append("SYSTEM HEALTH")
    report.append("-" * 60)
    for key, value in health.items():
        report.append(f"{key:20}: {value}")

    report.append("")
    report.append("=" * 60)

    return "\n".join(report)


def save_report(filename="system_report.txt"):
    """
    Saves the report to a text file.
    """
    report = generate_report()

    with open(filename, "w", encoding="utf-8") as file:
        file.write(report)

    return filename


if __name__ == "__main__":

    report = generate_report()
    print(report)

    choice = input("\nDo you want to save this report? (y/n): ")

    if choice.lower() == "y":
        filename = save_report()
        print(f"\nReport saved as '{filename}'")
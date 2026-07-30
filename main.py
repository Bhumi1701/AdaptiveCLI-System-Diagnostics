from diagnostics import (
    get_system_info,
    get_cpu_usage,
    get_memory_usage,
    get_disk_usage,
    get_battery_info,
    get_system_health
)

from network import (
    check_internet,
    get_local_ip,
    dns_lookup,
    ping_host
)

from config import (
    show_environment_variables,
    clear_temp_files,
    get_current_directory,
    list_disk_partitions
)

from report import (
    generate_report,
    save_report
)


def print_menu():
    print("\n" + "=" * 50)
    print(" ADAPTIVE CLI SYSTEM DIAGNOSTICS TOOL ")
    print("=" * 50)
    print("1. System Information")
    print("2. CPU Usage")
    print("3. Memory Usage")
    print("4. Disk Usage")
    print("5. Battery Status")
    print("6. System Health")
    print("7. Network Diagnostics")
    print("8. Environment Variables")
    print("9. Disk Partitions")
    print("10. Current Working Directory")
    print("11. Clear Temporary Files")
    print("12. Generate System Report")
    print("13. Save Report to File")
    print("0. Exit")
    print("=" * 50)


def show_system_info():
    print("\n===== SYSTEM INFORMATION =====")
    info = get_system_info()
    for key, value in info.items():
        print(f"{key:20}: {value}")


def show_cpu():
    print(f"\nCPU Usage : {get_cpu_usage()}%")


def show_memory():
    print("\n===== MEMORY =====")
    memory = get_memory_usage()

    for key, value in memory.items():
        print(f"{key:20}: {value}")


def show_disk():
    print("\n===== DISK =====")
    disk = get_disk_usage()

    for key, value in disk.items():
        print(f"{key:20}: {value}")


def show_battery():
    print("\n===== BATTERY =====")

    battery = get_battery_info()

    for key, value in battery.items():
        print(f"{key:20}: {value}")


def show_health():
    print("\n===== SYSTEM HEALTH =====")

    health = get_system_health()

    for key, value in health.items():
        print(f"{key:20}: {value}")


def network_menu():
    print("\n===== NETWORK =====")

    print("Internet :", "Connected" if check_internet() else "Not Connected")
    print("Local IP :", get_local_ip())

    domain = input("\nEnter Domain (example google.com): ")
    print("Resolved IP :", dns_lookup(domain))

    host = input("Enter Host to Ping : ")
    print("\nPing Result:\n")
    print(ping_host(host))


def environment_menu():
    env = show_environment_variables()

    print("\n===== ENVIRONMENT VARIABLES =====")

    count = 0

    for key, value in env.items():
        print(f"{key} = {value}")

        count += 1

        if count == 15:
            print("...Showing first 15 variables only...")
            break


def partition_menu():
    print("\n===== DISK PARTITIONS =====")

    for partition in list_disk_partitions():
        print("-" * 40)
        for key, value in partition.items():
            print(f"{key:15}: {value}")


def main():

    while True:

        print_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            show_system_info()

        elif choice == "2":
            show_cpu()

        elif choice == "3":
            show_memory()

        elif choice == "4":
            show_disk()

        elif choice == "5":
            show_battery()

        elif choice == "6":
            show_health()

        elif choice == "7":
            network_menu()

        elif choice == "8":
            environment_menu()

        elif choice == "9":
            partition_menu()

        elif choice == "10":
            print("\nCurrent Directory:")
            print(get_current_directory())

        elif choice == "11":
            result = clear_temp_files()

            print("\nTemporary Files Cleanup")
            print(result)

        elif choice == "12":
            print("\n")
            print(generate_report())

        elif choice == "13":
            filename = save_report()
            print(f"\nReport saved as '{filename}'")

        elif choice == "0":
            print("\nThank you for using the Adaptive CLI System Diagnostics Tool!")
            break

        else:
            print("\nInvalid Choice! Please try again.")


if __name__ == "__main__":
    main()
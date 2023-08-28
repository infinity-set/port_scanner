import socket
import re

def scan_ports(target, ports):
    print(f"Scanning target: {target}")
    for port in ports:
        # Create a socket using IPv4 and TCP protocol
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Set a timeout for the connection attempt (in seconds)
        sock.settimeout(1)

        # Try to connect to the target's IP address and port
        try:
            result = sock.connect_ex((target, port))
        except:
            print(f"Cannot make connection to host '{target}'")
            break

        if result == 0:
            # If the result is 0, the connection was successful (port is open)
            print(f"***Port {port} is open***")

            # Open a file in append mode and write the open port information
            with open(f"./port_scan_host_{target}.txt", "a") as file:
                file.write(f"{port}\n")
        else:
            # If the result is not 0, the connection failed (port is closed)
            print(f"Port {port} is closed")

        # Close the socket connection
        sock.close()


# Define a function to check if the input string is a valid IPv4 address
def is_valid_ipv4(input_str):
    # Define a regular expression pattern for valid IPv4 addresses
    ipv4_pattern = r'^(\d{1,3}\.){3}\d{1,3}$'

    # Use the re.match() function to check if the input matches the IPv4 pattern
    # If a match is found, the input is a valid IPv4 address, so return True
    # If no match is found, the input is not a valid IPv4 address, so return False
    return re.match(ipv4_pattern, input_str) is not None


# Define a function to get a positive integer input from the user
def get_positive_integer_input(prompt):
    while True:
        try:
            # Try to convert user input to an integer
            value = int(input(prompt))

            # Check if the value is non-negative (positive or zero)
            if value >= 0:
                return value
            else:
                # Print an error message if the value is negative
                print("Must be a positive number")
        except ValueError:
            # Handle the case where the input cannot be converted to an integer
            print("Invalid input")


def main():
    print("""
██████╗░░█████╗░██████╗░████████╗  ░██████╗░█████╗░░█████╗░███╗░░██╗███╗░░██╗███████╗██████╗░
██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝  ██╔════╝██╔══██╗██╔══██╗████╗░██║████╗░██║██╔════╝██╔══██╗
██████╔╝██║░░██║██████╔╝░░░██║░░░  ╚█████╗░██║░░╚═╝███████║██╔██╗██║██╔██╗██║█████╗░░██████╔╝
██╔═══╝░██║░░██║██╔══██╗░░░██║░░░  ░╚═══██╗██║░░██╗██╔══██║██║╚████║██║╚████║██╔══╝░░██╔══██╗
██║░░░░░╚█████╔╝██║░░██║░░░██║░░░  ██████╔╝╚█████╔╝██║░░██║██║░╚███║██║░╚███║███████╗██║░░██║
╚═╝░░░░░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░  ╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝
    """)

    # Loop to get a valid IPv4 address from the user
    while True:
        target_host = input("Enter the IPv4 Address of the target to scan: ")
        if is_valid_ipv4(target_host):
            break
        else:
            print("    **Enter a valid IPv4 address.**\n")

    # Get the starting and ending port numbers from the user
    starting_port = get_positive_integer_input("Enter the starting port number: ")

    ending_port = get_positive_integer_input("Enter the ending port number: ")
    while ending_port <= starting_port:
        print("Ending port must be greater than the starting port.")
        ending_port = get_positive_integer_input("Enter the ending port number: ")

    # Create a range of target ports
    target_ports = range(starting_port, ending_port + 1)

    # Print verification details
    print("\nVerification:")
    print(f"Host: {target_host}")
    print(f"Ports: {starting_port}-{ending_port}")

    # Loop to get user confirmation for conducting the scan
    while True:
        conduct_scan = input("\nConduct scan? (Type 'Yes' or 'No'): ").lower()
        if conduct_scan in ["yes", "no"]:
            break
        else:
            print("Please enter 'Yes' or 'No'.")

    # Conduct the scan if user confirmed
    if conduct_scan == "yes":
        scan_ports(target_host, target_ports)
    else:
        print("Port scan aborted.")

# Entry point of the program
if __name__ == "__main__":
    main()





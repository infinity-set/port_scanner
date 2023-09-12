## Simple Port Scanner

Welcome to the Simple Port Scanner – your entry point to understanding the basic concepts of port scanning! 
This Python script offers a beginner-friendly introduction to the world of network security by allowing you to explore the fundamentals of identifying open ports on a target host.

## Table of Contents

- [Description](#description)
- [Why Use This Script?](#why-use-this-script)
- [Languages and Utilities Used](#languages-and-utilities-used)
- [Environments Used](#environments-used)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [Program Walk-Through](#program-walk-through)


## Description
Port scanning is a crucial technique in the field of cybersecurity. It involves probing a network or a computer system for open ports,
which can provide valuable insights into potential vulnerabilities and the services running on a machine. The Simple Port Scanner script provides an
approachable way to learn about port scanning by walking you through the process of scanning for open ports on a specified target host.

This script is designed with simplicity in mind, making it an ideal starting point for those new to the concept of port scanning. It doesn't encompass the complexities
of advanced scanning tools but offers a hands-on opportunity to explore the basic mechanics.

<br />

## Why Use This Script?

- <b>Educational Purpose:</b> The script is an educational tool that introduces you to the fundamental principles of port scanning. It's perfect for those who want to learn how port scanning works before diving into more complex tools.

- <b>Hands-On Learning:</b> By using this script, you'll gain hands-on experience in initiating connections to various ports and understanding their status.

- <b>Simplified Approach:</b> The script's simplicity makes it a suitable resource for beginners who want to grasp the basics of port scanning without overwhelming technical details.

- <b>Ethical Considerations:</b> Port scanning should always be conducted responsibly and with the necessary permissions. This script emphasizes the importance of ethical scanning practices.

-  <b>Port Record:</b> The script creates a text file named <b>port_scan_host_<i>{target}</i>.txt</b>, which contains a record of the open ports on the scanned target host. This feature can be helpful for further analysis and documentation.
<br />


## Languages and Utilities Used

- <b>Python</b> 
- <b>PyCharm</b>

[<img align="center" alt="PyCharm Icon" width="50px" src="https://upload.wikimedia.org/wikipedia/commons/1/1d/PyCharm_Icon.svg" />][pycharm]
[<img align="left" alt="Python Icon" width="40px" src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" />][python]

[pycharm]: https://www.jetbrains.com/pycharm/
[python]: https://www.python.org/

## Environments Used 

- <b>Windows 10</b>

[<img align="left" alt="Microsoft Icon" width="35px" src="https://upload.wikimedia.org/wikipedia/commons/3/34/Windows_logo_-_2012_derivative.svg" />][windows]

[windows]: https://www.microsoft.com/
<br /><br />

## Dependencies 

- <b>Python's socket Library:</b> The script utilizes the <b><i>socket</i></b> library to handle low-level network communication, enabling connections to target hosts' IP addresses and specific ports.
<br>

- <b>Python's re Library:</b> The <b><i>re</i></b> library is employed for working with regular expressions, specifically for validating IPv4 addresses using a predefined pattern.

## Usage 

1. Run the script.
2. Enter the IPv4 address of the target host you want to scan. Make sure it's a valid IPv4 address. If the entered address is invalid, the script will prompt you to enter a valid one.
3. Provide the range of ports you want to scan. You'll be asked to enter the starting and ending port numbers. The script validates these inputs to ensure they are positive integers and that the ending port is greater than the starting port.
4. You'll be asked whether you want to proceed with the scan. Enter either "Yes" or "No" to confirm or cancel the scan.
5. The script will start scanning the specified range of ports on the target host. For each port, it will attempt to establish a connection and determine if the port is open or closed.
6. After scanning is complete, the script will display whether each port is open or closed based on the connection result. Additionally, a text file named port_scan_host_{target}.txt will be created in the script's directory.
 This file will contain a list of open ports from the scan.
7. You can use the generated text file for further analysis, documentation, or exploration of the open ports on the target host.
8. The script will exit after displaying the results. You can re-run the script for scanning different target hosts or port ranges.

<br /><br />

## Program Walk-Through

<p align="center">
Launch PyCharm and Run the file: <br/>
<img src="https://github.com/infinity-set/port_scanner/assets/142350896/1f49c6e0-5281-4f2e-b49f-5ae22a10eee7" height="80%" width="80%" alt="Run PyCharm File"/>
<br />
<br />
Follow the prompts: <br/>
<img src="https://github.com/infinity-set/port_scanner/assets/142350896/0dc4d80a-3a95-436e-b506-330d95abd20c" height="80%" width="80%" alt="Encryption Steps"/>
<br />
<br />
Generated Text File: <br/>
<img src="https://github.com/infinity-set/port_scanner/assets/142350896/754be26d-a9c9-419b-9a3c-1bd6bc797b43" height="80%" width="80%" alt="Encryption/Decryption Key"/>
<br />  
</p>

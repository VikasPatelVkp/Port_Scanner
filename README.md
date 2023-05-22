![Screenshot (3601)](https://github.com/VikasPatelVkp/Port_Scanner/assets/54985292/027a7401-11b5-4000-b6f3-0ce84f6d0eed)

# Port Scanner 

A simple Python script that allows user to scan a range of ports on a target IP address and identifies which ports are open. If port is open it identifies service running on it. 

It uses the socket library for network communication. 

It utilizes threading for concurrent scanning of multiple ports. 


## Author
This Port Scanner script was created by **_Vikas Patel_**.
- [@VikasPatelVkp](https://github.com/VikasPatelVkp)
## Demo
 ![Screenshot (3602)](https://github.com/VikasPatelVkp/Port_Scanner/assets/54985292/65e57cbf-dae0-49ef-85f0-5d48fe368bff)

## Dependencies

The Port Scanner script relies on the following external libraries:

**sys:** Provides access to command-line arguments.

**socket:** Enables network communication and socket operations.

**threading:** Allows concurrent execution of port scanning.

**pyfiglet:** Generates ASCII art banners for program.

**termcolor:** Provides colored output.

**datetime:** Used for displaying the scan start time.

Ensure that these dependencies are installed before running the script.

## Deployment

To deploy the Port Scanner on your system, you can follow these steps:

1- Clone the repository or download the script file.

2- Make sure you have Python 3.x installed on your system.

3- Install the required dependencies by running the following command:

```bash
  pip install pyfiglet 
  pip install termcolor
```
Open a terminal or command prompt and navigate to the directory containing the script.

Run the script using the following syntax command:


### Syntax
```bash
 python3 Port_Scanner.py <IP address> <start port> <end port>
```
Replace <IP address> with the target IP address you want to scan.
Replace <start port> and <end port> with the range of ports you want to scan.






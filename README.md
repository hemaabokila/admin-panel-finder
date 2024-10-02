
# Admin Panel Finder

## Overview

Admin Panel Finder is a powerful tool designed to help security professionals and developers locate admin panels on websites using a customizable wordlist. This tool employs multi-threading to enhance scanning speed and efficiency, making it ideal for penetration testing and security assessments.

## Features

- **Multi-threading**: Perform scans faster by using multiple threads.
- **Custom Wordlists**: Specify your own wordlist or use the default.
- **User-friendly Output**: Easily identify found or missing admin panels with clear messages.
- **Signal Handling**: Gracefully stop execution with a simple keyboard interrupt (Ctrl+C).

## Requirements

- Python 3.6 or higher
- `requests` library
- `colorama` library

## Installation
```
$ git clone https://github.com/hemaabokila/admin-panel.git
$ cd adminp
$ pip install .
$ adminp
```

- **To install the required libraries, use the following command**:

```
pip install requests colorama
```
## Usage
- **Run the tool from the command line using the following syntax**:

```
adminp <url> [-w <wordlist>] [-t <threads>] [-to <timeout>]
```
## Parameters:
```
<url>: The target URL to scan.
-w <wordlist>: (Optional) Path to a custom wordlist file (default is admin.txt in the wordlists directory).
-t <threads>: (Optional) Number of threads to use (default is 10).
-to <timeout>: (Optional) Request timeout in seconds (default is 5).
```
## Example
- **To scan a website using the default wordlist**:

```
adminp http://example.com
```
- **To use a custom wordlist and specify the number of threads**:

```
adminp http://example.com -w /path/to/your_wordlist.txt -t 5
```
## Contributing
- **Contributions are welcome! If you have suggestions or improvements, please create an issue or submit a pull request**.


## Acknowledgements
- **Requests for making HTTP requests simpler**.
- **Colorama for enhancing console output with colors**.
## Contact
- **For questions or feedback, feel free to reach out to me at ibrahemabokila@gmail.com**.
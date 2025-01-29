### **Descrizione / Description**
Uno scanner di rete è uno strumento utilizzato per individuare dispositivi connessi a una rete locale, raccogliendo informazioni come indirizzi IP e MAC. Questo strumento è utile per amministratori di sistema, esperti di sicurezza e utenti avanzati che vogliono monitorare e gestire i dispositivi collegati alla propria rete.

A network scanner is a tool used to identify devices connected to a local network, gathering information such as IP and MAC addresses. This tool is useful for system administrators, security experts, and advanced users who want to monitor and manage devices connected to their network.

### **1. Requisiti / Requirements**
Prima di eseguire lo scanner di rete, assicurati di avere installato Python e la libreria Scapy. Lo script richiede anche privilegi di amministratore.

Before running the network scanner, ensure you have installed Python and the Scapy library. The script also requires administrator privileges.

### **2. Installazione di Python e Scapy / Installing Python and Scapy**
- **Linux (Ubuntu/Debian):**
  ```bash
  sudo apt update && sudo apt install python3 python3-pip
  pip3 install scapy
  ```
- **Windows:**
  1. Scarica e installa Python da [python.org](https://www.python.org/)
  2. Apri il terminale (PowerShell o Prompt dei comandi) ed esegui:
     ```powershell
     pip install scapy
     ```
  
  1. Download and install Python from [python.org](https://www.python.org/)
  2. Open the terminal (PowerShell or Command Prompt) and run:
     ```powershell
     pip install scapy
     ```

- **macOS:**
  ```bash
  brew install python3
  pip3 install scapy
  ```

### **3. Esecuzione dello Scanner / Running the Scanner**
Assicurati di eseguire lo script con privilegi di amministratore.

Make sure to run the script with administrator privileges.

- **Linux/macOS:**
  ```bash
  sudo python3 network_scanner.py -t 192.168.1.1/24
  ```
- **Windows (PowerShell con privilegi di amministratore / PowerShell with administrator privileges):**
  ```powershell
  python network_scanner.py -t 192.168.1.1/24
  ```

### **4. Risoluzione dei Problemi / Troubleshooting**
- **Permessi Negati / Permission Denied:** Se ricevi un errore di permessi, assicurati di eseguire il comando come amministratore (usando `sudo` su Linux/macOS o aprendo PowerShell come amministratore su Windows).

  If you receive a permission error, make sure to run the command as an administrator (using `sudo` on Linux/macOS or opening PowerShell as an administrator on Windows).

- **Scapy non installato / Scapy not installed:** Se ricevi un errore `ModuleNotFoundError: No module named 'scapy'`, assicurati che Scapy sia installato con `pip install scapy`.

  If you receive a `ModuleNotFoundError: No module named 'scapy'` error, ensure Scapy is installed using `pip install scapy`.

- **Firewall:** Alcuni firewall potrebbero bloccare le richieste ARP, disattivali temporaneamente per testare lo scanner.

  Some firewalls may block ARP requests, temporarily disable them to test the scanner.

Seguendo questi passaggi, dovresti essere in grado di eseguire lo scanner di rete su qualsiasi sistema operativo!

By following these steps, you should be able to run the network scanner on any operating system!


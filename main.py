import scapy.all as scapy
import argparse

# Funzione per ottenere gli argomenti dalla riga di comando
# Function to get command-line arguments
def get_arguments():
    parser = argparse.ArgumentParser(description="Scanner di rete / Network scanner")
    parser.add_argument("-t", "--target", dest="target", required=True, help="IP range o indirizzo IP target")
    args = parser.parse_args()
    return args.target

# Funzione per scansionare la rete
# Function to scan the network
def scan(ip):
    # Creazione di una richiesta ARP per ottenere l'indirizzo MAC
    # Creating an ARP request to get the MAC address
    arp_request = scapy.ARP(pdst=ip)
    
    # Creazione di un pacchetto Ethernet per inviare la richiesta ARP
    # Creating an Ethernet packet to send the ARP request
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    
    # Combinazione dei due pacchetti
    # Combining the two packets
    arp_request_broadcast = broadcast / arp_request
    
    # Invio del pacchetto e ricezione delle risposte
    # Sending the packet and receiving responses
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    
    # Lista dei dispositivi rilevati
    # List of detected devices
    clients_list = []
    for element in answered_list:
        client_info = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_info)
    
    return clients_list

# Funzione per visualizzare i risultati
# Function to display results
def print_result(results_list):
    print("IP Address\t\tMAC Address")
    print("-----------------------------------------")
    for client in results_list:
        print(client["ip"] + "\t" + client["mac"])

# Ottenimento dell'argomento target
# Getting the target argument
target_ip = get_arguments()

# Esecuzione della scansione
# Running the scan
scan_result = scan(target_ip)

# Stampa dei risultati
# Printing the results
print_result(scan_result)

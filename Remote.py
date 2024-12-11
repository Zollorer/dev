import socket
import os

def send_wol(mac_address):
    # MAC-Adresse in Bytes umwandeln
    mac_bytes = bytes.fromhex(mac_address.replace(":", "").replace("-", ""))
    # Magic Packet erstellen
    magic_packet = b'\xff' * 6 + mac_bytes * 16
    # Magic Packet senden
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.sendto(magic_packet, ("<broadcast>", 9))

def start_remote_desktop(hostname, username=None, password=None):
    # Grundbefehl für Remote Desktop
    command = f"mstsc /v:{hostname}"
    
    if username and password:
        # Optional: RDP-Datei mit Credentials erstellen
        rdp_content = f"""
        screen mode id:i:2
        use multimon:i:0
        desktopwidth:i:1920
        desktopheight:i:1080
        session bpp:i:32
        winposstr:s:0,3,0,0,800,600
        full address:s:{hostname}
        username:s:{username}
        """
        with open("temp_connection.rdp", "w") as rdp_file:
            rdp_file.write(rdp_content)
        command = "mstsc temp_connection.rdp"
    
    os.system(command)

# Beispielnutzung: Wake-on-LAN
send_wol("F0:2F:74:1A:D2:02")

# Beispielnutzung: Remote Desktop starten
start_remote_desktop("192.168.178.10", username="sonne")

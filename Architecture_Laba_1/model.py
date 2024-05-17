import ipaddress
import netifaces
from PyQt6.QtCore import QObject, pyqtSignal


class NetworkParams(QObject):
    changed = pyqtSignal()

    def __init__(self):
        super().__init__()

        self._start_ip = ipaddress.IPv4Address('0.0.0.0')
        self._end_ip = ipaddress.IPv4Address('255.255.255.255')
        self._result_text = ""

    def set_start_ip(self, start_ip):
        try:
            self._start_ip = ipaddress.IPv4Address(start_ip)
            self.calculate_network_params()
        except ValueError:
            self._result_text = "Некорректный начальный IP-адрес"
            self.changed.emit()

    def set_end_ip(self, end_ip):
        try:
            self._end_ip = ipaddress.IPv4Address(end_ip)
            self.calculate_network_params()
        except ValueError:
            self._result_text = "Некорректный конечный IP-адрес"
            self.changed.emit()

    def get_start_ip(self):
        return str(self._start_ip)

    def get_end_ip(self):
        return str(self._end_ip)

    def get_result_text(self):
        return self._result_text

    def __set_mac_address(self, interface):
        try:
            return netifaces.ifaddresses(interface)[netifaces.AF_LINK][0]["addr"]
        except KeyError:
            return "MAC-адрес не найден"

    def calculate_network_params(self):
        start_int = int(self._start_ip)
        end_int = int(self._end_ip)

        common_bits = bin(start_int ^ end_int).count('1')
        mask_length = 32 - common_bits

        try:
            ip_network = ipaddress.ip_network(f"{self._start_ip}/{mask_length}", strict=False)
            network_address = ip_network.network_address
            broadcast_address = ip_network.broadcast_address
            netmask = ip_network.netmask

            try:
                mac_address = self.__set_mac_address(netifaces.interfaces()[0])
            except IndexError:
                mac_address = "MAC-адрес не найден"

            self._result_text = (f"Адрес сети: {network_address}\n"
                                 f"Broadcast-адрес: {broadcast_address}\n"
                                 f"MAC-Адрес: {mac_address}\n"
                                 f"Маска сети: {netmask}\n")

            self.changed.emit()
        except ValueError as e:
            self._result_text = str(e)
            self.changed.emit()

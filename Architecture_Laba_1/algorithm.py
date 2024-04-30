import random


def ipToBinary(ip):
    binaryIp = ''
    ipParts = ip.split('.')
    for part in ipParts:
        binaryIp += bin(int(part))[2:].zfill(8)
    return binaryIp


def binaryToIp(binary):
    ip = ''
    for i in range(0, len(binary), 8):
        ip += str(int(binary[i:i+8], 2)) + '.'
    return ip[:-1]


def generateMac():
    mac = [0x00, 0x16, 0x3e,
           random.randint(0x00, 0x7f),
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff)]
    macAddress = ''
    for byte in mac:
        macAddress += "%02x" % byte + ':'
    return macAddress[:-1]


def calculateNetworkParams(ipRange):
    if '/' not in ipRange or ipRange.count('/') != 1:
        return None
        
    ip, subnet = ipRange.split('/')
    ipBinary = ipToBinary(ip)
    
    networkAddress = binaryToIp(ipBinary[:int(subnet)] + '0' * (32 - int(subnet)))
    broadcastAddress = binaryToIp(ipBinary[:int(subnet)] + '1' * (32 - int(subnet)))
    networkMask = binaryToIp('1' * int(subnet) + '0' * (32 - int(subnet)))
    macAddress = generateMac()
    
    networkParams = [networkAddress, broadcastAddress, networkMask, macAddress]

    return networkParams


def validateIp(ip):
    allowed_characters = set("0123456789./")
    if set(ip) - allowed_characters:
        return False
    
    parts = ip.split('/')
    if len(parts) != 2:
        return False
    
    ipParts = parts[0].split('.')
    if len(ipParts) != 4:
        return False
    
    try:
        prefixLength = int(parts[1])
        if prefixLength < 0 or prefixLength > 32:
            return False
        
        for part in ipParts:
            num = int(part)
            if num < 0 or num > 255:
                return False
        
        return True
    except ValueError:
        return False
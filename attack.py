from scapy.all import *
def send_rst(src_ip, dst_ip, src_port, dst_port):
    # 构造RST报文并发送
    send(IP(src=src_ip, dst=dst_ip, ttl=1) / TCP(seq=1, ack=1, sport=src_port, dport=dst_port, flags="R"))

def main():
    # 定义源IP地址、目标IP地址和目标端口
    src_ip = "192.168.3.4"
    dst_ip = "82.157.125.228"
    dst_port = 80

    # 循环遍历源端口范围，并发送RST报文
    for src_port in range(50000, 50010):
        send_rst(src_ip, dst_ip, src_port, dst_port)

if __name__ == "__main__":
    main()
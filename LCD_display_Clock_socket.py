import serial
import psutil
import time
import socket
sleeptime = 1

def socket_start():
    global sock
    sock = socket.socket()
    host = "192.168.31.6"
    port = 8080
    sock.connect((host, port))
    print("Connected . . .")

def socket_send(st):
    sock.sendall(bytes("$%s" % st, encoding="utf-8"))
    print("sent:%s"%st)


def bytes_received():
    traffic = psutil.net_io_counters(pernic=False, nowrap=False)
    return traffic.bytes_recv

def SerialConnect():
    try:
        global ser

        ser = serial.Serial('COM8', 9600, timeout=200)
        if ser.is_open == True:
            print("Connected")
    except:
        print("fonction SerialConnect, Check if you had connect to port or not.")

def Get_cpu_usage():
    cpu_usage = psutil.cpu_percent()
    return  cpu_usage

def VPN_connection_checker(file_name = 'uk4105.nordvpn.com.udp.log'):
    path = "C://Users//66405//OpenVPN//log//" + file_name
    fo = open(path,encoding="utf-8")
    info_list = []
    for line in fo:
        line = line.replace("\n", "")
        info_list.append(line.strip(","))
    fo.close()
    if info_list[-1].find('CONNECTED,SUCCESS') != -1:
        return True
    elif info_list[-1].find('Control Channel:') != -1:
        return True
    else:
        return False

def serial_input(A = str):
    str(A)
    input_intiger = A
    bytes_converter_variable = str(input_intiger)
    bstr = bytes( bytes_converter_variable, encoding="utf8")
    ser.write(bstr)
    #print("\ryou had write:{}".format(bstr),end="")   #Print what you had write


def LCD_str_inputmaker(input_str = ""):
    str_lis = input_str.split('&')
    output_str = ""
    for i in str_lis:
        formed_str =  i.ljust(40)
        output_str = output_str + formed_str
    return output_str



def main():
    socket_start()
    while True:
        localtime = time.asctime(time.localtime(time.time()))
        localtime = str(localtime)
        s = "{}&{}".format(localtime[0:11],localtime[11:])
        socket_send(LCD_str_inputmaker(s))
        #socket_send(LCD_str_inputmaker(s.lower()))
        time.sleep(sleeptime)

if __name__ == '__main__':
    main()



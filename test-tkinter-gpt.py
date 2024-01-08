import socket
import threading
import tkinter as tk
from queue import Queue

class SocketListener:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))
        self.data = ""

    def read_data(self):
        self.data = self.socket.recv(1024).decode("utf-8")

    def close(self):
        self.socket.close()

class MyGridWindow:
    def __init__(self, ip_list_file):
        self.socket_listeners = []
        self.main_window = tk.Tk()
        self.data_queue = Queue()

        i = 0
        ip_list = self.read_ip_list_from_file(ip_list_file)
        for ip in ip_list:
            i += 1
            label = tk.Label(self.main_window, text=f"Data from Socket {i} ({ip}):")
            label.pack(side=tk.LEFT)

            entry = tk.Entry(self.main_window)
            entry.pack(side=tk.LEFT)

            self.socket_listeners.append(SocketListener(ip, 12345))
            threading.Thread(target=self.update_data_from_socket, args=(i,)).start()

        update_button = tk.Button(self.main_window, text="Update Grid", command=self.on_update_button_clicked)
        update_button.pack(side=tk.LEFT)

        # Set up event handler for updating the UI
        self.main_window.after(100, self.check_queue)

    def read_ip_list_from_file(self, file_path):
        with open(file_path, 'r') as file:
            ip_list = file.read().splitlines()
        return ip_list

    def update_data_from_socket(self, index):
        while True:
            self.socket_listeners[index - 1].read_data()
            data = (index, self.socket_listeners[index - 1].data)
            self.data_queue.put(data)
            self.main_window.after(5000)  # Sleep for 5 seconds

    def check_queue(self):
        try:
            data = self.data_queue.get_nowait()
            self.update_ui(data)
        except Queue.Empty:
            pass
        self.main_window.after(100, self.check_queue)

    def update_ui(self, data):
        index, value = data
        entry = self.main_window.children[f'!entry{index}']
        entry.delete(0, tk.END)
        entry.insert(tk.END, value)

    def on_update_button_clicked(self):
        pass  # Placeholder for additional update logic if needed

if __name__ == "__main__":
    ip_list_file = "ip_list.txt"
    my_grid_window = MyGridWindow(ip_list_file)
    my_grid_window.main_window.mainloop()


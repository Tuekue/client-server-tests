import socket
import threading
from gi.repository import Gtk, GObject

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

class MyGridWindow(Gtk.Window):
    def __init__(self, ip_list_file):
        Gtk.Window.__init__(self, title="Socket Data to GTK Grid")
        self.set_default_size(400, 300)

        self.grid = Gtk.Grid()
        self.add(self.grid)

        self.labels = []
        self.entries = []
        self.threads = []

        # Read IP list from file
        with open(ip_list_file, 'r') as file:
            ip_list = file.read().splitlines()

        # Create UI elements and threads for each IP
        for i, ip in enumerate(ip_list):
            label = Gtk.Label(label=f"Data from Socket {i + 1} ({ip}):")
            self.labels.append(label)
            self.grid.attach(label, 0, i, 1, 1)

            entry = Gtk.Entry()
            self.entries.append(entry)
            self.grid.attach(entry, 1, i, 1, 1)

            thread = threading.Thread(target=self.update_data_from_socket, args=(i, ip))
            self.threads.append(thread)

        self.update_button = Gtk.Button(label="Update Grid")
        self.update_button.connect("clicked", self.on_update_button_clicked)
        self.grid.attach(self.update_button, 0, len(ip_list), 2, 1)

        # Start threads
        for thread in self.threads:
            thread.start()

        # Set up periodic update
        GObject.timeout_add_seconds(5, self.on_update_button_clicked)

    def on_update_button_clicked(self, widget=None):
        for i, thread in enumerate(self.threads):
            thread.join()  # Wait for thread to finish
            self.entries[i].set_text(self.threads[i].listener.data)

        return True

    def update_data_from_socket(self, index, ip):
        listener = SocketListener(ip, 12345)
        self.threads[index].listener = listener  # Attach the listener to the thread
        while True:
            listener.read_data()

    def on_destroy(self, widget):
        for thread in self.threads:
            thread.listener.close()
        Gtk.main_quit()

if __name__ == "__main__":
    win = MyGridWindow("ip_list.txt")
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()


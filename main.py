import tkinter as tk
from tkinter import filedialog
import requests
import os


class FileDownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Downloader")

        self.label = tk.Label(root, text="Выберите количество файлов для загрузки:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=10)

        self.button = tk.Button(root, text="Загрузить файлы", command=self.download_files)
        self.button.pack(pady=10)

    def download_files(self):
        try:
            count = int(self.entry.get())
        except ValueError:
            tk.messagebox.showerror("Ошибка", "Введите корректное число")
            return

        url = "https://jsonplaceholder.typicode.com/posts"
        response = requests.get(url)
        posts = response.json()

        for i in range(count):
            post = posts[i]
            filename = f"post_{post['id']}.json"
            with open(filename, 'w') as file:
                file.write(str(post))

        tk.messagebox.showinfo("Успех", f"{count} файлов были успешно загружены")


if __name__ == "__main__":
    root = tk.Tk()
    app = FileDownloaderApp(root)
    root.mainloop()

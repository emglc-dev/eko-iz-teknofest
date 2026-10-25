import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Yapılacaklar Listesi")
        self.root.geometry("400x500")
        self.root.config(bg="#f0f2f5")

        # Başlık Etiketi
        title_label = tk.Label(root, text="Günlük Planlayıcı", font=("Arial", 18, "bold"), bg="#f0f2f5", fg="#333")
        title_label.pack(pady=15)

        # Görev Giriş Alanı
        self.task_entry = tk.Entry(root, font=("Arial", 14), width=22, bd=2, relief="solid")
        self.task_entry.pack(pady=5)
        self.task_entry.bind("<Return>", lambda event: self.add_task()) # Enter tuşuna basınca ekler

        # Ekle Butonu
        add_button = tk.Button(root, text="Görev Ekle", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", width=18, command=self.add_task)
        add_button.pack(pady=10)

        # Görev Listesi ve Kaydırma Çubuğu
        frame = tk.Frame(root)
        frame.pack(pady=10)

        self.task_listbox = tk.Listbox(frame, font=("Arial", 12), width=28, height=12, bd=2, relief="solid", selectbackground="#d1e7dd")
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.task_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.task_listbox.yview)

        # Seçilen Görevi Sil Butonu
        delete_button = tk.Button(root, text="Seçilen Görevi Sil", font=("Arial", 12, "bold"), bg="#d9534f", fg="white", width=18, command=self.delete_task)
        delete_button.pack(pady=10)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task != "":
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Uyarı", "Lütfen boş bir görev girmeyin!")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_index)
        except IndexError:
            messagebox.showwarning("Uyarı", "Lütfen silmek için bir görev seçin!")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
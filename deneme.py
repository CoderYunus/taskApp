import tkinter as tk
from tkinter import messagebox






class GorevApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TaskApp")
        self.root.iconbitmap("icon.ico")  # Simgenin dosya yolu
        self.root.geometry("350x450")  # Pencere boyutunu ayarla

        self.to_do_list = []
        self.task_entry = tk.Text(self.root, width=30, height=3)  # Genişlik ve yüksekliği ayarla
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(self.root, text="Görev Ekle", command=self.add_task, width=20, height=3)
        self.add_button.pack(pady=10)

        self.show_button = tk.Button(self.root, text="Görevleri Göster", command=self.show_tasks, width=20, height=2)
        self.show_button.pack(pady=10)

        self.delete_button = tk.Button(self.root, text="Görev Sil", command=self.delete_task, width=20, height=2)
        self.delete_button.pack(pady=10)

        self.complete_button = tk.Button(self.root, text="Görevi Tamamla", command=self.complete_task, width=20, height=2)
        self.complete_button.pack(pady=10)

        self.complete_button = tk.Button(self.root, text="Tamamlanmış Görevleri\n Temizle", command=self.delete_completed_tasks, width=20, height=2)
        self.complete_button.pack(pady=10)

        self.exit_button = tk.Button(self.root, text="Çık", command=self.exit_app, width=5, height=1)
        self.exit_button.pack()

    def add_task(self):
        task = self.task_entry.get("1.0", tk.END)  # Tüm içeriği almak için "1.0" ile "end" aralığını kullanın
        if task.strip():
            self.to_do_list.append(task)
            self.task_entry.delete("1.0", tk.END)  # Girdiyi temizle
            messagebox.showinfo("Başarılı","Görev Başarıyla Eklendi")
        else :
            messagebox.showerror("Hata","Görev Zaten Ekli Veya Hatalı \n Lütfen Tekrar Deneyiniz ")
    def show_tasks(self):
        tasks_text = "\n".join(self.to_do_list)
        if tasks_text:
            messagebox.showinfo("Yapılacak Görevler \n", tasks_text)
        else:
            messagebox.showinfo("Yapılacak Görevler", "Görev yok.")

    def delete_task(self):
        task = self.task_entry.get("1.0", tk.END)  # Tüm içeriği almak için "1.0" ile "end" aralığını kullanın

        if task in self.to_do_list:
            self.to_do_list.remove(task)
            messagebox.showinfo("Başarılı", "Görev başarıyla silindi.")
        else:
            messagebox.showerror("Hata", "Görev bulunamadı.")
        self.task_entry.delete("1.0", tk.END)




    def complete_task(self):
        task = self.task_entry.get("1.0", tk.END)
        if task in self.to_do_list:
            completed_task = "Tamamlandı: " + task
            self.to_do_list.remove(task)
            self.to_do_list.insert(0, completed_task)
            messagebox.showinfo("Başarılı", "Görev başarıyla tamamlandı.")
        else:
            messagebox.showerror("Hata", "Görev bulunamadı.")
        self.task_entry.delete(0, tk.END)

    def delete_completed_tasks(self):
        completed_tasks = [task for task in self.to_do_list if task.startswith("Tamamlandı: ")]
        if completed_tasks: 
            for task in completed_tasks:
                self.to_do_list.remove(task)
            messagebox.showinfo("Başarılı", "Tamamlanmış görevler silindi.")
        else:
            messagebox.showinfo("Bilgi", "Tamamlanmış görev bulunmuyor.")



    def exit_app(self):

        self.root.quit()


if __name__ == "__main__":
    root = tk.Tk()
    app = GorevApp(root)
    root.mainloop()

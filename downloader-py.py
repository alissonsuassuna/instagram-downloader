import instaloader
import tkinter as tk
from tkinter import messagebox

def download_instagram_video():
    post_url = url_entry.get()

    if not post_url:
        messagebox.showwarning("Erro", "Por favor, insira a URL da postagem do Instagram.")
        return

    L = instaloader.Instaloader()
    shortcode = post_url.split("/")[-2]

    try:
        post = instaloader.Post.from_shortcode(L.context, shortcode)
        
        if post.is_video:
            L.download_post(post, target=f"downloads/{post.owner_username}")
            messagebox.showinfo("Sucesso", "O vídeo foi baixado com sucesso!")
        else:
            messagebox.showwarning("Aviso", "A postagem não contém um vídeo.")
    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao baixar o vídeo: {e}")

# Criar a interface gráfica
app = tk.Tk()
app.title("Downloader de Vídeos do Instagram")
app.geometry("400x200")

# Label de instrução
label = tk.Label(app, text="Insira a URL do vídeo do Instagram:", font=("Arial", 12))
label.pack(pady=10)

# Entrada de texto para a URL
url_entry = tk.Entry(app, width=50, font=("Arial", 12))
url_entry.pack(pady=10)

# Botão de download
download_button = tk.Button(app, text="Baixar Vídeo", command=download_instagram_video, font=("Arial", 12), bg="blue", fg="white")
download_button.pack(pady=10)

# Iniciar a aplicação
app.mainloop()

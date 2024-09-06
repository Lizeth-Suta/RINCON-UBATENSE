import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk  # Para usar el ComboBox

class EntreMontañasYLeyendas:
    def __init__(self, root):
        self.root = root
        self.root.title("Entre Montañas y Leyendas", )
        self.root.geometry("1024x680")

        # Cargar la imagen de fondo 
        self.bg_image = Image.open(r"C:\Users\USUARIO\OneDrive - UNIVERSIDAD DE CUNDINAMARCA\PROYECTO INTEGRADOR\fondo.jpeg")
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        # Crear un canvas para la imagen de fondo
        self.canvas = tk.Canvas(self.root, width=1024, height=768)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        # Título de la aplicación
        self.title_label = tk.Label(self.root, text="Entre Montañas y Leyendas", font=("Times Roman", 24, "bold"), bg="#D2691E", fg="white")
        self.title_label.place(relx=0.5, rely=0.1, anchor="center")
        
        # Botón de Municipio
        self.btn_municipio = tk.Button(self.root, text="Municipio", font=("Times New Roman", 14), bg="#4682B4", fg="white", command=self.municipio)
        self.btn_municipio.place(relx=0.3, rely=0.6, anchor="center")

        # Botón de Hospedaje
        self.btn_hospedaje = tk.Button(self.root, text="Reservación", font=("Times New Roman", 14), bg="#4682B4", fg="white", command=self.hospedaje)
        self.btn_hospedaje.place(relx=0.7, rely=0.6, anchor="center")

    def municipio(self):
        print("Navegando a la sección de Municipio")
    def abrir_municipio(self):
        # Crear una nueva ventana
        self.municipio_window = tk.Toplevel(self.root)
        self.municipio_window.title("Seleccionar Municipio")
        self.municipio_window.geometry("400x300")

        # Título en la nueva ventana
        label = tk.Label(self.municipio_window, text="Seleccione un Municipio", font=("Times New Roman", 16))
        label.pack(pady=10)

        # ComboBox para seleccionar el municipio
        municipios = ["Fuquene", "Susa", "Simijaca", "Guacheta"]
        self.combo_municipios = ttk.Combobox(self.municipio_window, values=municipios, font=("Times New Roman", 14))
        self.combo_municipios.pack(pady=10)

        # Botón para confirmar selección
        btn_confirmar = tk.Button(self.municipio_window, text="Confirmar", font=("Times New Roman", 14), command=self.mostrar_municipio)
        btn_confirmar.pack(pady=10)

    def mostrar_municipio(self):
        municipio_seleccionado = self.combo_municipios.get()
        if municipio_seleccionado:
            # Aquí puedes añadir más funciones, como mostrar información sobre el municipio seleccionado
            print(f"Has seleccionado: {municipio_seleccionado}")
            # Por ejemplo, podrías cerrar la ventana después de la selección
            self.municipio_window.destroy()

    def hospedaje(self):
        print("Navegando a la sección de Hospedaje")

if __name__ == "__main__":
    root = tk.Tk()
    app = EntreMontañasYLeyendas(root)
    root.mainloop()

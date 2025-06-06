#GAURAV MAHADU ROKADE
#task-02 CS Imagage encryption and decryption by pixel manipulation
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np

class ImageEncryptorDecryptor:
    def __init__(self, master):
        self.master = master
        master.title("Image Encryption and Decryption")

        # Image Panel
        self.panel = tk.Label(master)
        self.panel.pack()

        # Open Image Button
        self.btn_open = tk.Button(master, text="Open Image", command=self.open_image)
        self.btn_open.pack()

        # Key Entry
        tk.Label(master, text="Enter Key:").pack()
        self.entry_key = tk.Entry(master)
        self.entry_key.pack()

        # Encrypt and Decrypt Buttons
        self.btn_encrypt = tk.Button(master, text="Encrypt Image", command=self.encrypt_image)
        self.btn_encrypt.pack()

        self.btn_decrypt = tk.Button(master, text="Decrypt Image", command=self.decrypt_image)
        self.btn_decrypt.pack()

        # Save Image Button
        self.btn_save = tk.Button(master, text="Save Encrypted Image", command=self.save_image)
        self.btn_save.pack()

        # Initialize variables
        self.original_image = None
        self.encrypted_image = None

    def open_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            img = Image.open(file_path)
            img = img.resize((300, 300))  # Resize for display
            img_tk = ImageTk.PhotoImage(img)
            self.panel.config(image=img_tk)
            self.panel.image = img_tk
            self.original_image = np.array(img)

    def save_image(self):
        if self.encrypted_image is not None:
            save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                     filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
            if save_path:
                Image.fromarray(self.encrypted_image).save(save_path)
                messagebox.showinfo("Image Saved", "Encrypted image saved successfully!")
        else:
            messagebox.showwarning("No Image", "No image to save.")

    def encrypt_image(self):
        key = self.get_key()
        if key is not None and self.original_image is not None:
            self.encrypted_image = self.pixel_manipulation(self.original_image, key)
            self.display_image(self.encrypted_image)

    def decrypt_image(self):
        key = self.get_key()
        if key is not None and self.encrypted_image is not None:
            decrypted_img = self.pixel_manipulation(self.encrypted_image, key)
            self.display_image(decrypted_img)

    def get_key(self):
        try:
            key = int(self.entry_key.get())
            return key
        except ValueError:
            messagebox.showwarning("Invalid Key", "Please enter a valid integer key.")
            return None

    def pixel_manipulation(self, image_array, key):
        return image_array ^ key

    def display_image(self, image_array):
        img = Image.fromarray(image_array)
        img = img.resize((300, 300))  # Resize for display
        img_tk = ImageTk.PhotoImage(img)
        self.panel.config(image=img_tk)
        self.panel.image = img_tk

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEncryptorDecryptor(root)
    root.mainloop()

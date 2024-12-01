import customtkinter as ctk

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Main App")
        self.geometry("400x400")
        
        # Some variable in the main app
        self.my_variable = "Hello from MainApp"
        
        # Button that opens a new Toplevel window
        self.open_toplevel_button = ctk.CTkButton(self, text="Open Toplevel", command=self.open_toplevel)
        self.open_toplevel_button.pack(pady=20)
    
    def open_toplevel(self):
        # Pass the main app variable to Toplevel
        toplevel_window = ToplevelWindow(self, self.my_variable)
        toplevel_window.grab_set()  # Optional: makes the toplevel window modal

class ToplevelWindow(ctk.CTkToplevel):
    def __init__(self, variable):
        super().__init__()
        
        self.title("Toplevel Window")
        self.geometry("300x300")
        
        # Use the passed variable
        self.label = ctk.CTkLabel(self, text=f"Received: {variable}")
        self.label.pack(pady=20)

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()

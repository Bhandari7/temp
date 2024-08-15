import subprocess
import tkinter as tk
from tkinter import scrolledtext


# Function to run 'ollama codelama' command
def run_codelama():
    try:
        # Call subprocess to run ollama codelama with a configuration file
        output = subprocess.check_output("C:/Users/vijay/AppData/Local/Programs/Ollama/ollama run codellama 'why do you think you are smart?'")
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, output.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        print('-----------------------------', e)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"-------------------------------Error: {e}")

# Tkinter GUI setup
root = tk.Tk()
root.title("Ollama CodeLlama Runner")

# Button to trigger the subprocess call
run_button = tk.Button(root, text="Run CodeLlama", command=run_codelama)
run_button.pack(pady=10)

# ScrolledText to display the output
result_text = scrolledtext.ScrolledText(root, width=60, height=20)
result_text.pack(padx=10, pady=10)


# Run the Tkinter loop
root.mainloop()

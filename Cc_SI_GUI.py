import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import joblib
import numpy as np

# Load the pre-trained models
def load_model():
    try:
        cc_model = joblib.load("./results/models/Cc_Random Forest_best.pkl")
        si_model = joblib.load("./results/models/SI_Random Forest_best.pkl")
        return cc_model, si_model
    except Exception as e:
        messagebox.showerror("Error", f"Error loading models: {e}")
        return None, None

# Calculate Plasticity Index (PI)
def calculate_pi():
    try:
        ll = entry_widgets["Liquid Limit (LL)"].get()
        pl = entry_widgets["Plastic Limit (PL)"].get()

        if ll and pl:
            ll = float(ll)
            pl = float(pl)
            pi = ll - pl

            if pi < 0:
                pi_label.config(text="Invalid")
                messagebox.showerror("Input Error", "Plasticity Index (PI) cannot be negative.")
                return None
            else:
                pi_label.config(text=f"{pi:.2f}")
                return pi
        else:
            pi_label.config(text="N/A")
            return None
    except ValueError:
        pi_label.config(text="Invalid")
        return None

# Predict Cc and SI
def predict_results():
    try:
        cc_model, si_model = load_model()
        if cc_model is None or si_model is None:
            return

        # Collect inputs
        inputs = []
        for label, entry in entry_widgets.items():
            value = entry.get()
            if not value.strip():
                messagebox.showerror("Input Error", f"Please fill in the {label}.")
                return
            inputs.append(float(value))

        # Calculate Plasticity Index (PI)
        pi = calculate_pi()
        if pi is None:
            return
        inputs.append(pi)  # Add PI to the input array

        # Reshape inputs for model prediction
        inputs = np.array(inputs).reshape(1, -1)

        # Make predictions
        cc_prediction = cc_model.predict(inputs)
        si_prediction = si_model.predict(inputs)

        # Display results
        result_label.config(
            text=(f"Predicted Compression Index (Cc): {cc_prediction[0]:.4f}\n"
                  f"Predicted Swelling Index (SI): {si_prediction[0]:.4f}")
        )
    except Exception as e:
        messagebox.showerror("Prediction Error", f"Error during prediction: {e}")

# Copy all entries and results
def copy_all():
    try:
        inputs = [f"{field}: {entry.get()}" for field, entry in entry_widgets.items()]
        pi_text = f"Plasticity Index (PI): {pi_label.cget('text')}"
        results = result_label.cget("text")
        clipboard_content = "\n".join(inputs + [pi_text, "\nResults:\n" + results])
        root.clipboard_clear()
        root.clipboard_append(clipboard_content)
        messagebox.showinfo("Copied", "All inputs and results copied to clipboard!")
    except Exception as e:
        messagebox.showerror("Error", f"Error copying data: {e}")

# About the application
def about_application():
    messagebox.showinfo(
        "About This Application",
        "This application predicts the Compression Index (Cc) and Swelling Index (SI) "
        "based on soil parameters. Designed and developed by Rod Will.",
    )

# How to use the application
def how_to_use():
    messagebox.showinfo(
        "How to Use",
        "1. Enter the initial void ratio (eo), natural water content (wn), Liquid Limit (LL), "
        "and Plastic Limit (PL).\n"
        "2. The Plasticity Index (PI) will be calculated automatically.\n"
        "3. Click 'Predict Cc & SI' to get results.\n"
        "4. Use the 'Copy All' button to save the inputs and results.",
    )

# Create the GUI window
root = tk.Tk()

# Set the application icon
ico = Image.open('logo.png')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)

root.title("Cc and SI Prediction Application")
root.geometry("600x750")
root.configure(bg="#f4f1de")

# Add logo at the top
try:
    logo_path = "Presentation2.png"
    logo = Image.open(logo_path).resize((500, 120), Image.Resampling.LANCZOS)
    logo_img = ImageTk.PhotoImage(logo)
    tk.Label(root, image=logo_img, bg="#f4f1de").pack(pady=10)
except Exception:
    tk.Label(root, text="Logo not available.", fg="red", bg="#f4f1de").pack()

# Top buttons
top_frame = tk.Frame(root, bg="#f4f1de")
top_frame.pack(pady=10, fill="x")
tk.Button(top_frame, text="About", command=about_application, bg="#e07a5f", fg="white", font=("Arial", 10, "bold")).pack(side="left", padx=20)
tk.Button(top_frame, text="How to Use", command=how_to_use, bg="#3d405b", fg="white", font=("Arial", 10, "bold")).pack(side="left", padx=20)

# Input frame
input_frame = tk.Frame(root, bg="#f4f1de", bd=2, relief="groove")
input_frame.pack(pady=20, padx=20, fill="both", expand=True)
fields_dict = {
    "Initial Void Ratio (eo)": "Initial void ratio of the soil",
    "Natural Water Content (wn)": "Natural water content of the soil (%)",
    "Liquid Limit (LL)": "Liquid Limit of the soil (%)",
    "Plastic Limit (PL)": "Plastic Limit of the soil (%)",
}
entry_widgets = {}
for i, (label_text, desc_text) in enumerate(fields_dict.items()):
    tk.Label(input_frame, text=label_text, anchor="w", bg="#f4f1de", font=("Arial", 10, "bold")).grid(row=i * 2, column=0, padx=10, pady=5, sticky="w")
    tk.Label(input_frame, text=desc_text, anchor="w", bg="#f4f1de", fg="#8d99ae", font=("Arial", 9, "italic")).grid(row=i * 2 + 1, column=0, padx=10, pady=2, sticky="w")
    entry = tk.Entry(input_frame, bg="white", fg="black", font=("Arial", 10))
    entry.grid(row=i * 2, column=1, padx=10, pady=5, sticky="ew")
    entry_widgets[label_text] = entry

input_frame.columnconfigure(1, weight=1)

# Plasticity Index (PI) display
pi_frame = tk.Frame(root, bg="#f4f1de", bd=2, relief="groove")
pi_frame.pack(pady=10, padx=20, fill="x")
tk.Label(pi_frame, text="Plasticity Index (PI):", font=("Arial", 12, "bold"), bg="#f4f1de").pack(side="left", padx=10)
pi_label = tk.Label(pi_frame, text="N/A", font=("Arial", 12, "bold"), bg="#f4f1de", fg="#3d405b")
pi_label.pack(side="left", padx=5)

# Buttons
btn_frame = tk.Frame(root, bg="#f4f1de")
btn_frame.pack(pady=20)
tk.Button(btn_frame, text="Predict Cc & SI", command=predict_results, bg="#81b29a", fg="white", font=("Arial", 12, "bold"), width=15).pack(side="left", padx=20)
tk.Button(btn_frame, text="Copy All", command=copy_all, bg="#f2cc8f", fg="white", font=("Arial", 12, "bold"), width=15).pack(side="left", padx=20)

# Results
result_frame = tk.Frame(root, bg="#f4f1de", bd=2, relief="groove")
result_frame.pack(pady=20, padx=20, fill="x")
tk.Label(result_frame, text="Results:", font=("Arial", 12, "bold"), bg="#f4f1de").pack(anchor="w", padx=10, pady=5)
result_label = tk.Label(result_frame, text="", font=("Arial", 12), bg="#f4f1de", fg="#3d405b")
result_label.pack(pady=5, padx=10)

# Footer
footer = tk.Label(root, text="Developed by Rod Will", font=("Arial", 10, "italic"), bg="#f4f1de", fg="#8d99ae")
footer.pack(side="bottom", pady=10)

# Bind LL and PL changes to update PI dynamically
entry_widgets["Liquid Limit (LL)"].bind("<KeyRelease>", lambda event: calculate_pi())
entry_widgets["Plastic Limit (PL)"].bind("<KeyRelease>", lambda event: calculate_pi())

# Run the application
root.mainloop()

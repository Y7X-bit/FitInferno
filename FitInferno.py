import customtkinter as ctk
import tkinter.messagebox as mb

# AMOLED + HOT RED Theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

def get_advice(w, h_cm, g):
    try:
        w = float(w)
        h = float(h_cm) / 100
        g = g.lower()

        bmi = round(w / (h ** 2), 2)
        if bmi < 18.5:
            status = "Underweight"
        elif 18.5 <= bmi <= 24.9:
            status = "Normal"
        elif 25 <= bmi <= 29.9:
            status = "Overweight"
        else:
            status = "Obese"

        if g == "lose weight":
            workout = "🏃‍♂️ 30–45 min cardio + strength 5x/week."
            diet = "🥗 High protein, low carbs, calorie deficit."
        elif g == "gain muscle":
            workout = "🏋️ Heavy lifting 4–5x/week (squats, deadlifts)."
            diet = "🍗 High protein (1.6–2g/kg), calorie surplus."
        elif g == "stay fit":
            workout = "🧘‍♀️ Mix of strength, yoga & cardio weekly."
            diet = "🍎 Balanced diet: fruits, veggies, protein."
        else:
            workout = "🤸‍♀️ 3–4x/week light workouts + stretching."
            diet = "🥦 Avoid junk, eat clean, hydrate well."

        return f"📊 BMI: {bmi} ({status})\n\n🏋️ Workout:\n{workout}\n\n🥗 Diet:\n{diet}"
    except:
        return "⚠️ Please enter valid numbers."

def calculate():
    weight = entry_weight.get()
    height = entry_height.get()
    goal = combo_goal.get()

    if not weight or not height or not goal:
        mb.showwarning("Input Error", "Please fill all fields.")
        return

    result = get_advice(weight, height, goal)
    result_label.configure(text=result)

# --- GUI ---
app = ctk.CTk()
app.title("🔥 FitInferno")
app.geometry("520x400")
app.resizable(False, False)
app.configure(fg_color="#000000")  # AMOLED pitch black

# Colors
MAIN_RED = "#FF0000"
WHITE = "#FFFFFF"

# Title
ctk.CTkLabel(app, text="🔥 FitInferno", font=("Segoe UI", 26, "bold"), text_color=MAIN_RED).pack(pady=(25, 15))

# Input Frame - pure black
frame = ctk.CTkFrame(app, width=460, height=180, corner_radius=10, fg_color="#000000")
frame.pack(pady=(0, 10))
frame.pack_propagate(False)
frame.grid_columnconfigure((0, 1), weight=1)

label_font = ("Segoe UI", 14)

# Weight
ctk.CTkLabel(frame, text="Weight (kg):", font=label_font, text_color=MAIN_RED).grid(row=0, column=0, padx=15, pady=10, sticky="e")
entry_weight = ctk.CTkEntry(frame, width=180, fg_color="#000000", text_color=MAIN_RED, border_color=MAIN_RED)
entry_weight.grid(row=0, column=1, padx=15, pady=10, sticky="w")

# Height
ctk.CTkLabel(frame, text="Height (cm):", font=label_font, text_color=MAIN_RED).grid(row=1, column=0, padx=15, pady=10, sticky="e")
entry_height = ctk.CTkEntry(frame, width=180, fg_color="#000000", text_color=MAIN_RED, border_color=MAIN_RED)
entry_height.grid(row=1, column=1, padx=15, pady=10, sticky="w")

# Goal
ctk.CTkLabel(frame, text="Fitness Goal:", font=label_font, text_color=MAIN_RED).grid(row=2, column=0, padx=15, pady=10, sticky="e")
combo_goal = ctk.CTkComboBox(frame, values=["Lose Weight", "Gain Muscle", "Stay Fit", "Other"],
                             width=180, fg_color="#000000", text_color=MAIN_RED, border_color=MAIN_RED,
                             button_color="#000000", button_hover_color="#111111")
combo_goal.grid(row=2, column=1, padx=15, pady=10, sticky="w")

# Red Outline Button with White Text (No Fill)
glow_btn = ctk.CTkButton(
    app,
    text="🎯 Generate Plan",
    command=calculate,
    font=("Segoe UI", 17, "bold"),
    width=240,
    height=50,
    fg_color="transparent",       # No fill
    border_width=2,
    border_color=MAIN_RED,
    text_color=WHITE,
    hover_color="#1a1a1a",
    corner_radius=25,
)
glow_btn.pack(pady=(10, 15))

# Output in red
result_label = ctk.CTkLabel(app, text="", font=("Segoe UI", 15), wraplength=480, justify="left", text_color=MAIN_RED)
result_label.pack(pady=(5, 10))

app.mainloop()
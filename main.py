import customtkinter as ctk
import tkinter.messagebox as mb

# Theme
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

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
            workout = "🏃‍♂️ Cardio 30–45min 5x/week + light strength."
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
app.title("💪 AI Fitness & Diet Advisor")
app.geometry("520x560")
app.resizable(False, False)

# Title
ctk.CTkLabel(app, text="💪 AI Fitness & Diet Advisor", font=("Segoe UI", 26, "bold")).pack(pady=(25, 15))

# Input Frame
frame = ctk.CTkFrame(app, width=460, height=180, corner_radius=10)
frame.pack(pady=(0, 10))
frame.pack_propagate(False)
frame.grid_columnconfigure((0, 1), weight=1)

label_font = ("Segoe UI", 14)

ctk.CTkLabel(frame, text="Weight (kg):", font=label_font).grid(row=0, column=0, padx=15, pady=10, sticky="e")
entry_weight = ctk.CTkEntry(frame, width=180)
entry_weight.grid(row=0, column=1, padx=15, pady=10, sticky="w")

ctk.CTkLabel(frame, text="Height (cm):", font=label_font).grid(row=1, column=0, padx=15, pady=10, sticky="e")
entry_height = ctk.CTkEntry(frame, width=180)
entry_height.grid(row=1, column=1, padx=15, pady=10, sticky="w")

ctk.CTkLabel(frame, text="Fitness Goal:", font=label_font).grid(row=2, column=0, padx=15, pady=10, sticky="e")
combo_goal = ctk.CTkComboBox(frame, values=["Lose Weight", "Gain Muscle", "Stay Fit", "Other"], width=180)
combo_goal.grid(row=2, column=1, padx=15, pady=10, sticky="w")

# Glow-Effect Button Styling
glow_btn = ctk.CTkButton(
    app,
    text="🎯 Generate Plan",
    command=calculate,
    font=("Segoe UI", 17, "bold"),
    width=240,
    height=50,
    fg_color="#00FFAA",           # neon teal
    hover_color="#66FFCC",        # brighter hover effect
    text_color="black",
    corner_radius=25,
)
glow_btn.pack(pady=(10, 15))

# Output
result_label = ctk.CTkLabel(app, text="", font=("Segoe UI", 15), wraplength=480, justify="left")
result_label.pack(pady=(5, 10))

def pulse_button():
    current_color = glow_btn.cget("fg_color")
    next_color = "#00FFAA" if current_color == "#66FFCC" else "#66FFCC"
    glow_btn.configure(fg_color=next_color)
    app.after(700, pulse_button)

pulse_button()

app.mainloop()
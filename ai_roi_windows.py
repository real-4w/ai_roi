import tkinter as tk
from tkinter import messagebox

class ROICalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("AI/Automation ROI Calculator")
        self.root.geometry("400x500")

        # Create and place input labels and entries
        tk.Label(root, text="Hourly Rate ($):").pack(pady=10)
        self.hourly_rate_entry = tk.Entry(root)
        self.hourly_rate_entry.pack()

        tk.Label(root, text="Time Required for Task (hours):").pack(pady=10)
        self.time_required_entry = tk.Entry(root)
        self.time_required_entry.pack()

        tk.Label(root, text="Time Saved by AI (%):").pack(pady=10)
        self.time_saved_entry = tk.Entry(root)
        self.time_saved_entry.pack()

        # Calculate button
        tk.Button(root, text="Calculate ROI", command=self.calculate_roi).pack(pady=20)

        # Results display
        self.result_label = tk.Label(root, text="", wraplength=350, justify="left")
        self.result_label.pack(pady=10)

    def calculate_roi(self):
        try:
            hourly_rate = float(self.hourly_rate_entry.get())
            time_required = float(self.time_required_entry.get())
            time_saved_percent = float(self.time_saved_entry.get())

            # Validate inputs
            if hourly_rate < 0 or time_required < 0 or time_saved_percent < 0 or time_saved_percent > 100:
                messagebox.showerror("Error", "Please enter valid positive numbers (time saved % should be 0-100).")
                return

            # Calculate cost without AI
            cost_without_ai = hourly_rate * time_required

            # Calculate time and cost with AI
            time_saved = time_required * (time_saved_percent / 100)
            time_with_ai = time_required - time_saved
            cost_with_ai = hourly_rate * time_with_ai

            # Calculate savings and ROI
            savings = cost_without_ai - cost_with_ai
            roi_percentage = (savings / cost_without_ai) * 100 if cost_without_ai > 0 else 0

            # Display results
            result_text = (
                f"Results:\n"
                f"Original Task Cost: ${cost_without_ai:.2f}\n"
                f"Cost with AI: ${cost_with_ai:.2f}\n"
                f"Savings: ${savings:.2f}\n"
                f"Time Saved: {time_saved:.2f} hours\n"
                f"ROI: {roi_percentage:.2f}%"
            )
            self.result_label.config(text=result_text)

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numerical values.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ROICalculator(root)
    root.mainloop()
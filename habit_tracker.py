habits = [("Drink water", True), ("Read 10 pages", False),
          ("Exercise", True), ("Sleep 8 hours", True)]
habits = [("Drink water", True), ("Read 10 pages", False),
          ("Exercise", True), ("Sleep 8 hours", True),
          ("Meditate", False)]

for name, completed in habits:
    status = "Done" if completed else "Not done"
    print(f"{name}: {status}")

def habit_report(habits):
    completed = sum(1 for _, done in habits if done)
    return {"completed": completed, "total": len(habits)}

print(habit_report(habits))
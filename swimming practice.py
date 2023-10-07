
import pandas as pd


# Define the swim training program
training_program = {
    "Week 1": {
        "Day": ["Monday", "Wednesday", "Saturday"],
        "Workout": [
            "Warm-up: 200m easy swim | Main set: 4x50m freestyle (rest 20 sec between each) | Cool-down: 200m easy swim",
            "Warm-up: 200m easy swim | Main set: 4x100m freestyle (rest 30 sec between each) | Cool-down: 200m easy swim",
            "Warm-up: 200m easy swim | Main set: 4x150m freestyle (rest 45 sec between each) | Cool-down: 200m easy swim"
        ]
    },
    "Week 2": {
        "Day": ["Monday", "Wednesday", "Saturday"],
        "Workout": [
            "Warm-up: 200m easy swim | Main set: 6x50m freestyle (rest 20 sec between each) | Cool-down: 200m easy swim",
            "Warm-up: 200m easy swim | Main set: 6x100m freestyle (rest 30 sec between each) | Cool-down: 200m easy swim",
            "Warm-up: 200m easy swim | Main set: 6x150m freestyle (rest 45 sec between each) | Cool-down: 200m easy swim"
        ]
    },
    # Add the remaining weeks of the training program
    "Week 3": {
        "Day": ["Monday", "Wednesday", "Saturday"],
        "Workout": [
            "Warm-up: 200m easy swim | Main set: 8x50m freestyle (rest 20 sec between each) | Cool-down: 200m easy swim",
            "Warm-up: 200m easy swim | Main set: 8x100m freestyle (rest 30 sec between each) | Cool-down: 200m easy swim",
            "Warm-up: 200m easy swim | Main set: 8x150m freestyle (rest 45 sec between each) | Cool-down: 200m easy swim"
        ]
    },
    "Week 4": {
        "Day": ["Monday", "Wednesday", "Saturday"],
        "Workout": [
            "Warm-up: 200m easy swim | Main set: 10x50m freestyle (rest 20 sec between each) | Cool-down: 200m easy swim",
            "Warm-up: 200m easy swim | Main set: 10x100m freestyle (rest 30 sec between each) | Cool-down: 200m easy swim",
            "Warm-up: 200m easy swim | Main set: 10x150m freestyle (rest 45 sec between each) | Cool-down: 200m easy swim"
        ]
    },
    "Week 5": {
        "Day": ["Monday", "Wednesday", "Saturday"],
        "Workout": [
            "Warm-up: 200m easy swim | Main set: 12x50m freestyle (rest 20 sec between each) | Cool-down: 200m easy swim",
            "Warm-up: 200m easy swim | Main set: 12x100m freestyle (rest 30 sec between each) | Cool-down: 200m easy swim",
            "Warm-up: 200m easy swim | Main set: 12x150m freestyle (rest 45 sec between each) | Cool-down: 200m easy swim"
        ]
    },
    "Week 6": {
        "Day": ["Monday", "Wednesday", "Saturday"],
        "Workout": [
            "Warm-up: 200m easy swim | Main set: 14x50m freestyle (rest 20 sec between each) | Cool-down: 200m easy swim",
            "Warm-up: 200m easy swim | Main set: 14x100m freestyle (rest 30 sec between each) | Cool-down: 200m easy swim",
            "Warm-up: 200m easy swim | Main set: 14x150m freestyle (rest 45 sec between each) | Cool-down: 200m easy swim"
        ]
    },
    "Week 7": {
        "Day": ["Monday", "Wednesday", "Saturday"],
        "Workout": [
            "Warm-up: 200m easy swim | Main set: 16x50m freestyle (rest 20 sec between each) | Cool-down: 200m easy swim",
            "Warm-up: 200m easy swim | Main set: 16x100m freestyle (rest 30 sec between each) | Cool-down: 200m easy swim",
            "Warm-up: 200m easy swim | Main set: 16x150m freestyle (rest 45 sec between each) | Cool-down: 200m easy swim"
        ]
    },
    "Week 8": {
        "Day": ["Monday", "Wednesday", "Saturday"],
        "Workout": [
            "Warm-up: 200m easy swim | Main set: 18x50m freestyle (rest 20 sec between each) | Cool-down: 200m easy swim",
            "Warm-up: 200m easy swim | Main set: 18x100m freestyle (rest 30 sec between each) | Cool-down: 200m easy swim",
            "Warm-up: 200m easy swim | Main set: 18x150m freestyle (rest 45 sec between each) | Cool-down: 200m easy swim"
        ]
    },
    "Week 9": {
        "Day": ["Monday", "Wednesday", "Saturday"],
        "Workout": [
            "Warm-up: 200m easy swim | Main set: 20x50m freestyle (rest 20 sec between each) | Cool-down: 200m easy swim",
            "Warm-up: 200m easy swim | Main set: 20x100m freestyle (rest 30 sec between each) | Cool-down: 200m easy swim",
            "Warm-up: 200m easy swim | Main set: 20x150m freestyle (rest 45 sec between each) | Cool-down: 200m easy swim"
        ]
    },
    "Week 10": {
        "Day": ["Monday", "Wednesday", "Saturday"],
        "Workout": [
            "Warm-up: 200m easy swim | Main set: 22x50m freestyle (rest 20 sec between each) | Cool-down: 200m easy swim",
            "Warm-up: 200m easy swim | Main set: 22x100m freestyle (rest 30 sec between each) | Cool-down: 200m easy swim",
            "Warm-up: 200m easy swim | Main set: 22x150m freestyle (rest 45 sec between each) | Cool-down: 200m easy swim"
        ]
    },
    "Week 11": {
        "Day": ["Monday", "Wednesday", "Saturday"],
        "Workout": [
            "Warm-up: 200m easy swim | Main set: 24x50m freestyle (rest 20 sec between each) | Cool-down: 200m easy swim",
            "Warm-up: 200m easy swim | Main set: 24x100m freestyle (rest 30 sec between each) | Cool-down: 200m easy swim",
            "Warm-up: 200m easy swim | Main set: 24x150m freestyle (rest 45 sec between each) | Cool-down: 200m easy swim"
        ]
    },
    "Week 12": {
        "Day": ["Monday", "Wednesday", "Saturday"],
        "Workout": [
            "Warm-up: 200m easy swim | Main set: 26x50m freestyle (rest 20 sec between each) | Cool-down: 200m easy swim",
            "Warm-up: 200m easy swim | Main set: 26x100m freestyle (rest 30 sec between each) | Cool-down: 200m easy swim",
            "Warm-up: 200m easy swim | Main set: 26x150m freestyle (rest 45 sec between each) | Cool-down: 200m easy swim"
        ]
    }
}

# Create a new dictionary to store the modified training program
modified_training_program = {}

# Iterate over each week and modify the main set of workouts
for week, workouts in training_program.items():
    modified_workouts = []
    for workout in workouts["Workout"]:
        parts = workout.split("|")
        main_set = parts[1].strip()
        modified_main_set = main_set + " + " + str(len(parts[1].split("x")) * 2) + " extra reps"
        modified_workout = parts[0] + " | " + modified_main_set + " | " + parts[2]
        modified_workouts.append(modified_workout)
    
    modified_training_program[week] = {
        "Day": workouts["Day"],
        "Workout": modified_workouts
    }

# Create a list to store the rows for the Excel file
rows = []

# Iterate over each week and add the data to the rows list
for week, workouts in modified_training_program.items():
    # Add an empty row before each week's data
    rows.append(["", "", ""])
    
    # Add the week's data
    rows.append(["Week", "Day", "Workout"])
    for day, workout in zip(workouts["Day"], workouts["Workout"]):
        rows.append([week, day, workout])

# Create a Pandas DataFrame from the rows data
df = pd.DataFrame(rows)

# Create an Excel writer object
writer = pd.ExcelWriter('swim_training_program_modified.xlsx', engine='xlsxwriter')

# Write the DataFrame to the Excel file
df.to_excel(writer, index=False, header=False)

# Set column widths
worksheet = writer.sheets['Sheet1']
worksheet.set_column('A:A', 15)
worksheet.set_column('B:B', 15)
worksheet.set_column('C:C', 70)

# Save the Excel file
writer._save()
print("")
print("Excel file 'swim_training_program_modified.xlsx' has been generated.")
print("")
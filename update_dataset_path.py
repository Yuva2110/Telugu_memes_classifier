import json
import os

# Load your JSON file
with open("/Telugu_memes_classifier/Dataset/final_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Set your current image directory path
new_base_path = "/Telugu_memes_classifier/Dataset/images"

# Update image paths
for entry in data:
    img_filename = os.path.basename(entry["img"])
    entry["img"] = os.path.join(new_base_path, img_filename)

# Save updated JSON
with open("Final_updated_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("Image paths updated and saved to updated_data.json")

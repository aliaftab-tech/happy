import os
from PIL import Image

frames_dir = r"d:\happy birthday\video_frames"
out_dir = r"d:\happy birthday\website_assets"
os.makedirs(out_dir, exist_ok=True)

# Helper function to crop and save
def crop_box(frame_num, box, filename):
    img_path = os.path.join(frames_dir, f"frame_{frame_num:03d}.jpg")
    if not os.path.exists(img_path):
        print(f"Missing {img_path}")
        return
    img = Image.open(img_path)
    cropped = img.crop(box)
    cropped.save(os.path.join(out_dir, filename), quality=95)
    print(f"Saved {filename}")

# Frame resolution is 720x1280

# 1. Screen 0 Gift Box (frame 3)
# Centered around y: 350 to 720, x: 150 to 570
crop_box(3, (160, 350, 560, 710), "intro_gift_box.png")

# 2. Screen 1 Cats (Peach & Goma) (frame 6)
# Centered around y: 400 to 650, x: 180 to 540
crop_box(6, (180, 410, 540, 645), "cats_hug.png")

# 3. Screen 1 Reject Panda & Bear (frame 9)
# y: 420 to 630, x: 160 to 560
crop_box(9, (160, 425, 560, 625), "panda_gun_bear.png")

# 4. Screen 2 Hub Icons (frame 16)
# 4 rounded cards:
# Top-Left: Cake
crop_box(16, (140, 440, 425, 595), "hub_card_cake.png")
# Top-Right: Camera
crop_box(16, (610, 440, 895, 595) if False else (440, 440, 720, 595), "hub_card_camera.png")
# Let's get exact coordinates for the 4 cards:
# Card 1 (TL): x: 140 to 425, y: 440 to 590
# Card 2 (TR): x: 610 is offscreen? Wait, frame is 720 wide!
# Let's inspect x coordinates for 4 cards in 720px width:
# Left cards: x: 100 to 310, Right cards: x: 410 to 620
# Let's do a more precise crop test!

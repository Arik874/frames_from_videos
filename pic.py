import cv2
import os

# Path to the input 4K video file
video_path = 'vdo.MOV'

# Directory to save the extracted frames
output_dir = 'photu'

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Open the video file
cap = cv2.VideoCapture(video_path)

# Initialize frame count
count = 0

# Read until video is completed
while True:
    # Read a frame from the video
    ret, frame = cap.read()
    
    # Break the loop if no more frames are returned
    if not ret:
        break
    
    # Save the frame as an image
    output_file = os.path.join(output_dir, f"frame_{count:04d}.jpg")
    cv2.imwrite(output_file, frame)
    
    # Increment the frame count
    count += 1

    # Display the frame every 100 frames (optional)
    if count % 100 == 0:
        cv2.imshow('Frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release the video capture object and close the window (if open)
cap.release()
cv2.destroyAllWindows()

print(f"Extracted {count} frames and saved them in {output_dir}")

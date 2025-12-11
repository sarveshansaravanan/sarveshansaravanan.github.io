from PIL import Image
import os

def resize_images(media_folder, min_width=800, target_width=300):
    """
    Resize small images in the media folder.
    
    Args:
        media_folder: Path to the media folder
        min_width: Images smaller than this will be resized (default 800px)
        target_width: Target width for resized images (default 1200px)
    """
    
    # Get all image files
    image_extensions = {'.png', '.jpg', '.jpeg', '.gif', '.bmp'}
    
    for filename in os.listdir(media_folder):
        file_path = os.path.join(media_folder, filename)
        
        # Skip if not a file or already a resized version
        if not os.path.isfile(file_path) or '_resized' in filename:
            continue
        
        # Check if it's an image file
        ext = os.path.splitext(filename)[1].lower()
        if ext not in image_extensions:
            continue
        
        try:
            # Open the image
            with Image.open(file_path) as img:
                width, height = img.size
                
                # Check if image is smaller than minimum width
                if width < min_width:
                    print(f"Resizing {filename} (current: {width}x{height})")
                    
                    # Calculate new height to maintain aspect ratio
                    aspect_ratio = height / width
                    new_height = int(target_width * aspect_ratio)
                    
                    # Resize the image
                    resized_img = img.resize((target_width, new_height), Image.LANCZOS)
                    
                    # Create new filename with _resized suffix
                    name_without_ext = os.path.splitext(filename)[0]
                    new_filename = f"{name_without_ext}_resized{ext}"
                    new_path = os.path.join(media_folder, new_filename)
                    
                    # Save the resized image
                    resized_img.save(new_path, quality=95)
                    print(f"  → Saved as {new_filename} ({target_width}x{new_height})")
                else:
                    print(f"Skipping {filename} (already large: {width}x{height})")
        
        except Exception as e:
            print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    # Change this to your media folder path
    media_folder = "leftover"
    
    print("Starting image resize process...")
    print(f"Looking for images smaller than 800px in: {media_folder}\n")
    
    resize_images(media_folder, min_width=800, target_width=300)
    
    print("\nDone!")
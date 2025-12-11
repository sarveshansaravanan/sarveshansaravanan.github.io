from PIL import Image
import os

def replace_resized_images(media_folder, target_width=300):
    """
    Replace all _resized images with new versions at target_width.
    This is a one-for-one replacement - deletes old _resized and creates new one.
    
    Args:
        media_folder: Path to the media folder
        target_width: Target width for resized images (default 300px)
    """
    
    # Get all image files
    image_extensions = {'.png', '.jpg', '.jpeg', '.gif', '.bmp'}
    
    for filename in os.listdir(media_folder):
        # Only process _resized files
        if '_resized' not in filename:
            continue
            
        file_path = os.path.join(media_folder, filename)
        
        # Skip if not a file
        if not os.path.isfile(file_path):
            continue
        
        # Check if it's an image file
        ext = os.path.splitext(filename)[1].lower()
        if ext not in image_extensions:
            continue
        
        # Find the original file (without _resized suffix)
        name_without_ext = os.path.splitext(filename)[0]
        original_name = name_without_ext.replace('_resized', '')
        original_filename = f"{original_name}{ext}"
        original_path = os.path.join(media_folder, original_filename)
        

        try:
            # Open the original image
            with Image.open(original_path) as img:
                width, height = img.size
                print(f"Processing {original_filename} (current: {width}x{height})")
                
                # Calculate new height to maintain aspect ratio
                aspect_ratio = height / width
                new_height = int(target_width * aspect_ratio)
                
                # Resize the image
                resized_img = img.resize((target_width, new_height), Image.LANCZOS)
                
                # Delete the old _resized file
                print(f"  → Deleting old {filename}")
                os.remove(file_path)
                
                # Save the new resized image with same filename
                resized_img.save(file_path, quality=95)
                print(f"  → Created new {filename} ({target_width}x{new_height})")
        
        except Exception as e:
            print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    # Change this to your media folder path
    media_folder = "leftover"
    
    print("Starting image replacement process...")
    print(f"Replacing all _resized images with 300px width versions in: {media_folder}\n")
    
    replace_resized_images(media_folder, target_width=300)
    
    print("\nDone! All _resized images have been replaced with 300px versions.")
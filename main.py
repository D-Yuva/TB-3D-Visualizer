from src.preprocess import load_images, apply_mask, save_masked_image, generate_mask_from_image
from src.extrusion_3d import extrude_2d_to_3d
from src.visualize import show_3d_volume
import os

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_dir, "data")

    image_path = os.path.join(data_path, "/Users/yuva/development/3D/data/xray.jpeg")
    mask_path = os.path.join(data_path, "tb_mask.png")
    output_path = os.path.join(data_path, "masked_result.png")

    # Check if mask exists; if not, create one
    if not os.path.exists(mask_path):
        print("[INFO] Mask not found. Generating a simple mask...")
        generate_mask_from_image(image_path, mask_path)

    # Save masked image
    save_masked_image(image_path, mask_path, output_path)

    # Load and process
    image, mask = load_images(image_path, mask_path)
    masked_image = apply_mask(image, mask)
    volume = extrude_2d_to_3d(masked_image, depth=40)
    show_3d_volume(volume)

if __name__ == "__main__":
    main()

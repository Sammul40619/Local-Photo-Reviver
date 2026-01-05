from .preprocess import preprocess
from .restore import restore_photo
from .colorize import colorize_photo
from .animate import animate_photo

def run_pipeline(args):
    """
    Runs the full image processing pipeline.
    
    Args:
        args: An object containing processing options. It can come from the CLI or GUI.
              It should have attributes like restore, colorize, animate, and either
              `input` (for a file path) or `input_image` (for a numpy array).
              
    Returns:
        The final processed image as a NumPy array or a path to the saved video file.
    """
    img = preprocess(args)  # Pass the whole args object to the preprocessor
    
    if args.restore:
        img = restore_photo(img)
        
    if args.colorize:
        img = colorize_photo(img)
        
    if args.animate:
        # The animate function is expected to save a file and return the path
        output = animate_photo(img, mode=args.animate)
        return output

    # If not animating, return the processed image array
    return img
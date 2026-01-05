import gradio as gr
import numpy as np
from PIL import Image

# Import your pipeline functions
# Note: These are placeholder functions. You'll need to adapt them to work with NumPy arrays.
from pipeline.full_pipeline import run_pipeline

print("Loading models and setting up pipeline... (This may take a moment)")

def process_image(input_image, restore, colorize, animate_mode):
    """
    A wrapper function to connect the Gradio UI to the backend pipeline.
    
    Args:
        input_image (np.ndarray): The input image from Gradio's Image component.
        restore (bool): Whether to run the restoration pipeline.
        colorize (bool): Whether to run the colorization pipeline.
        animate_mode (str): The animation mode ('face' or 'parallax').
    
    Returns:
        The processed image or video.
    """
    if input_image is None:
        raise gr.Error("Please upload an image first!")

    print("Processing...")
    
    # Create a mock 'args' object to pass to the existing pipeline
    class Args:
        pass
    
    args = Args()
    args.input_image = input_image  # Pass the image data directly
    args.restore = restore
    args.colorize = colorize
    # Gradio dropdown sends "None" as a string if nothing is selected
    args.animate = animate_mode if animate_mode != "None" else None

    # The run_pipeline function will need to be adapted to handle an image array
    # instead of an input file path. It should return the final image array or video path.
    output = run_pipeline(args)

    print("Processing complete!")
    
    # The pipeline should return a NumPy array for images or a file path for videos
    return output


# Define the Gradio interface
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown(
        """
        # 🖼️ Local Photo Reviver
        Upload an old photo, select the AI pipelines you want to run, and see the magic happen!
        """
    )
    
    with gr.Row():
        with gr.Column(scale=1):
            image_input = gr.Image(type="numpy", label="Upload Your Photo")
            with gr.Accordion("⚙️ AI Options", open=True):
                restore_checkbox = gr.Checkbox(label="Restore (Fix damage & blur)", value=True)
                colorize_checkbox = gr.Checkbox(label="Colorize (Add color to B&W)", value=True)
                animation_dropdown = gr.Dropdown(
                    ["None", "face", "parallax"], label="Animate Photo", value="None"
                )
            
            submit_button = gr.Button("Revive Photo", variant="primary")

        with gr.Column(scale=1):
            # Use a single component that can display both images and videos
            # We will update its visibility based on the output type.
            image_output = gr.Image(label="Processed Image", visible=True)
            video_output = gr.Video(label="Animated Video", visible=False)
    
    gr.Markdown("---")
    gr.Markdown("📜 **Disclaimer**: This is a demo for research and educational purposes. Please respect privacy and historical accuracy.")

    def on_submit(input_image, restore, colorize, animate_mode):
        # This function handles the output type switching
        processed_output = process_image(input_image, restore, colorize, animate_mode)
        
        # Heuristic to check if the output is a video path or an image array
        if isinstance(processed_output, str) and processed_output.endswith(('.mp4', '.avi', '.mov')):
            # It's a video
            return {
                image_output: gr.update(visible=False),
                video_output: gr.update(visible=True, value=processed_output)
            }
        else:
            # It's an image
            return {
                image_output: gr.update(visible=True, value=processed_output),
                video_output: gr.update(visible=False)
            }
            
    submit_button.click(
        fn=on_submit,
        inputs=[image_input, restore_checkbox, colorize_checkbox, animation_dropdown],
        outputs=[image_output, video_output]
    )


if __name__ == "__main__":
    print("Launching Gradio interface...")
    demo.launch(share=False)

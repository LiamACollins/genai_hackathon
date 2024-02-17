

import subprocess

def convert_mp4_to_gif(input_file, output_file):
    # Command to convert MP4 to GIF using FFmpeg
    # This example uses a simple conversion process.
    # You may want to add additional options to optimize the size and quality of the output GIF.
    cmd = [
        'ffmpeg',
        '-i', input_file,  # Input file
        '-filter_complex', '[0:v] fps=10,scale=480:-1:flags=lanczos,split [a][b];[a] palettegen [p];[b][p] paletteuse',
        '-f', 'gif',  # Output format
        output_file  # Output file
    ]
    
    try:
        # Execute the FFmpeg command
        subprocess.run(cmd, check=True)
        print(f"Conversion successful: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion: {e}")

# Example usage
for input_mp4 in ['converted_thriller_vibrant_independence.mp4', 'converted_thriller_vibrant_liberty_bell.mp4', 'converted_hist_kodak_independence.mp4', 'converted_hist_kodak_bell.mp4']:
    output_gif = input_mp4[:-4] + '.gif'  # Replace with the desired output GIF file path

    convert_mp4_to_gif(input_mp4, output_gif)
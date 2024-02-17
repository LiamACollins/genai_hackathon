

import subprocess

def convert_mp4_to_gif(input_file, output_file):
    # Command to convert MP4 to GIF using FFmpeg
    # This example uses a simple conversion process.
    # You may want to add additional options to optimize the size and quality of the output GIF.
    cmd = [
        'ffmpeg',
        '-i', input_file,  # Input file
        '-vf', 'fps=10,scale=320:-1',  # Frame rate and scale options
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
input_mp4 = 'converted_thriller_vibrant_independence.mp4'  # Replace with the path to your MP4 file
output_gif = input_mp4[:-4] + '.gif'  # Replace with the desired output GIF file path

convert_mp4_to_gif(input_mp4, output_gif)
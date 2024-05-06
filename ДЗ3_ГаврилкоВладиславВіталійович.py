import os
import shutil
import argparse

def copy_files_recursively(source_dir, target_dir):
    # Create target directory if not exists
    os.makedirs(target_dir, exist_ok=True)
    
    for item in os.listdir(source_dir):
        source_path = os.path.join(source_dir, item)
        if os.path.isdir(source_path):
            # Recursively call this function for subdirectories
            copy_files_recursively(source_path, target_dir)
        elif os.path.isfile(source_path):
            # Handle the file: create subdir based on file extension and copy file
            file_ext = os.path.splitext(item)[1][1:]  # Get extension without the dot
            if not file_ext:
                file_ext = 'no_extension'
            ext_dir = os.path.join(target_dir, file_ext)
            os.makedirs(ext_dir, exist_ok=True)
            shutil.copy(source_path, ext_dir)

def parse_arguments():
    parser = argparse.ArgumentParser(description="Copy files by extension to new directory structure")
    parser.add_argument("source_dir", type=str, help="Path to the source directory")
    parser.add_argument("target_dir", type=str, nargs='?', default="dist", help="Path to the target directory (default: dist)")
    args = parser.parse_args()
    return args

# The function calls are commented out for now, as per instructions
# args = parse_arguments()
# copy_files_recursively(args.source_dir, args.target_dir)

import turtle

def koch_curve(t, length, depth):
    if depth == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch_curve(t, length, depth-1)
        t.left(60)
        koch_curve(t, length, depth-1)
        t.right(120)
        koch_curve(t, length, depth-1)
        t.left(60)
        koch_curve(t, length, depth-1)

def draw_koch_snowflake():
    recursion_depth = int(input("Enter the recursion depth of the Koch snowflake: "))
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)

    # Initial setup to position the snowflake
    t.penup()
    t.goto(-150, 90)
    t.pendown()

    # Draw three sides of the Koch snowflake
    for _ in range(3):
        koch_curve(t, 300, recursion_depth)
        t.right(120)

    t.hideturtle()
    window.mainloop()

# The function calls are commented out for now, as per instructions
# draw_koch_snowflake()

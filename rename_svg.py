import os

def delete_and_rename(directory, index):
    """
    Delete the SVG at the specified index and rename all SVGs after it.
    
    :param directory: The directory containing the SVG files.
    :param index: The index of the SVG file to delete (0-based).
    """
    # List all SVG files in the directory
    svg_files = [f for f in os.listdir(directory) if f.endswith('.svg')]
    svg_files.sort(key= lambda f: int(f.split('.')[0]))
    
    # Check if the index is valid
    if index < 0 or index >= len(svg_files):
        print("Invalid index")
        return

    # Delete the SVG at the specified index
    os.remove(os.path.join(directory, svg_files[index]))
    print(f"Deleted {svg_files[index]}")

    # Rename all SVGs after the deleted one
    for i in range(index + 1, len(svg_files)):
        old_name = os.path.join(directory, svg_files[i])
        new_name = os.path.join(directory, svg_files[i - 1])
        os.rename(old_name, new_name)
        print(f"Renamed {svg_files[i]} to {svg_files[i - 1]}")

if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('--directory', help="The directory containing the SVG files.")
    parser.add_argument('--index', type=int, help="The index of the SVG file to delete (0-based).")
    args = parser.parse_args()
    directory_path = args.directory
    index_to_delete = args.index - 1
    delete_and_rename(directory_path, index_to_delete)

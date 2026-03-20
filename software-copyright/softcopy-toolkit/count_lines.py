#!/usr/bin/env python3
"""Count lines of code in a directory structure."""

import os
import sys

SOURCE_EXTENSIONS = {
    '.py', '.js', '.java', '.c', '.cpp', '.h', '.sh', '.bash',
    '.yml', '.yaml', '.tex', '.json'
}


def count_file_lines(file_path):
    """Count lines in a single file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return len(f.readlines())
    except:
        return 0


def should_ignore(path):
    """Check if path should be ignored."""
    ignore_dirs = {'.git', '__pycache__', 'node_modules', '.idea', '.vscode', 'venv', 'env'}
    ignore_files = {'.gitignore', 'LICENSE'}
    ignore_exts = {'.log', '.out', '.err', '.csv', '.xml', '.pkl', '.jpg', '.jpeg', '.png', '.gif', '.pdf', '.zip', '.tar', '.gz'}

    name = os.path.basename(path)

    # Check directory names
    if os.path.isdir(path) and name in ignore_dirs:
        return True

    # Check file names and extensions
    if os.path.isfile(path):
        if name in ignore_files:
            return True
        _, ext = os.path.splitext(name)
        if ext in ignore_exts:
            return True

    return False


def count_directory_lines(directory):
    """Count lines in all source files in directory."""
    total_lines = 0
    file_count = 0

    for root, dirs, files in os.walk(directory):
        # Remove ignored directories from traversal
        dirs[:] = [d for d in dirs if not should_ignore(os.path.join(root, d))]

        for file in files:
            file_path = os.path.join(root, file)
            if should_ignore(file_path):
                continue

            if any(file.endswith(ext) for ext in SOURCE_EXTENSIONS):
                lines = count_file_lines(file_path)
                rel_path = os.path.relpath(file_path, directory)
                print(f"{rel_path}: {lines} lines")
                total_lines += lines
                file_count += 1

    print(f"\nTotal: {file_count} files, {total_lines} lines")
    return total_lines, file_count


def remove_empty_lines(file_path):
    """Remove empty lines from a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        non_empty_lines = [line for line in lines if line.strip()]
        with open(file_path, 'w', encoding='utf-8') as f:
            if non_empty_lines:
                if not non_empty_lines[-1].endswith('\n'):
                    non_empty_lines[-1] += '\n'
                f.writelines(non_empty_lines)
        return len(non_empty_lines)
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return 0


def remove_empty_lines_from_directory(directory, extensions=None):
    """Remove empty lines from all source files in directory."""
    if extensions is None:
        extensions = SOURCE_EXTENSIONS
    total_lines = 0
    file_count = 0
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if not should_ignore(os.path.join(root, d))]
        for file in files:
            file_path = os.path.join(root, file)
            if should_ignore(file_path):
                continue
            if any(file.endswith(ext) for ext in extensions):
                lines = remove_empty_lines(file_path)
                rel_path = os.path.relpath(file_path, directory)
                print(f"{rel_path}: {lines} lines (after removing empty lines)")
                total_lines += lines
                file_count += 1
    print(f"\nTotal: {file_count} files, {total_lines} lines")
    return total_lines, file_count


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python count_lines.py <directory> [--remove-empty]")
        sys.exit(1)
    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print(f"Directory not found: {directory}")
        sys.exit(1)
    if len(sys.argv) > 2 and sys.argv[2] == '--remove-empty':
        remove_empty_lines_from_directory(directory)
    else:
        count_directory_lines(directory)

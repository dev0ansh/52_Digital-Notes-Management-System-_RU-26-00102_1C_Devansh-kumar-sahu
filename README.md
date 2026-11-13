# Notes Management System

A small, menu-driven command-line app for creating and managing personal notes. It uses only the Python standard library.

## Requirements

- Python 3

## Run

From this directory, run:

```bash
python project2.py
```

On Windows, `py project2.py` can be used if the Python launcher is installed.

## Features

The interactive menu lets you:

- Add notes with automatically generated IDs (`N1`, `N2`, and so on).
- List notes and view an individual note by ID.
- Search note titles and content (search is case-sensitive).
- Edit a note's title or content; press Enter to keep either value unchanged.
- Delete a note after confirming the action.

Titles cannot be empty or contain the `|` character. Blank lines in note content are removed, and newlines are converted to spaces.

## Data storage

Notes are stored in `project.txt` in the current working directory. The file is created when a note is saved; it is intentionally excluded from version control so personal note data is not uploaded. Each line stores one note as `ID|title|content`.

Run the app from the same directory each time to continue using the same `project.txt` file.

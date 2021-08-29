from pathlib import Path
# Absolute path
# Start from harddrive
# relative path
# or from our current directory

# Path() references the current directory
path = Path("ecommerce")
print(path.exists())

# Make Directory
path = Path("emails")
print(path.mkdir())

# Remove directory
path = Path("emails")
print(path.rmdir())

# References current Dir
path = Path()
# Searches through every file in current director
# * would find every file and directory
# *.* for every file
for file in (path.glob('*.*')):
    print(file)


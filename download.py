import kagglehub

# Download latest version
path = kagglehub.dataset_download("datasnaek/chess")

print("Path to dataset files:", path)

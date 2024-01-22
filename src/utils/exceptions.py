class MetadataFolderNotFoundError(Exception):
    def __init__(self, metadata_folder_name, prefix, folder):
        self.metadata_folder_name = metadata_folder_name
        self.prefix = prefix
        self.folder = folder

    def __str__(self):
        return f"{self.metadata_folder_name} folder not found inside {self.prefix}/{self.folder}"

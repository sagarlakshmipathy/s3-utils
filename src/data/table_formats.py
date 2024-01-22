from enum import Enum


class MetadataFolderNames(Enum):
    HUDI = ".hoodie"
    ICEBERG = "metadata"
    DELTA = "_delta_log"

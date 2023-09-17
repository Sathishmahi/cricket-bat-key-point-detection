import os
import yaml

def read_config(yaml_file_path: str = "config/config.yaml") -> dict:
    """
    Read a YAML configuration file and return its contents as a dictionary.

    Args:
        yaml_file_path (str, optional): The path to the YAML configuration file.
            Defaults to "config/config.yaml".

    Returns:
        dict: A dictionary containing the configuration data.

    Raises:
        FileNotFoundError: If the specified YAML file does not exist.
        Exception: If there is an error while loading the YAML file.

    Example:
        >>> config_data = read_config("my_config.yaml")
    """
    if not os.path.exists(yaml_file_path):
        raise FileNotFoundError(f"{yaml_file_path} not found")
    try:
        with open(yaml_file_path, 'r') as f:
            config = yaml.safe_load(f)
        return config
    except Exception as e:
        raise e

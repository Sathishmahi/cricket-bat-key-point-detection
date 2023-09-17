import os
import os
import yaml

def read_config(yaml_file_path:str = "config/config.yaml" )->dict:
    if not os.path.exists(yaml_file_path):
        raise FileNotFoundError(f"{yaml_file_path} not found")
    try:
        with open(yaml_file_path, 'r') as f:
            config = yaml.safe_load(f)
        return config
    except Exception as e:
        raise e
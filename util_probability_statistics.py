# probability_statistics\util_probability_statistics.py

# created 2/2/25
# last updated 2/2/25

import sys, os, json, logging
import importlib.util

### DIRECTORY ###
def get_working_directory(scan_file="README.md"):
    # updated 8.1.24
    current_directory = os.getcwd()
    parent_directory = os.path.dirname(current_directory)

    if os.path.exists(os.path.join(current_directory, scan_file)):
        working_directory = current_directory
        return working_directory
    elif os.path.exists(os.path.join(parent_directory, scan_file)):
        working_directory = parent_directory
        return working_directory
    else:
        raise FileNotFoundError(f"Cannot determine the working directory because {scan_file} was not found in the current or the parent directory.")
    
def get_script_directory_depth(script_filepath, logger=None, scan_directory="develop"):
    # updated 9.1.24
    logger = setup_fallback_logger(logger)

    script_filepath = os.path.abspath(__file__)
    logger.info(f"script_filepath: {script_filepath}")


### LOGGING ###
def setup_logging(script_name):
    # updated 8.1.24
    working_directory = get_working_directory()
    log_directory = os.path.join(working_directory, "log")
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    log_file = os.path.join(log_directory, f"{script_name}.log")
    with open(log_file, "w"):
        pass

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )

    logger = logging.getLogger(script_name)
    logger.info(f"Logging initialized for {script_name}")

    return logger

def setup_fallback_logger(logger):
    # updated 8.1.24
    if logger is None:
        logger = logging.getLogger(__name__)
        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            logger.setLevel(logging.INFO)
    return logger

### INTERCONNECTING PYTHON ###
def process_module(module_name, logger=None):
    # updated 8.1.24
    logger = setup_fallback_logger(logger)
    if module_name in sys.modules:
        module = sys.modules[module_name]
        logger.info(f"Module {module_name} found in sys.modules")
        return module
    else:
        logger.info(f"Module {module_name} not found in sys.modules")
        return None
    
def import_modules(processes_directory, module_names, logger=None):
    # updated 8.1.24
    logger = setup_fallback_logger(logger)
    imported_modules = {}
    for module_name in module_names:
        module_path = os.path.join(processes_directory, f"{module_name}.py")
        if not os.path.exists(module_path):
            logger.error(f"Module path does not exist: {module_path}")
        
        spec = importlib.util.spec_from_file_location(module_name, module_path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)

        if module_name in sys.modules:
            logger.info(f"Module {module_name} imported successfully")
            imported_modules[module_name] = module
        else:
            logger.error(f"Failed to import module {module_name}")
    return imported_modules

### JSON ###
def get_parameter(parameter_key, parent_directory=None, logger=None):
    # updated 8.1.24
    logger = setup_fallback_logger(logger)
    if parent_directory == None:
        parent_directory = get_working_directory()
        logger.debug(f"parent_directory argument is None, get_working_directory(), parent_directory={parent_directory}")

    parameters_filepath = os.path.join(parent_directory, "parameters.json")
    with open(parameters_filepath, "r") as parameters_file:
        parameters = json.load(parameters_file)
    logger.debug(f"parameters:\n{parameters}")

    parameter = parameters[parameter_key]
    logger.debug(f"parameters[{parameter_key}]={parameter}")

    return parameter

def write_parameter(parameter_key, parameter_new_value, parent_directory=None, logger=None):
    # updated 8.1.24
    logger = setup_fallback_logger(logger)
    if parent_directory == None:
        parent_directory = get_working_directory()
        logger.debug(f"parent_directory argument is None, get_working_directory(), parent_directory={parent_directory}")

    parameters_filepath = os.path.join(parent_directory, "parameters.json")
    with open(parameters_filepath, "r") as parameters_file:
        parameters = json.load(parameters_file)
    logger.debug(f"parameters:\n{parameters}")

    parameters[parameter_key] = parameter_new_value
    logger.debug(f"parameters[{parameter_key}] set to {parameter_new_value}")
    
    with open(parameters_filepath, "w") as parameters_file:
        json.dump(parameters, parameters_file, indent=4)
    logger.debug(f"parameters writeen to {parameters_filepath}")

def write_to_json(filepath, key, new_value, logger=None):
    # updated 8.1.24
    logger = setup_fallback_logger(logger)
    with open(filepath, "r") as file:
        data = json.load(file)
    logger.debug(f"data of {filepath}:\n{data}")

    data[key] = new_value
    logger.debug(f"set data[{key}] to {new_value}")

    with open(filepath, "w") as file:
        json.dump(data, file, indent=4)
    logger.debug(f"new data written to {filepath}")
# probability_statistics\config_probability_statistics.py

# created 2/2/25
# last updated 2/2/25

from pathlib import Path
from package_setup_probability_statistics import PackageSetupProbabilityStatistics

script_filepath = Path(__file__).resolve()
package_setup = PackageSetupProbabilityStatistics(script_filepath, level="debug")
logger = package_setup.setup_logger()
scan_directory_path = package_setup.scan_directory_path
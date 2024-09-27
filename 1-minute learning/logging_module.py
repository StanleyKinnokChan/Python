import logging
import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Change the current working directory to the script's directory
os.chdir(script_dir)

print("Current working directory:", os.getcwd())


# 1. Basic Logging Example
# -------------------------
# The simplest way to use logging is to log messages at different severity levels.

# Configure the logging system
logging.basicConfig(level=logging.DEBUG)

# Log messages of different severity levels
logging.debug("This is a DEBUG message - for debugging information.")
logging.info("This is an INFO message - for general information.")
logging.warning("This is a WARNING message - for something unexpected or a warning.")
logging.error("This is an ERROR message - for an error that occurred.")
logging.critical("This is a CRITICAL message - for serious errors or crashes.")

# Explanation:
# - The `basicConfig()` function configures the logging system with the specified settings.
# - The `level=logging.DEBUG` sets the minimum logging level to DEBUG, so all messages from DEBUG and above will be shown.
# - The `logging.debug()`, `logging.info()`, etc., are methods to log messages at different levels of severity.


# 2. Changing Logging Format
# --------------------------
# You can customize the format of the logged messages by specifying a format string.

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True
)

logging.info("This is an INFO message with a custom format.")

# Explanation:
# - The `format` argument in `basicConfig()` specifies the structure of the log message.
# - `%(asctime)s`: The time when the log message was generated.
# - `%(levelname)s`: The severity level of the log message (DEBUG, INFO, WARNING, ERROR, CRITICAL).
# - `%(message)s`: The actual log message.


# 3. Logging to a File
# --------------------
# Instead of logging messages to the console, you can direct them to a file.

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename=r"log.log",  # Log messages will be written to 'app.log'
    filemode="w",         # 'w' mode will overwrite the file each time the script runs
    force=True
)

logging.info("This INFO message will be written to a file.")

# Explanation:
# - The `filename` argument in `basicConfig()` specifies the file to which log messages will be written.
# - The `filemode` argument can be set to "w" (write mode) or "a" (append mode). "w" overwrites the file on each run, while "a" appends new log messages.


# 4. Advanced Configuration with Multiple Handlers
# ------------------------------------------------
# You can set up multiple handlers to log messages to both the console and a file simultaneously.

# Create a custom logger
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)

# Create a file handler for logging to a file
file_handler = logging.FileHandler('app_advanced.log')
file_handler.setLevel(logging.DEBUG)

# Create a console handler for logging to the console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Create a formatter and set it for both handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add the handlers to the logger (where the logs in the logger should be sent to)
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Log messages using the custom logger
logger.debug("This DEBUG message will go to both the console and the file.")
logger.info("This INFO message will go to both the console and the file.")

# Explanation:
# - `getLogger('my_logger')`: Creates or retrieves a logger object.
# - `FileHandler('app_advanced.log')`: Logs messages to a file.
# - `StreamHandler()`: Logs messages to the console (stdout).
# - `setFormatter()`: Applies the same formatting to both file and console outputs.
# - `addHandler()`: Adds the handlers to the logger so that it can log to multiple destinations.


# 5. Logging Exceptions
# ---------------------
# You can automatically include exception information in log messages using the `exc_info=True` parameter.

try:
    x = 1 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    logger.error("An exception occurred!", exc_info=True)

# Explanation:
# - `exc_info=True`: Automatically adds the stack trace to the log message when an exception is caught.


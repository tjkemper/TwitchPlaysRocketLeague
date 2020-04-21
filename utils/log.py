import logging
import colorlog
from colorlog import ColoredFormatter

formatter = ColoredFormatter(
	# "%(bold_purple)s %(asctime)s %(log_color)s%(levelname)-8s%(reset)s %(message)s",
    "%(bold_purple)s %(asctime)s %(log_color)s%(levelname)-8s %(message)s",
	datefmt="%Y-%m-%d %H:%M:%S",
	reset=True,
	log_colors={
		'DEBUG':    'bold_cyan',
		'INFO':     'bold_green',
		'WARNING':  'bold_yellow',
		'ERROR':    'bold_red',
		'CRITICAL': 'bold_red,bg_white',
	},
	secondary_log_colors={},
	style='%'
)

def init_logger(level=logging.DEBUG):
    handler = colorlog.StreamHandler()
    handler.setFormatter(formatter)

    logger = get_logger()
    logger.setLevel(level)
    logger.addHandler(handler)

def get_logger():
    return colorlog.getLogger('TwitchPlaysRocketLeague')

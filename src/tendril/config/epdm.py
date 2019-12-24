

from tendril.utils.config import ConfigOption
from tendril.utils import log
logger = log.get_logger(__name__, log.DEFAULT)

depends = ['tendril.config.core']


config_elements_epdm = [
    ConfigOption(
        "EPDM_HOST",
        "None",
        "EPDM hostname"
    ),
    ConfigOption(
        "EPDM_USERNAME",
        "''",
        "Username to use to connect to EPDM"
    ),
    ConfigOption(
        "EPDM_PASSWORD",
        "''",
        "Password to use to connect to EPDM"
    )
]


def load(manager):
    logger.debug("Loading {0}".format(__name__))
    manager.load_elements(config_elements_epdm,
                          doc="EPDM Connector Configuration")

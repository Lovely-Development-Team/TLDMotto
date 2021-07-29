import logging.config

# Configure logging
logging.config.fileConfig(fname="log.conf", disable_existing_loggers=False)
logging.getLogger("discord").setLevel(logging.CRITICAL)
logging.getLogger("discord.gateway").setLevel(logging.INFO)
logging.getLogger("asyncio").setLevel(logging.CRITICAL)
logging.getLogger("urllib").setLevel(logging.CRITICAL)
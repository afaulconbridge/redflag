import argparse
import logging
import logging.config


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--log-config", type=str, default=None, help="log configuration file"
    )
    parser.add_argument(
        "--log-critical", action="store_const", const=logging.CRITICAL, dest="log_level"
    )
    parser.add_argument(
        "--log-error", action="store_const", const=logging.ERROR, dest="log_level"
    )
    parser.add_argument(
        "--log-warning", action="store_const", const=logging.WARNING, dest="log_level"
    )
    parser.add_argument(
        "--log-info",
        action="store_const",
        const=logging.INFO,
        dest="log_level",
        default=logging.INFO,
    )
    parser.add_argument(
        "--log-debug", action="store_const", const=logging.DEBUG, dest="log_level"
    )
    args = parser.parse_args()

    logging.basicConfig(level=args.log_level)
    if args.log_config:
        logging.config.fileConfig(args.log_config)

    # TODO update
    logger = logging.getLogger("redflag")

    if args.log_config:
        logger.debug("loaded log config from {}".format(args.log_config))

    # TODO finish


if __name__ == "__main__":
    main()

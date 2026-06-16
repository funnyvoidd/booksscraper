import argparse
from core.engine import run

def main():
    parser = argparse.ArgumentParser(description="Scraping system CLI")

    parser.add_argument(
        "--config",
        default="src/config/config.yaml",
        help="Path to config file"
    )

    args = parser.parse_args()

    run(args.config)


if __name__ == "__main__":
    main()
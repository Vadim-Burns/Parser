from parser import ExampleParser
from signal import signal, SIGTERM, SIGINT


def main():
    p = ExampleParser()
    p.run()

    def handle_sigterm(*_):
        print("Shutdown signal received")
        p.stop()
        print("Shutdown gracefully")

    signal(SIGTERM, handle_sigterm)
    signal(SIGINT, handle_sigterm)
    try:
        p.stop()
    except KeyboardInterrupt:
        handle_sigterm()


if __name__ == '__main__':
    main()

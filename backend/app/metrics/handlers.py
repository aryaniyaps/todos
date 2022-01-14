from prometheus_client import start_http_server

from app.core.config import METRICS_PORT


def start_metrics() -> None:
    """
    Starts the metrics server.
    """
    start_http_server(port=METRICS_PORT)
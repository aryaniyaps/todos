from prometheus_client import start_http_server

from app.config import settings


def start_metrics() -> None:
    """
    Starts the metrics server.
    """
    start_http_server(port=settings.METRICS_PORT)
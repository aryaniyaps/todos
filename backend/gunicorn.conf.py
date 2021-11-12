import multiprocessing

# server socket
bind = "0.0.0.0:8000"

# worker processes
workers = (multiprocessing.cpu_count() * 2) + 1
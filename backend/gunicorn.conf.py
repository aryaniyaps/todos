from multiprocessing import cpu_count

# server socket
bind = "0.0.0.0:8000"

# worker processes
workers = (cpu_count() * 2) + 1
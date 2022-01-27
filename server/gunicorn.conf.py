from multiprocessing import cpu_count

# server socket.
bind = "0.0.0.0:5000"

# worker processes.
workers = (cpu_count() * 2) + 1

# worker class.
worker_class = "gevent"

# worker connections.
worker_connections = pow(10, 2)

# max requests to be processed.
max_requests = pow(10, 3)

# worker timeout.
timeout = 15

# request waiting time.
keepalive = 5

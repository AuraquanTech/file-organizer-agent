from prometheus_client import Counter, Histogram, start_http_server
start_http_server(8000)
REQS=Counter('agent_requests','Total requests')
LATENCY=Histogram('agent_latency','Request latency')
def record(fn):
    def wrapped(*a,**k):
        REQS.inc();
        with LATENCY.time():
            return fn(*a,**k)
    return wrapped

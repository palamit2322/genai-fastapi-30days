import time
from collections import defaultdict

RATE_LIMIT=5
WINDOW_SIZE=60

request_store=defaultdict(list)

def is_rate_limited(client_id:str)->bool:
    current_time= time.time()
    window_start=current_time-WINDOW_SIZE
    return True

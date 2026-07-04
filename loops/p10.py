import time
wait_time = 1
max_retries = 5
Attempts = 0

while Attempts <= max_retries:
    print ("Attempts", Attempts+1,"-wait time",wait_time)
    time.sleep(wait_time)
    wait_time*=2
    Attempts+=1
    
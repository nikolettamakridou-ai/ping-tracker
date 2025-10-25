import os 
import time 

servers = [ " 8. 8. 8. 8 " , " 1. 1. 1. 1 " , " www.google.com " ] 

print(" Ping Tracker Started\n ")
while True :
  for s in servers :
    response = os.system ( f"ping -n 1 {s} > nul " )
    status = " Online " if response == 0 else " Offline " 

    print ( f"{s:20} -> {status}" )
    print ( "-" * 40 )
    time.sleep(5)
    
    
      

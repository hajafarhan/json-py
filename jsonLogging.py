import time,json,sys,datetime 
i=0 
while True:
            i=i+1
            ts=time.time()
            data={
              "timestamp"   :datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'),
              "index"       :i,
              "Employee ID":1000,
              "Name":"Subajith",
              "Designation":"Software Engineer",
              "Organization": "Grameenphone"
            }
           
            json_string = json.dumps(data)
            print(json_string)
            time.sleep(1) # sleep for 1 sec

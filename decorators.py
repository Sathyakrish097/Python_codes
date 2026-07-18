import time

def time_taken(base_fn):
    def enhance_fn():
        start_time= time.time()
        base_fn()
        end_time= time.time()
        total_time= end_time-start_time
        print(f"Time taken: {total_time} seconds")
        print("==============================================")
    return enhance_fn 

@time_taken
def tea():
    print("Preparing Tea....")
    time.sleep(1)
    print("Tea is ready to drink!..")
 
@time_taken  
def coffee():
    print("Preparing Coffee....")
    time.sleep(1)
    print("Coffee is ready to drink!..")

def main():
    tea()
    coffee()
    
if __name__ == "__main__":
    main()
    

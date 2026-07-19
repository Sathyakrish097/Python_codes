import time
from  datetime import datetime, timedelta

def time_taken(base_fn):
    def enhance_fn(*args, **kwargs):
        start_time= time.time()
        result= base_fn(*args, **kwargs)
        end_time= time.time()
        total_time= end_time-start_time
        print(f"Time taken: {total_time} seconds")
        print("==============================================")
        return result
    return enhance_fn 

@time_taken
def tea(tea_type, steep_time):
    print(f"Preparing {tea_type} Tea....")
    time.sleep(steep_time)
    print(f"{tea_type} Tea is ready to drink!..")
 
@time_taken  
def coffee():
    print("Preparing Coffee....")
    time.sleep(1)
    print("Coffee is ready to drink!..")
    return f"Drink Coffee by {datetime.now() + timedelta(minutes=30)}"

def main():
    tea("green", 2)
    print(coffee())
    
if __name__ == "__main__":
    main()
    

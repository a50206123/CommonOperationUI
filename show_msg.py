import time

def tic_toc(name:str) :
    def deco(func) :
        def wrapper(*args, **kwags) :
            start = time.time()
            print(f"{f' Do {name} ':*^60s}")

            func(*args, **kwags)

            end = time.time()
            spend = end - start
            print(f"{f' Done {name} (Took {spend:.3f} sec)':*^60s}")
        return wrapper
    return deco



# def click_msg(name) :
#     print(f"{f' Do {name} ':*^60s}")

# def done_msg(name) :
#     print(f"{f' Done {name} ':*^60s}")
import time

def timer_decorator(function):
    def enhanced_function(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)
        end_time = time.time()
        print(f"Task time: {end_time - start_time}")
        return result
    return enhanced_function


@timer_decorator
def brew_tea(tea_type, seep_time):  
    print(f'{tea_type} tea is brewing')
    time.sleep(seep_time)
    print('Tea is ready!!')
    
@timer_decorator
def make_pasta():
    print('Pasta is boiling')
    time.sleep(2)
    print('Pasta is ready!!')
    return "Eat it up before it's cold"

@timer_decorator
def countdown(num):
    for i in range(num, 0, -1):
        print(i)
        time.sleep(1)
    print('TIMES UP!!!!')

brew_tea(seep_time=1, tea_type='black')
print(make_pasta())
countdown(num=3)

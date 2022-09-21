import sys, inspect

# https://blog.jerrycodes.com/sneak-peek-python-3-8/
def audit(event, args):
    if 'socket' in event:
        if event == 'socket.connect':
            for info in inspect.stack()[::-1]:
                if info.filename.endswith("/mymodule.py"):
                    print("module 1")
                    break
                # print(info.filename)
                # print(info.lineno)
                # print(info.function)
                # print(info.code_context)
                # print('')
                    #raise RuntimeError('Alright, this is too much')
        #sys.audit("event_name", 1, 2, dict(key="value"))
        #print(f'Captain, some networking going on: event={event}, args={args}')
    # else:
    #     print(f'Not very interesting event: {event}')

sys.addaudithook(audit)

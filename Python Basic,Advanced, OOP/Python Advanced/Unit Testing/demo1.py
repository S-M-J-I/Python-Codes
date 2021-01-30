def do_stuff(num):
    try:
        if num:
            # if num has a value,then true
            return int(num) + 5
        else:
            return "please enter a number"
    except ValueError as ex:
        # check for number. if not a number, then throw error
        # returns an instance of ValueError class
        return ex


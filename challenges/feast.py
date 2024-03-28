def feast(beast, dish):
    if beast[0] == dish[0]:
        if beast[len(beast)-1] == dish[len(dish)-1]:
            return True
        else:
            return False
    else: 
        return False
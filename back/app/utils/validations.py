def validate_arr_numbers(arr):
    int_arr = []
    for item in arr:
        try: 
            int_item = int(item) 
            int_arr.append(int_item)
        except Exception as e:
            print(e)
            return False,[]
    return True, int_arr
    
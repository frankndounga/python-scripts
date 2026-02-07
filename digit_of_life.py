import sys

#This function create an equivalent array of the date with the specified month in number
def equivalent_date_array(date_of_birth):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    try:
        string_to_array = date_of_birth.split(' ')
        month_to_number = months.index(string_to_array[1]) + 1
    except ValueError:
        return "You must enter a valid date in format day full_month year"
    else:
        string_to_array[1] = str(month_to_number)
    return int("".join(string_to_array))

#this function return array of integer values of an array form with values of a number
def convert_and_sum_values(value):
    if type(value) == str:
        print('Invalid format')
        sys.exit()
    value = str(value)
    value = list(value)
    print(value)
    array_of_numb = [int(val) for val in value]
    return array_of_numb

#this function do the return the digit of life
def find_digit_of_life(date_of_birth):
    digit_of_life = sum(convert_and_sum_values(equivalent_date_array(date_of_birth)))
    while digit_of_life > 10:
        digit_of_life = sum(convert_and_sum_values(digit_of_life))
    return digit_of_life

if __name__ == '__main__':

    #test
    date = "11 September 1988"
    print(find_digit_of_life(date))

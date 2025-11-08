def move(my_list, direction):
    # מציאת האינדקס של ה-1 (מניחים שקיים 1 אחד בדיוק לפי ההנחיות)
    index_of_one = my_list.index(1)
    
    # גודל הרשימה
    list_length = len(my_list) 
    
    # הזזה ימינה
    if direction == 'right':
        # בודק אם ה-1 אינו האיבר האחרון
        if index_of_one < list_length - 1:
            my_list[index_of_one] = 0
            my_list[index_of_one + 1] = 1
            
    # הזזה שמאלה
    elif direction == 'left':
        # בודק אם ה-1 אינו האיבר הראשון
        if index_of_one > 0:
            my_list[index_of_one] = 0
            my_list[index_of_one - 1] = 1
            
    return my_list

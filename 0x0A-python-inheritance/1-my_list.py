
dule: 1-my_list
'''


class MyList(list):
    ''' Represents a MyList
    '''

    def print_sorted(self):
        '''
        prints the list, but sorted
        '''
        print(sorted(self))

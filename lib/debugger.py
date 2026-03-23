class VarsFollowing:
    def __init__(self):
        '''
            Make the value following for the sets
            of variable and in a program for determined
            momentums
        '''
        # Key: Var name, Value: Var value
        self.vars: dict = {}
        # Key: Var name, Value: Moment name
        self.date: dict = {}
        # Key: Var name, Value: Var type
        self.kinds: dict = {}
        
    def set_var(self, name: str, kind: str, value: str):
        '''
            Add a new var with his value
        '''
        # Reduce mistakes and lines from two to one
        self.vars.__setitem__(name, value)
        self.kinds.__setitem__(name, kind)

    def set_moment(self, name: str, moment: str):
        '''
            Add a new moment for the var
        '''    
        self.date.__setitem__(name, moment)

    def get_following(self, name: str) -> str:
        '''
            Give the moment, the var name, type
            and value.

            write a debug.log file for auxiliar storage
            for future consult without make complicated
            code
        '''   
        result: str = f'\t{self.date[name]}: {name}, {self.kinds[name]} -> {self.vars[name]}\n'
        
        with open('debug.log', 'a') as debugger:
            debugger.write(result)
            
        return result
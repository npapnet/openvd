class Tire(object):
    '''Tire Tire abstract class This class must be inherited by tire models that will be used with the simulator. This class has no properties, since parameters of tire models differ significantly from one another.

    :var param: Loucura

    '''

    def __init__(self):
        self.param = 10

    def Characteristic(self, alpha, varargin):
        ''' an abstract method that should be overriden from other models
        
        Returns: Not Applicable
        '''
        pass

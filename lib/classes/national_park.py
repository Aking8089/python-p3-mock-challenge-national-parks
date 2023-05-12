from statistics import mode
class NationalPark:
 
    def __init__(self, name):
        if isinstance(name, str)and name:
            self._name = name
        else:
            raise Exception
        self._trips = []
        self._visitors = []
        
    @property
    def name(self):
            return self._name

        
    def trips(self):
        from classes.trip import Trip
        return [t for t in Trip.all if t.national_park == self]
    
    def visitors(self):
        return list(set([t.visitor for t in self.trips() if t.national_park == self]))
    
    
    def total_visits(self):
        return len(self.trips())
    
    def best_visitor(self):
        visitors = [t.visitor for t in self.trips()]
        return max(visitors, key=visitors.count)
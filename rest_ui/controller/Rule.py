

class Rule(object):
    
    def __init__(self):
        self.header = {
            "Content-Type":"application/json",
            # "X-Client-Id":"6786787678f7dd8we77e787",
            # "X-Client-Secret":"96777676767585",
        }
   
        self.payload = {
            "x": "test_x",
            "y": "test_y",
            "start_date": "2022-05-27 12:48:07"
        }
        
    def get_header(self):
        return self.header
        
    def get_payload(self):
        return self.payload
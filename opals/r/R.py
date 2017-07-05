
import subprocess
import os
from bedrock.analytics.utils import Algorithm 


class R(Algorithm):
    def __init__(self):
        super(R, self).__init__()
        self.parameters = []
        self.inputs = []
        self.outputs = ['output.txt']
        self.name ='R'
        self.type = 'R'
        self.description = 'Runs arbitrary R code.'
        self.parameters_spec = [{ "name" : "InputSpec", "attrname" : "inputspec", "value" : '', "type" : "input"}]

    def compute(self, filepath, **kwargs):
        
        # Write self.inputspec to file
        Rpath = os.path.dirname(os.path.abspath(__file__))
        with open(Rpath + '/script.R','w') as f:
            f.write(self.inputspec)

        # Run R script
        cmd = ['Rscript',Rpath+'/script.R']
        r_output = subprocess.check_output(cmd, universal_newlines=True)
        print r_output

        self.results = {'output.txt': r_output }

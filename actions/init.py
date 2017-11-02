import os
from lib import action

class Init(action.BaseAction):
    def run(self, planpath, backend):
        os.chdir(planpath)
        return self.terraform.init(planpath, backend_config=backend)

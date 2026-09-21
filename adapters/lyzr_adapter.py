from adapters.base import AdapterContract
from agent import CodeMedic

class LyzrAdapter(AdapterContract):
    framework="lyzr"
    def run(self,path):
        return CodeMedic().inspect(path).to_dict()
    def verify(self,path):
        result=self.run(path)
        return {"framework":self.framework,"mode":"portable","verified":super().verify(path),"result":result}

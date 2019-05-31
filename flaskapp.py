from flask import Flask
from flask_restful import Resource, Api
from flask import request
import os
import subprocess
app = Flask(__name__)
api = Api(app, prefix="/api/v1")
class aeo_cmVmStop(Resource):
    def get(self, vmname):
        if vmname not in ("aeo-cmappn-02", "aeo-cmdpsn-02", "aeo-cmirrn-02", "aeo-cmnacn-02 "):
            response="This VM doesn't comes under the Designated VM's for cost cutting process"
            return {'Response': response}
        else:
            execution=self.execute_vmshell(vmname,'stop')
            if "was not found" in execution:
               response="Requested VM {} shutdown was not successful. VM does not Exist".format(vmname)
            else:
               response="Requested VM {} successfully stopped".format(vmname)
            return {'Response': response}
    def execute_vmshell(self,vmname,arg3):
        #cmd = 'sh k8s_vmwise_start_stop.sh {} {}'.format(vmname,arg3)
        #command=os.popen(cmd).read()
        p = subprocess.Popen(["sh", "aeo_cm_mw_vmwise_start_stop.sh", vmname, arg3], stdout=subprocess.PIPE, stderr = subprocess.STDOUT)
        stdout, stderr= p.communicate()
        return stderr
class aeo_cmVmStart(Resource):
    def get(self, vmname):
        if vmname not in ("aeo-cmappn-02", "aeo-cmdpsn-02", "aeo-cmirrn-02", "aeo-cmnacn-02 "):
            response="This VM doesn't comes under the Designated VM's for cost cutting process"
            return {'Response': response}
        else:
            execution=obj_aeo_cmVmStop.execute_vmshell(vmname,'start')
            if "was not found" in execution:
               response="Requested VM {} startup was not successful. The VM doesn't exist".format(vmname)
            else:
               response="Requested VM {} was successfully started".format(vmname)
            return {'Response': response}
api.add_resource(aeo_cmVmStop, '/aeocm/stop/<vmname>')
api.add_resource(aeo_cmVmStart, '/aeocm/start/<vmname>')
obj_aeo_cmVmStop=aeo_cmVmStop()
if __name__ == '__main__':
    #app.run(host='0.0.0.0',debug=True)
     app.run(debug=True, port=5001)

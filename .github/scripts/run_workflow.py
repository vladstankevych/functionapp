import sys
from cpfr.deploy.basic_actions import BasicActions

for i in sys.argv:
    print(i)

if sys.argv[2] == "false":
    response, run_id = BasicActions().run_workflow(workflow_name=sys.argv[1])
else:
    response, run_id = BasicActions().run_workflow(job_id=sys.argv[1])

print(f"Ran workflow with run_id: {response}")
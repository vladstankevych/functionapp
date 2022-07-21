import sys
from cpfr.deploy.basic_actions import BasicActions

if not sys.argv[2]:
    response, run_id = BasicActions().run_workflow(workflow_name=sys.argv[1])
else:
    response, run_id = BasicActions().run_workflow(job_id=sys.argv[1])

print(f"Ran workflow with run_id: {response}")
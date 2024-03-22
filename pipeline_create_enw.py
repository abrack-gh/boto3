import stepfunctions
import aws_cdk.aws_lambda as lambda_
import aws_cdk.aws_stepfunctions as sfn

from stepfunctions.steps import *
from stepfunctions.workflow import *

# def buildWorkflow():

#     start_pass_state = Pass(state_id="Hello World")
#     basic_path = Chain([start_pass_state])

#     basic_workflow = Workflow(
#         name="MyWorkflow_Simple", definition=basic_path, role="arn:aws:s3:us-east-1:536869379274:reur8eu8",
#     )

#     basic_workflow.render_graph()
#     print(basic_workflow.definition.to_json(pretty=True))
    
#     return basic_workflow

# buildWorkflow()
def passWorkflow():
        
        start_pass_state = Pass(state_id="Goodbye World!", )
        next_pass_state = Pass(state_id="Goodbye Pt 2")
        last_pass_state = Pass(state_id="Last", comment="Last one")
        
        
        lambdaState = LambdaStep(
            state_id="Runs this lambda",
            parameters={
                "FunctionName": "<lambda_fn_name>",
                "Payload": {"input": "Hello World!"},
                
            }
        )
        
        chain_path = Chain([start_pass_state, next_pass_state, lambdaState ,last_pass_state])
        
        workflow = Workflow(
            name="Workflow", definition=chain_path, role="arn:aws:s3:::wfjeorgerjogerigreigo", timeout_seconds=300, type=Choice
        )
    
        
        workflow.render_graph()
        print(workflow.definition.to_json(pretty=True))
        
        return workflow

passWorkflow()
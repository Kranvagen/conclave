import sys
import json
from conclave.lang import *
from conclave.utils import *
from conclave import workflow



def protocol():

    # step one: define input relations
    dataset_one = [
        defCol('SSN', 'INTEGER', [1]),
        defCol('Zip_Code', 'INTEGER', [1])
    ]

    dataset_two = [
        defCol('SSN', 'INTEGER', [2]),
        defCol('Income', 'INTEGER', [2])
    ]


    dataset_three = [   defCol('SSN', 'INTEGER' ,[2]) ,  defCol('Niklas' , 'INTEGER', [2] ) ]
    
    # step two: convert input relations to Create nodes
    in1 = create("in1", dataset_one, {1})
    in2 = create("in2", dataset_two, {2})
    in3 = create("in3" , dataset_three,{2})
    
    # step 3: define operations over data
    pro = project(in1 , 'pro' , [ 'Zip_Code', 'SSN'] )
    pro2 = project(in2 , 'pro2' , [ 'Income', 'SSN'] )
    pro3 = join( in2 , in3 , 'pro3' , ['SSN'] , ['SSN'])




    # step 4: reveal result to a party and return root nodes of the DAG

    collect(pro3,2)
    return {in1, in2}
    
if __name__ == "__main__":
    with open(sys.argv[1], "r") as c:
        c = json.load(c)

    workflow.run(protocol, c, mpc_framework="jiff", apply_optimisations=True)

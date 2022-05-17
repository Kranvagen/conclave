import sys
import json
from conclave.lang import *
from conclave.utils import *
from conclave import workflow


def protocol():

	cols_in_one = [
		defCol("car_id", "INTEGER", [1]),
		defCol("location", "INTEGER", [1])
	]
	in_one = create("in1", cols_in_one, {1})

	cols_in_two = [
		defCol("car_id", "INTEGER", [1]),
		defCol("location", "INTEGER", [1])
	]
	in_two = create("in2", cols_in_two, {1})

	cols_in_three = [
		defCol("car_id", "INTEGER", [1]),
		defCol("location", "INTEGER", [1])
	]
	in_three = create("in3", cols_in_three, {1})

	combined = concat([in_one, in_two, in_three], "combined_data")
	agged = aggregate_count(combined, "heatmap", ["location"], "by_location")
	collect(agged, 1)

	return {in_one, in_two, in_three}


if __name__ == "__main__":

	with open(sys.argv[1], "r") as c:
		c = json.load(c)

	workflow.run(protocol, c, mpc_framework="jiff", apply_optimisations=True)

from conclave.codegen.libs.python import *

if __name__ == "__main__":
    print("start python")
    in2 = read_rel('/home/kali/Desktop/myconclave/conclave/demo/data/in2.csv')
    pro2 = project(in2, [1, 0])
    write_rel('/home/kali/Desktop/myconclave/conclave/demo/data', 'pro2.csv', pro2, '"Income","SSN"')

    print("done python")

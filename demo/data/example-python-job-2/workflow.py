from conclave.codegen.libs.python import *

if __name__ == "__main__":
    print("start python")
    in2 = read_rel('/home/kali/Desktop/myconclave/conclave/demo/data/in2.csv')
    in3 = read_rel('/home/kali/Desktop/myconclave/conclave/demo/data/in3.csv')
    pro3  = join(in2, in3, 0, 0)
    write_rel('/home/kali/Desktop/myconclave/conclave/demo/data', 'pro3.csv', pro3, '"SSN","Income","Niklas"')

    print("done python")

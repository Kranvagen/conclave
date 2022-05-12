from conclave.codegen.libs.python import *

if __name__ == "__main__":
    print("start python")
    in1 = read_rel('/home/kali/Desktop/myconclave/conclave/demo/data/in1.csv')
    pro = project(in1, [1, 0])
    write_rel('/home/kali/Desktop/myconclave/conclave/demo/data', 'pro.csv', pro, '"Zip_Code","SSN"')

    print("done python")

import pandas as pd
import os

# get saf.proto file form SAF_example_HOUSE_metric_ZYX_220.xlsx

def replace_str(x:str):
    reslut = ""
    re = x.find('[')
    if(re >=0 ):
        x = x.split('[')[0][:-1]
    return x.replace(" ", "_").replace("-", "_").lower()

def main():
    
    example_path = os.path.join(os.path.dirname(\
    os.path.dirname(os.path.realpath(__file__))), "examples")
    test_saf = os.path.join(example_path, "SAF_example_HOUSE_metric_ZYX_220.xlsx")

    # read all sheet execl file into a dataframe
    saf = pd.read_excel(test_saf, sheet_name=None)
    # list all sheets
    print(saf.keys())

    proto_file = r"// www.saf.guide"
    proto_file += "\n"
    proto_file += r"// li chao, 252429238@qq.com"
    proto_file += "\n"
    proto_file += "syntax = \"proto3\";"
    proto_file += "\n"
    proto_file += "import \"google/protobuf/timestamp.proto\";"
    proto_file += "\n"
    # proto_file += "import \"define.proto\";"
    proto_file += "\n"
    proto_file += r"package saf;"
    proto_file += "\n"
    proto_file += "\n"
    saf_proto = "message SAF {\n"  

    index_i = 1
    for sheet in saf.keys():
        proto_file += ("message " + sheet.replace("Structural", "") + " {\n")
        sheet_pd = None
        if saf[sheet].columns.size <3:
            saf_proto += ("    " + sheet.replace("Structural", "") + " " + replace_str(sheet) + " = " + str(index_i) + ";\n")
            sheet_pd = pd.read_excel(test_saf, sheet_name=sheet, index_col= 0, header=None)
            sheet_pd = sheet_pd.transpose()
        else:
            saf_proto += ("    repeated " + sheet.replace("Structural", "") + " " + replace_str(sheet) + " = " + str(index_i) + ";\n")
            sheet_pd = pd.read_excel(test_saf, sheet_name=sheet)
        index =1
        for column in sheet_pd.columns:
            proto_file += ("    "+ str(sheet_pd[column].dtype) + " " + replace_str(column) + " = " + str(index) + ";\n")
            index += 1
        proto_file += "}\n"
        index_i += 1
    
    saf_proto += "}\n"

    proto_file = proto_file.replace("float64", "double")
    proto_file = proto_file.replace("int64", "double")
    proto_file = proto_file.replace("object", "string")
    proto_file = proto_file.replace("(x;y;z)", "")
    proto_file = proto_file.replace("repeat_(n)", "repeat")
    proto_file = proto_file.replace("2d_member", "member_2d")
    proto_file = proto_file.replace("1d_member", "member_1d")
    proto_file = proto_file.replace("datetime64[ns]", "string")

    # proto_file = proto_file.replace("string lcs_of_cross_section","LcsOfCrossSection lcs_of_cross_section")
    # proto_file = proto_file.replace("string system_of_units","SystemOfUnits system_of_units")
    # proto_file = proto_file.replace("string cross_section_type","CrossSectionType cross_section_type")
    # proto_file = proto_file.replace("string shape","Shape shape")
    # proto_file = proto_file.replace("string system_line","Alignment system_line")
    # proto_file = proto_file.replace("string alignment","Alignment alignment")
    # proto_file = proto_file.replace("string lcs ","LCS lcs ")
    proto_file = proto_file.replace("double parent_id ","string parent_id ")
    # proto_file = proto_file.replace("double form_code ","FormCode form_code ")
    # proto_file = proto_file.replace("string type_of_connection ","TypeOfConnection type_of_connection ")
    # proto_file = proto_file.replace("string system_plane_at ","SystemPlaneAt system_plane_at ")
    # proto_file = proto_file.replace("string thickness_type ","ThicknesType thickness_type ")
    # proto_file = proto_file.replace("string lcs_type ","LCSType lcs_type ") 


    proto_file +=  "\n"
    proto_file +=  saf_proto

    # write proto file
    file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), r"proto\saf.proto")
    file = open(file, "w")
    file.write(proto_file)
    file.close()


if __name__ == '__main__':
    main()   
    print("done")
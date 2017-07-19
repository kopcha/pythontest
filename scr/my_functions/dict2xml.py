import dicttoxml
from collections import OrderedDict

data_dict = OrderedDict([("@productNumber", "CXP9021234_20"),
                         ("@RState", "R7A"),
                         ("@functionDesignation", "My UP product")])
data_dict_new = OrderedDict([("ProductLevel2", data_dict)])


def demo_dicttoxml():
    data_xml = dicttoxml.dicttoxml(data_dict_new, custom_root="ProductLevel1", attr_type=False)
    ready_xml = data_xml.decode("utf-8")
    print(ready_xml)
    return ready_xml


def flush_to_file(file_path, data):
    with open(file_path, 'w') as output:
        output.write(data)
    return

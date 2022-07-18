import mimetypes, os, requests, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'greaterwms.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()
from django.conf import settings
import pandas as pd
from pathlib import Path

mimetypes.add_type("text/css", ".css", True)
mimetypes.add_type("text/javascript", ".js", True)

win32_folder = os.path.exists(os.path.join(settings.BASE_DIR, 'media/' + "/win32"))
linux_folder = os.path.exists(os.path.join(settings.BASE_DIR, 'media/' + "/linux"))
darwin_folder = os.path.exists(os.path.join(settings.BASE_DIR, 'media/' + "/darwin"))
upload_folder = os.path.exists(os.path.join(settings.BASE_DIR, 'media/' + "/upload_example"))
if not win32_folder:
    os.makedirs(os.path.join(settings.BASE_DIR, 'media/' + "/win32"))
if not linux_folder:
    os.makedirs(os.path.join(settings.BASE_DIR, 'media/' + "/linux"))
if not darwin_folder:
    os.makedirs(os.path.join(settings.BASE_DIR, 'media/' + "/darwin"))
if not upload_folder:
    os.makedirs(os.path.join(settings.BASE_DIR, 'media/' + "/upload_example"))

customer_cn_path = os.path.join(settings.BASE_DIR, 'media/' + "/upload_example/customer_cn.xlsx")
customer_en_path = os.path.join(settings.BASE_DIR, 'media/' + "/upload_example/customer_en.xlsx")
goodslist_cn_path = os.path.join(settings.BASE_DIR, 'media/' + "/upload_example/goodslist_cn.xlsx")
goodslist_en_path = os.path.join(settings.BASE_DIR, 'media/' + "/upload_example/goodslist_en.xlsx")
supplier_cn_path = os.path.join(settings.BASE_DIR, 'media/' + "/upload_example/supplier_cn.xlsx")
supplier_en_path = os.path.join(settings.BASE_DIR, 'media/' + "/upload_example/supplier_en.xlsx")
customer_cn_file = os.path.exists(customer_cn_path)
customer_en_file = os.path.exists(customer_en_path)
goodslist_cn_file = os.path.exists(goodslist_cn_path)
goodslist_en_file = os.path.exists(goodslist_en_path)
supplier_cn_file = os.path.exists(supplier_cn_path)
supplier_en_file = os.path.exists(supplier_en_path)
if not customer_cn_file:
    customer_cn = pd.DataFrame({"客户名称": [], "客户城市": [] ,"详细地址": [], "联系电话": [], "负责人": [], "客户等级": []})
    df = customer_cn.set_index("客户名称")
    df.to_excel(customer_cn_path)

if not customer_en_file:
    customer_en = pd.DataFrame({"Customer Name": [], "Customer City": [], "Customer Address": [], "Customer Contact": [], "Customer Manager": [], "Customer Level": []})
    df = customer_en.set_index("Customer Name")
    df.to_excel(customer_en_path)

if not goodslist_cn_file:
    goodslist_cn = pd.DataFrame({"商品编码": [], "商品描述": [], "商品供应商": [], "商品单位重量": [], "商品单位长度": [], "商品单位宽度": [], "商品单位高度": [],  "最小单位体积": [], "商品单位": [], "商品类别": [], "商品品牌": [], "商品颜色": [], "商品形状": [], "商品规格": [], "商品产地": [], "商品成本": [], "商品价格": []})
    df = goodslist_cn.set_index("商品编码")
    df.to_excel(goodslist_cn_path)

if not goodslist_en_file:
    goodslist_en = pd.DataFrame({"Goods Code": [], "Goods Description": [], "Goods Supplier": [], "Goods Weight": [], "Goods Width": [], "Goods Depth": [], "Goods Height": [],  "Unit Volume": [], "Goods Unit": [], "Goods Class": [], "Goods Brand": [], "Goods Color": [], "Goods Shape": [], "Goods Specs": [], "Goods Origin": [], "Goods Cost": [], "Goods Price": []})
    df = goodslist_en.set_index("Goods Code")
    df.to_excel(goodslist_en_path)

if not supplier_cn_file:
    supplier_cn = pd.DataFrame({"供应商名称": [], "供应商城市": [] ,"详细地址": [], "联系电话": [], "负责人": [], "供应商等级": []})
    df = supplier_cn.set_index("供应商名称")
    df.to_excel(supplier_cn_path)

if not supplier_en_file:
    supplier_en = pd.DataFrame({"Supplier Name": [], "Supplier City": [] ,"Supplier Address": [], "Supplier Contact": [], "Supplier Manager": [], "Supplier Level": []})
    df = supplier_en.set_index("Supplier Name")
    df.to_excel(supplier_en_path)

print('Welcome To GreaterWMS')

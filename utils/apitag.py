import re

def api_tags(data):
    lang = re.findall(r'zh-CN', str(data), re.IGNORECASE)
    if lang:
        return [
        {
            "name": "asn",
            "description": "到货通知书"
        },
        {
            "name": "binproperty",
            "description": "库位属性"
        },
        {
            "name": "binset",
            "description": "库位设置"
        },
        {
            "name": "binsize",
            "description": "库位尺寸"
        },
        {
            "name": "capital",
            "description": "固定资产"
        },
        {
            "name": "chat",
            "description": "即时聊天"
        },
        {
            "name": "company",
            "description": "公司信息"
        },
        {
            "name": "customer",
            "description": "客户信息"
        },
        {
            "name": "cyclecount",
            "description": "动态盘点"
        },
        {
            "name": "dashboard",
            "description": "仪表盘"
        },
        {
            "name": "dn",
            "description": "发货单"
        },
        {
            "name": "driver",
            "description": "司机信息"
        },
        {
            "name": "goods",
            "description": "商品信息"
        },
        {
            "name": "goodsbrand",
            "description": "商品品牌"
        },
        {
            "name": "goodsclass",
            "description": "商品类别"
        },
        {
            "name": "goodscolor",
            "description": "商品颜色"
        },
        {
            "name": "goodsorigin",
            "description": "商品产地"
        },
        {
            "name": "goodsshape",
            "description": "商品形状"
        },
        {
            "name": "goodsspecs",
            "description": "商品规格"
        },
        {
            "name": "goodsunit",
            "description": "商品单位"
        },
        {
            "name": "payment",
            "description": "费用支出"
        },
        {
            "name": "scanner",
            "description": "扫描PDA"
        },
        {
            "name": "shopid",
            "description": "电商扩展"
        },
        {
            "name": "staff",
            "description": "员工信息"
        },
        {
            "name": "stock",
            "description": "库存信息"
        },
        {
            "name": "supplier",
            "description": "供应商信息"
        },
        {
            "name": "uploadfile",
            "description": "上传中心"
        },
        {
            "name": "warehouse",
            "description": "仓库信息"
        }
    ]
    else:
        return [
        {
            "name": "asn",
            "description": "Arrive Manifest"
        },
        {
            "name": "binproperty",
            "description": "Bin Property"
        },
        {
            "name": "binset",
            "description": "Bin Set"
        },
        {
            "name": "binsize",
            "description": "Bin Size"
        },
        {
            "name": "capital",
            "description": "Capital"
        },
        {
            "name": "chat",
            "description": "Chat"
        },
        {
            "name": "company",
            "description": "Company Info"
        },
        {
            "name": "customer",
            "description": "Customer Info"
        },
        {
            "name": "cyclecount",
            "description": "Cycle Count"
        },
        {
            "name": "dashboard",
            "description": "Dashboard"
        },
        {
            "name": "dn",
            "description": "Shipping Notice"
        },
        {
            "name": "driver",
            "description": "Driver Info"
        },
        {
            "name": "goods",
            "description": "Goods List"
        },
        {
            "name": "goodsbrand",
            "description": "Goods Brand"
        },
        {
            "name": "goodsclass",
            "description": "Goods Class"
        },
        {
            "name": "goodscolor",
            "description": "Goods Color"
        },
        {
            "name": "goodsorigin",
            "description": "Goods Origin"
        },
        {
            "name": "goodsshape",
            "description": "Goods Shape"
        },
        {
            "name": "goodsspecs",
            "description": "Goods Specs"
        },
        {
            "name": "goodsunit",
            "description": "Goods Unit"
        },
        {
            "name": "payment",
            "description": "Payment"
        },
        {
            "name": "scanner",
            "description": "Scanner PDA"
        },
        {
            "name": "shopid",
            "description": "E-comments"
        },
        {
            "name": "staff",
            "description": "Staff Info"
        },
        {
            "name": "stock",
            "description": "Stock Info"
        },
        {
            "name": "supplier",
            "description": "Supplier Info"
        },
        {
            "name": "uploadfile",
            "description": "Upload Center"
        },
        {
            "name": "warehouse",
            "description": "Warehouse Info"
        }
    ]
from django.http import JsonResponse
from userprofile.models import Users
from userprofile import serializers
from utils.fbmsg import FBMsg
from utils.md5 import Md5
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib import auth
from django.utils import timezone
from django.contrib.auth.models import User
from staff.models import ListModel as staff
import json
import random

def randomPhone():
    List = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139",
               "147", "150", "151", "152", "153", "155", "156", "157", "158", "159",
               "186", "187", "188", "189"]
    return (random.choice(List) + "".join(random.choice("0123456789") for i in range(8)))

randomcity = ["shanghai", "nanjing", "hangzhou", "beijing", "chongqing", "shenzhen", "guangzhou", "suzhou", "hefei",
                "chengdu", "kunming", "wuhan"]

randomcolor = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Purple"]

randomclass = ["Electronics", "Computers", "Smart Home", "Arts & Crafts", "Automotive", "Baby", "Health", "Kitchen",
               "Industrial", "Luggage", "Movies", "Software"]

randomunit = ["Box", "Package", "Piece", "Pallet"]

randomname = ["Aaron", "Abbott", "Abel", "Baird", "Baldwin", "Bancroft", "Caesar", "Calvin", "Camille", "chengdu",
              "Daisy", "Dale", "Dana", "Earl", "Eartha", "Ed", "Fabian", "Faithe", "Fanny", "Gabriel", "Gabrielle",
              "Gail", "Hale", "Haley", "Hamiltion", "Ian", "Ida", "Ina", "Jack", "Jacob", "Jacqueline", "Kama",
              "Karen", "Katherine", "Lambert", "Lance", "Larry", "Mabel", "Madeline", "Madge", "Nancy", "Naomi",
              "Nat", "Octavia", "Odelette", "Odelia", "Paddy", "Pag", "Page", "Queena", "Quennel", "Quentin",
              "Rachel", "Rae", "Ralap", "Sabina", "Sabrina", "Sally", "Tab", "Tabitha", "Tammy", "Ula", "Ulysses",
              "Una", "Valentina", "Valentine", "Valentine", "Wade", "Walker", "Wallis", "Xanthe", "Xavier", "Xaviera",
              "Yale", "Yedda", "Yehudi", "Zachary", "Zebulon", "Zenobia"
            ]

randomshape = ["Square", "Rectangle", "Cone", "Cylinder", "Irregular"]

randomspecs = ["1 x 10", "3 x 3", "5 x 5", "6 x 6"]

def randomStaffType():
    List = ["Manager", "Supplier", "Customer", "Receiver", "Shipper", "Worker", "Supervisor", "Leader", "Projector"]
    return (random.choice(List))

randombinproperty = ["Normal", "Holding", "Damage", "Inspection"]

randombinsize = ["Big", "Floor", "Tiny", "Small"]

@method_decorator(csrf_exempt, name='dispatch')
def register(request, *args, **kwargs):
    post_data = json.loads(request.body.decode())
    data = {
        "name": post_data.get('name'),
        "password1": post_data.get('password1'),
        "password2": post_data.get('password2')
    }
    ip = request.META.get('HTTP_X_FORWARDED_FOR') if request.META.get(
        'HTTP_X_FORWARDED_FOR') else request.META.get('REMOTE_ADDR')
    if Users.objects.filter(name=str(data['name']), developer=1, is_delete=0).exists():
        err_user_same = FBMsg.err_user_same()
        err_user_same['ip'] = ip
        err_user_same['data'] = data['name']
        return JsonResponse(err_user_same)
    else:
        if data.get('password1') is None:
            err_password1_empty = FBMsg.err_password1_empty()
            err_password1_empty['ip'] = ip
            err_password1_empty['data'] = data['name']
            return JsonResponse(err_password1_empty)
        else:
            if str(data['password1']) == '':
                err_password1_empty = FBMsg.err_password1_empty()
                err_password1_empty['ip'] = ip
                err_password1_empty['data'] = data['name']
                return JsonResponse(err_password1_empty)
            else:
                if data.get('password2') is None:
                    err_password2_empty = FBMsg.err_password2_empty()
                    err_password2_empty['ip'] = ip
                    err_password2_empty['data'] = data['name']
                    return JsonResponse(err_password2_empty)
                else:
                    if str(data['password2']) == '':
                        err_password2_empty = FBMsg.err_password2_empty()
                        err_password2_empty['ip'] = ip
                        err_password2_empty['data'] = data['name']
                        return JsonResponse(err_password2_empty)
                    else:
                        if str(data['password1']) != str(data['password2']):
                            err_password_not_same = FBMsg.err_password_not_same()
                            err_password_not_same['ip'] = ip
                            err_password_not_same['data'] = data['name']
                            return JsonResponse(err_password_not_same)
                        else:
                            transaction_code = Md5.md5(data['name'])
                            user = User.objects.create_user(username=str(data['name']),
                                                            password=str(data['password1']))
                            Users.objects.create(user_id=user.id, name=str(data['name']),
                                                 openid=transaction_code, appid=Md5.md5(data['name'] + '1'),
                                                 t_code=Md5.md5(str(timezone.now())),
                                                 developer=1, ip=ip)
                            auth.login(request, user)
                            staff.objects.create(staff_name=str(data['name']), staff_type='admin', openid=transaction_code)
                            ret = FBMsg.ret()
                            ret['ip'] = ip
                            data['openid'] = transaction_code
                            data['name'] = str(data['name'])
                            data.pop('password1', '')
                            data.pop('password2', '')
                            ret['data'] = data
                            from company.models import ListModel as company
                            company_data = [
                                company(openid=transaction_code,
                                        company_name='GreaterWMS',
                                        company_city=str(random.choice(randomcity)),
                                        company_address='People’s Square # 666 Room 1F',
                                        company_contact=int(randomPhone()),
                                        company_manager='Elvis.Shi',
                                        creater='GreaterWMS-DemoData'
                                        )
                            ]
                            company.objects.bulk_create(company_data, batch_size=100)
                            from warehouse.models import ListModel as warehouse
                            warehouse_data = [
                                warehouse(openid=transaction_code,
                                          warehouse_name='Center Warehouse',
                                          warehouse_city=str(random.choice(randomcity)),
                                          warehouse_address='People’s Square # 666 Room 2F',
                                          warehouse_contact=int(randomPhone()),
                                          warehouse_manager='Tim.Yao',
                                          creater='GreaterWMS-DemoData'
                                          )
                            ]
                            warehouse.objects.bulk_create(warehouse_data, batch_size=100)
                            from supplier.models import ListModel as supplier
                            supplier_data_list = []
                            for supplier_data in range(1, 97):
                                demo_data = supplier(openid=transaction_code,
                                                     supplier_name='Demo Supplier Name-' + str(supplier_data),
                                                     supplier_city=str(random.choice(randomcity)),
                                                     supplier_address='Demo Address-' + str(supplier_data),
                                                     supplier_contact=int(randomPhone()),
                                                     supplier_manager=str(random.choice(randomname)),
                                                     creater='GreaterWMS-DemoData'
                                                     )
                                supplier_data_list.append(demo_data)
                            supplier.objects.bulk_create(supplier_data_list, batch_size=100)
                            from customer.models import ListModel as customer
                            customer_data_list = []
                            for customer_data in range(1, 97):
                                demo_data = customer(openid=transaction_code,
                                                     customer_name='Demo Customer Name-' + str(customer_data),
                                                     customer_city=str(random.choice(randomcity)),
                                                     customer_address='Demo Address-' + str(customer_data),
                                                     customer_contact=int(randomPhone()),
                                                     customer_manager=str(random.choice(randomname)),
                                                     creater='GreaterWMS-DemoData'
                                                     )
                                customer_data_list.append(demo_data)
                            customer.objects.bulk_create(customer_data_list, batch_size=100)
                            staff_data_list = []
                            for staff_data in randomname:
                                demo_data = staff(openid=transaction_code,
                                                  staff_name=staff_data,
                                                  staff_type=str(randomStaffType())
                                                  )
                                staff_data_list.append(demo_data)
                            staff.objects.bulk_create(staff_data_list, batch_size=100)
                            from driver.models import ListModel as driver
                            driver_data_list = []
                            for driver_data in range(1, 97):
                                demo_data = driver(openid=transaction_code,
                                                   driver_name='Demo Driver Name-' + str(driver_data),
                                                   license_plate="".join(random.choice("0123456789") for i in range(8)),
                                                   creater='GreaterWMS-DemoData'
                                                   )
                                driver_data_list.append(demo_data)
                            driver.objects.bulk_create(driver_data_list, batch_size=100)
                            from capital.models import ListModel as capital
                            capital_data_list = []
                            for capital_data in range(1, 97):
                                demo_data = capital(openid=transaction_code,
                                                    capital_name='Demo Capital Name-' + str(capital_data),
                                                    capital_qty=random.randint(1, 100),
                                                    capital_cost=random.randint(100, 10000),
                                                    creater='GreaterWMS-DemoData'
                                                    )
                                capital_data_list.append(demo_data)
                            capital.objects.bulk_create(capital_data_list, batch_size=100)
                            from binsize.models import ListModel as binsize
                            binsize_data_list = [
                                binsize(openid=transaction_code,
                                        bin_size='Big',
                                        bin_size_w=1100,
                                        bin_size_d=1200,
                                        bin_size_h=1800,
                                        creater='GreaterWMS-DemoData'
                                        ),
                                binsize(openid=transaction_code,
                                        bin_size='Floor',
                                        bin_size_w=10000,
                                        bin_size_d=10000,
                                        bin_size_h=10000,
                                        creater='GreaterWMS-DemoData'
                                        ),
                                binsize(openid=transaction_code,
                                        bin_size='Small',
                                        bin_size_w=800,
                                        bin_size_d=1000,
                                        bin_size_h=1200,
                                        creater='GreaterWMS-DemoData'
                                        ),
                                binsize(openid=transaction_code,
                                        bin_size='Tiny',
                                        bin_size_w=200,
                                        bin_size_d=250,
                                        bin_size_h=300,
                                        creater='GreaterWMS-DemoData'
                                        )
                            ]
                            binsize.objects.bulk_create(binsize_data_list, batch_size=100)
                            from binset.models import ListModel as binset
                            binset_data_list = [
                                binset(openid=transaction_code,
                                       bin_name='A010101',
                                       bin_size=str(random.choice(randombinsize)),
                                       bin_property="Normal",
                                       empty_label=True,
                                       creater='GreaterWMS-DemoData'
                                       ),
                                binset(openid=transaction_code,
                                       bin_name='A010102',
                                       bin_size=str(random.choice(randombinsize)),
                                       bin_property="Normal",
                                       empty_label=True,
                                       creater='GreaterWMS-DemoData'
                                       ),
                                binset(openid=transaction_code,
                                       bin_name='A010103',
                                       bin_size=str(random.choice(randombinsize)),
                                       bin_property="Normal",
                                       empty_label=True,
                                       creater='GreaterWMS-DemoData'
                                       ),
                                binset(openid=transaction_code,
                                       bin_name='A010201',
                                       bin_size=str(random.choice(randombinsize)),
                                       bin_property="Normal",
                                       empty_label=True,
                                       creater='GreaterWMS-DemoData'
                                       ),
                                binset(openid=transaction_code,
                                       bin_name='A010202',
                                       bin_size=str(random.choice(randombinsize)),
                                       bin_property="Normal",
                                       empty_label=True,
                                       creater='GreaterWMS-DemoData'
                                       ),
                                binset(openid=transaction_code,
                                       bin_name='A010203',
                                       bin_size=str(random.choice(randombinsize)),
                                       bin_property="Normal",
                                       empty_label=True,
                                       creater='GreaterWMS-DemoData'
                                       ),
                                binset(openid=transaction_code,
                                       bin_name='A010301',
                                       bin_size=str(random.choice(randombinsize)),
                                       bin_property="Normal",
                                       empty_label=True,
                                       creater='GreaterWMS-DemoData'
                                       ),
                                binset(openid=transaction_code,
                                       bin_name='A010302',
                                       bin_size=str(random.choice(randombinsize)),
                                       bin_property="Normal",
                                       empty_label=True,
                                       creater='GreaterWMS-DemoData'
                                       ),
                                binset(openid=transaction_code,
                                       bin_name='A010303',
                                       bin_size=str(random.choice(randombinsize)),
                                       bin_property="Normal",
                                       empty_label=True,
                                       creater='GreaterWMS-DemoData'
                                       ),
                                binset(openid=transaction_code,
                                       bin_name='A020101',
                                       bin_size=str(random.choice(randombinsize)),
                                       bin_property="Normal",
                                       empty_label=True,
                                       creater='GreaterWMS-DemoData'
                                       ),
                                binset(openid=transaction_code,
                                       bin_name='A020102',
                                       bin_size=str(random.choice(randombinsize)),
                                       bin_property="Normal",
                                       empty_label=True,
                                       creater='GreaterWMS-DemoData'
                                       ),
                                binset(openid=transaction_code,
                                       bin_name='A020103',
                                       bin_size=str(random.choice(randombinsize)),
                                       bin_property="Normal",
                                       empty_label=True,
                                       creater='GreaterWMS-DemoData'
                                       ),
                                binset(openid=transaction_code,
                                       bin_name='A020201',
                                       bin_size=str(random.choice(randombinsize)),
                                       bin_property="Normal",
                                       empty_label=True,
                                       creater='GreaterWMS-DemoData'
                                       ),
                                binset(openid=transaction_code,
                                       bin_name='A020202',
                                       bin_size=str(random.choice(randombinsize)),
                                       bin_property="Normal",
                                       empty_label=True,
                                       creater='GreaterWMS-DemoData'
                                       ),
                                binset(openid=transaction_code,
                                       bin_name='A020203',
                                       bin_size=str(random.choice(randombinsize)),
                                       bin_property="Normal",
                                       empty_label=True,
                                       creater='GreaterWMS-DemoData'
                                       ),
                                binset(openid=transaction_code,
                                       bin_name='A030101',
                                       bin_size=str(random.choice(randombinsize)),
                                       bin_property="Normal",
                                       empty_label=True,
                                       creater='GreaterWMS-DemoData'
                                       ),
                                binset(openid=transaction_code,
                                       bin_name='A030102',
                                       bin_size=str(random.choice(randombinsize)),
                                       bin_property="Normal",
                                       empty_label=True,
                                       creater='GreaterWMS-DemoData'
                                       ),
                                binset(openid=transaction_code,
                                       bin_name='A030103',
                                       bin_size=str(random.choice(randombinsize)),
                                       bin_property="Normal",
                                       empty_label=True,
                                       creater='GreaterWMS-DemoData'
                                       ),
                                binset(openid=transaction_code,
                                       bin_name='A030201',
                                       bin_size=str(random.choice(randombinsize)),
                                       bin_property="Normal",
                                       empty_label=True,
                                       creater='GreaterWMS-DemoData'
                                       ),
                                binset(openid=transaction_code,
                                       bin_name='A030202',
                                       bin_size=str(random.choice(randombinsize)),
                                       bin_property="Normal",
                                       empty_label=True,
                                       creater='GreaterWMS-DemoData'
                                       ),
                                binset(openid=transaction_code,
                                       bin_name='A030203',
                                       bin_size=str(random.choice(randombinsize)),
                                       bin_property="Normal",
                                       empty_label=True,
                                       creater='GreaterWMS-DemoData'
                                       ),
                                binset(openid=transaction_code,
                                       bin_name='A030301',
                                       bin_size=str(random.choice(randombinsize)),
                                       bin_property="Normal",
                                       empty_label=True,
                                       creater='GreaterWMS-DemoData'
                                       ),
                                binset(openid=transaction_code,
                                       bin_name='A030302',
                                       bin_size=str(random.choice(randombinsize)),
                                       bin_property="Normal",
                                       empty_label=True,
                                       creater='GreaterWMS-DemoData'
                                       ),
                                binset(openid=transaction_code,
                                       bin_name='A030303',
                                       bin_size=str(random.choice(randombinsize)),
                                       bin_property="Normal",
                                       empty_label=True,
                                       creater='GreaterWMS-DemoData'
                                       ),
                                binset(openid=transaction_code,
                                       bin_name='B010101',
                                       bin_size=str(random.choice(randombinsize)),
                                       bin_property="Inspection",
                                       empty_label=True,
                                       creater='GreaterWMS-DemoData'
                                       ),
                                binset(openid=transaction_code,
                                       bin_name='B010102',
                                       bin_size=str(random.choice(randombinsize)),
                                       bin_property="Inspection",
                                       empty_label=True,
                                       creater='GreaterWMS-DemoData'
                                       ),
                                binset(openid=transaction_code,
                                       bin_name='B010103',
                                       bin_size=str(random.choice(randombinsize)),
                                       bin_property="Inspection",
                                       empty_label=True,
                                       creater='GreaterWMS-DemoData'
                                       ),
                                binset(openid=transaction_code,
                                       bin_name='B010201',
                                       bin_size=str(random.choice(randombinsize)),
                                       bin_property="Inspection",
                                       empty_label=True,
                                       creater='GreaterWMS-DemoData'
                                       ),
                                binset(openid=transaction_code,
                                       bin_name='B010202',
                                       bin_size=str(random.choice(randombinsize)),
                                       bin_property="Inspection",
                                       empty_label=True,
                                       creater='GreaterWMS-DemoData'
                                       ),
                                binset(openid=transaction_code,
                                       bin_name='B010203',
                                       bin_size=str(random.choice(randombinsize)),
                                       bin_property="Inspection",
                                       empty_label=True,
                                       creater='GreaterWMS-DemoData'
                                       ),
                                binset(openid=transaction_code,
                                       bin_name='B010301',
                                       bin_size=str(random.choice(randombinsize)),
                                       bin_property="Inspection",
                                       empty_label=True,
                                       creater='GreaterWMS-DemoData'
                                       ),
                                binset(openid=transaction_code,
                                       bin_name='B010302',
                                       bin_size=str(random.choice(randombinsize)),
                                       bin_property="Inspection",
                                       empty_label=True,
                                       creater='GreaterWMS-DemoData'
                                       ),
                                binset(openid=transaction_code,
                                       bin_name='B010303',
                                       bin_size=str(random.choice(randombinsize)),
                                       bin_property="Inspection",
                                       empty_label=True,
                                       creater='GreaterWMS-DemoData'
                                       ),
                                binset(openid=transaction_code,
                                       bin_name='B020101',
                                       bin_size=str(random.choice(randombinsize)),
                                       bin_property="Holding",
                                       empty_label=True,
                                       creater='GreaterWMS-DemoData'
                                       ),
                                binset(openid=transaction_code,
                                       bin_name='B020102',
                                       bin_size=str(random.choice(randombinsize)),
                                       bin_property="Holding",
                                       empty_label=True,
                                       creater='GreaterWMS-DemoData'
                                       ),
                                binset(openid=transaction_code,
                                       bin_name='B020103',
                                       bin_size=str(random.choice(randombinsize)),
                                       bin_property="Holding",
                                       empty_label=True,
                                       creater='GreaterWMS-DemoData'
                                       ),
                                binset(openid=transaction_code,
                                       bin_name='B020201',
                                       bin_size=str(random.choice(randombinsize)),
                                       bin_property="Holding",
                                       empty_label=True,
                                       creater='GreaterWMS-DemoData'
                                       ),
                                binset(openid=transaction_code,
                                       bin_name='B020202',
                                       bin_size=str(random.choice(randombinsize)),
                                       bin_property="Holding",
                                       empty_label=True,
                                       creater='GreaterWMS-DemoData'
                                       ),
                                binset(openid=transaction_code,
                                       bin_name='B020203',
                                       bin_size=str(random.choice(randombinsize)),
                                       bin_property="Holding",
                                       empty_label=True,
                                       creater='GreaterWMS-DemoData'
                                       ),
                                binset(openid=transaction_code,
                                       bin_name='B030101',
                                       bin_size=str(random.choice(randombinsize)),
                                       bin_property="Damage",
                                       empty_label=True,
                                       creater='GreaterWMS-DemoData'
                                       ),
                                binset(openid=transaction_code,
                                       bin_name='B030102',
                                       bin_size=str(random.choice(randombinsize)),
                                       bin_property="Damage",
                                       empty_label=True,
                                       creater='GreaterWMS-DemoData'
                                       ),
                                binset(openid=transaction_code,
                                       bin_name='B030103',
                                       bin_size=str(random.choice(randombinsize)),
                                       bin_property="Damage",
                                       empty_label=True,
                                       creater='GreaterWMS-DemoData'
                                       ),
                                binset(openid=transaction_code,
                                       bin_name='B030201',
                                       bin_size=str(random.choice(randombinsize)),
                                       bin_property="Damage",
                                       empty_label=True,
                                       creater='GreaterWMS-DemoData'
                                       ),
                                binset(openid=transaction_code,
                                       bin_name='B030202',
                                       bin_size=str(random.choice(randombinsize)),
                                       bin_property="Damage",
                                       empty_label=True,
                                       creater='GreaterWMS-DemoData'
                                       ),
                                binset(openid=transaction_code,
                                       bin_name='B030203',
                                       bin_size=str(random.choice(randombinsize)),
                                       bin_property="Damage",
                                       empty_label=True,
                                       creater='GreaterWMS-DemoData'
                                       ),
                                binset(openid=transaction_code,
                                       bin_name='B030301',
                                       bin_size=str(random.choice(randombinsize)),
                                       bin_property="Damage",
                                       empty_label=True,
                                       creater='GreaterWMS-DemoData'
                                       ),
                                binset(openid=transaction_code,
                                       bin_name='B030302',
                                       bin_size=str(random.choice(randombinsize)),
                                       bin_property="Damage",
                                       empty_label=True,
                                       creater='GreaterWMS-DemoData'
                                       ),
                                binset(openid=transaction_code,
                                       bin_name='B030303',
                                       bin_size=str(random.choice(randombinsize)),
                                       bin_property="Damage",
                                       empty_label=True,
                                       creater='GreaterWMS-DemoData'
                                       )
                            ]
                            binset.objects.bulk_create(binset_data_list, batch_size=100)
                            from goodsunit.models import ListModel as goodsunit
                            demo_data = []
                            for goods_unit in randomunit:
                                demo_data.append(goodsunit(openid=transaction_code, goods_unit=goods_unit,
                                                            creater='GreaterWMS-DemoData'))
                            goodsunit.objects.bulk_create(demo_data, batch_size=100)
                            from goodsclass.models import ListModel as goodsclass
                            demo_data = []
                            for goods_class in randomclass:
                                demo_data.append(goodsclass(openid=transaction_code, goods_class=goods_class,
                                                            creater='GreaterWMS-DemoData'))
                            goodsclass.objects.bulk_create(demo_data, batch_size=100)
                            from goodscolor.models import ListModel as goodscolor
                            demo_data = []
                            for goods_color in randomcolor:
                                demo_data.append(goodscolor(openid=transaction_code, goods_color=goods_color,
                                                            creater='GreaterWMS-DemoData'))
                            goodscolor.objects.bulk_create(demo_data, batch_size=100)
                            from goodsbrand.models import ListModel as goodsbrand
                            goodsbrand_data_list = []
                            for goodsbrand_data in range(1, 97):
                                demo_data = goodsbrand(openid=transaction_code,
                                                       goods_brand='Demo Brand Name-' + str(goodsbrand_data),
                                                       creater='GreaterWMS-DemoData'
                                                       )
                                goodsbrand_data_list.append(demo_data)
                            goodsbrand.objects.bulk_create(goodsbrand_data_list, batch_size=100)
                            from goodsshape.models import ListModel as goodsshape
                            demo_data = []
                            for goods_shape in randomshape:
                                demo_data.append(goodsshape(openid=transaction_code, goods_shape=goods_shape,
                                                            creater='GreaterWMS-DemoData'))
                            goodsshape.objects.bulk_create(demo_data, batch_size=100)
                            from goodsspecs.models import ListModel as goodsspecs
                            demo_data = []
                            for goods_specs in randomspecs:
                                demo_data.append(goodsspecs(openid=transaction_code, goods_specs=goods_specs,
                                                            creater='GreaterWMS-DemoData'))
                            goodsspecs.objects.bulk_create(demo_data, batch_size=100)
                            from goodsorigin.models import ListModel as goodsorigin
                            goodsorigin_data_list = []
                            for city in randomcity:
                                demo_data = goodsorigin(openid=transaction_code,
                                                        goods_origin=city,
                                                        creater='GreaterWMS-DemoData'
                                                        )
                                goodsorigin_data_list.append(demo_data)
                            goodsorigin.objects.bulk_create(goodsorigin_data_list, batch_size=100)
                            from goods.models import ListModel as goods
                            goods_data_list = []
                            for goods_data in range(1, 97):
                                goods_w = round(random.uniform(10, 1000), 2),
                                goods_d = round(random.uniform(10, 1000), 2),
                                goods_h = round(random.uniform(10, 1000), 2),
                                goods_cost = round(random.uniform(10, 1000), 2),
                                goods_price = round(random.uniform(10, 1000), 2),
                                while True:
                                    if goods_cost[0] >= goods_price[0]:
                                        goods_price = round(random.uniform(10, 1000), 2),
                                    else:
                                        break
                                demo_data = goods(openid=transaction_code,
                                                  goods_code="A0000" + str(goods_data),
                                                  goods_desc="Demo Goods Desc-" + str(goods_data),
                                                  goods_supplier='Demo Supplier Name-' + str(random.randint(1, 97)),
                                                  goods_weight=random.randint(100, 10000),
                                                  goods_w=goods_w[0],
                                                  goods_d=goods_d[0],
                                                  goods_h=goods_h[0],
                                                  unit_volume=round((int(goods_w[0]) * int(goods_d[0]) * int(goods_h[0]))/1000000000, 4),
                                                  goods_unit=random.choice(randomunit),
                                                  goods_class=random.choice(randomclass),
                                                  goods_brand='Demo Brand Name-' + str(random.randint(1, 97)),
                                                  goods_color=random.choice(randomcolor),
                                                  goods_shape=random.choice(randomshape),
                                                  goods_specs=random.choice(randomspecs),
                                                  goods_origin=random.choice(randomcity),
                                                  goods_cost=goods_cost[0],
                                                  goods_price=goods_price[0],
                                                  creater='GreaterWMS-DemoData'
                                                  )
                                goods_data_list.append(demo_data)
                            goods.objects.bulk_create(goods_data_list, batch_size=100)
                            from payment.models import TransportationFeeListModel as freight
                            freight_data_list = []
                            for sender in randomcity:
                                for receiver in randomcity:
                                    demo_data = freight(openid=transaction_code,
                                                        send_city=sender,
                                                        receiver_city=receiver,
                                                        weight_fee=random.randint(10, 20),
                                                        volume_fee=random.randint(100, 200),
                                                        min_payment=random.randint(250, 300),
                                                        transportation_supplier="Demo Supplier",
                                                        creater="GreaterWMS-DemoData"
                                                        )
                                    freight_data_list.append(demo_data)
                            freight.objects.bulk_create(freight_data_list, batch_size=100)
                            return JsonResponse(ret)

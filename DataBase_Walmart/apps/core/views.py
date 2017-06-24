import csv
import json
import sys
import urllib
from datetime import datetime

import requests
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from registration.forms import User

from DataBase_Walmart.apps.core.models import Items
from DataBase_Walmart.apps.core.tasks import just_print

try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode


def way_items(request):
    print('dfgfdgdfgd')
    ajax_response = {'sEcho': '', 'aaData': [], 'iTotalRecords': 0, 'iTotalDisplayRecords': 0}
    print('dfgfdgdfgd22')
    start_pos = int(request.GET['iDisplayStart'])
    print('dfgfdgdfgd33')
    end_pos = start_pos + int(request.GET['iDisplayLength'])
    print('dfgfdgdfgd44')
    # --- View contacts of login user ---
    user_contacts = Items.objects.filter(user_id=request.user.id).order_by('-id')
    print(user_contacts)

    # --- Views counts ---
    user_contacts_count = user_contacts.count()
    items = user_contacts[start_pos:end_pos]
    ajax_response['iTotalRecords'] = ajax_response['iTotalDisplayRecords'] = user_contacts_count
    print('dfgfdgdfgd66')
    # --- Getting data from base for send to front-end ---
    for item in items:
        ajax_response['aaData'].append({
            'DT_RowId': str(item.id),
            0: str(item.id),
            1: item.upc,
            2: item.image,
            3: item.name,
            4: item.brand,
            5: item.model,
            6: item.qty,
            7: item.in_stock,
            8: str(item.price),
            9: str(item.free_shipping),
            10: item.date_updated.strftime('%m/%d/%y') if item.date_updated else '',
        })
    print('dfgfdgdfgd77')
    return HttpResponse(json.dumps(ajax_response), content_type='application/json')


#API
if len(sys.argv) == 1:
    print( "Please pass the search string as a command line argument")
    exit()


my_api_key = 'jke868pu8xvfr6buv3qxyu7n'


date_time = datetime.strftime(datetime.today(), '%Y-%m-%d %H:%M:%S')


def onlinejson(request): #modal-wind
    return_dict = dict()
    data = request.POST
    upc = data.get('upc')
    print('UPC: '+upc)
    data_key = {'upc': upc, 'apiKey': my_api_key, 'format': 'json'}
    response = requests.get('http://api.walmartlabs.com/v1/items?'+urllib.parse.urlencode(data_key))
    print(response)
    if response.status_code != 200:
        return_dict = response.json()
    try:
        return_dict = response.json()
    except:
        pass

############################################

    for key in return_dict:
        for index in range(len(return_dict[key])):
            record = []

            if 'upc' in return_dict[key][index]:
                record.append(return_dict[key][index]['upc'])
            else:
                record.append('')

            if 'name' in return_dict[key][index]:
                record.append(return_dict[key][index]['name'])
            else:
                record.append('')

            if 'brandName' in return_dict[key][index]:
                record.append(return_dict[key][index]['brandName'])
            else:
                record.append('')

            if 'modelNumber' in return_dict[key][index]:
                record.append(return_dict[key][index]['modelNumber'])
            else:
                record.append('')

            if 'msrp' in return_dict[key][index]:
                record.append(str('%.2f' % float(return_dict[key][index]['msrp'])))
            else:
                record.append(0.00)

            if 'freeShipToStore' in return_dict[key][index]:
                record.append(str(return_dict[key][index]['freeShipToStore']))
            else:
                record.append('')

            if 'stock' in return_dict[key][index]:
                record.append(return_dict[key][index]['stock'])
            else:
                record.append('')

            if 'mediumImage' in return_dict[key][index]:
                record.append(return_dict[key][index]['mediumImage'])
            else:
                record.append('')

            if 'shipToStore' in return_dict[key][index]:
                record.append(str(return_dict[key][index]['shipToStore']))
            else:
                record.append('')

            record.append(date_time)
            print(record)
            print(record[1], type)


    ###########################################

            try:
                print(0, record[0])
                print(1, record[1])
                print(2, record[2])
                print(3, record[3])
                print(4, record[4])
                print(5, record[5])
                print(6, record[6])
                print(7, record[7])
                print(8, record[8])
                print(9, record[9])

                Items.objects.get_or_create(upc=record[0],
                                            image=record[7],
                                            name=record[1],
                                            brand=record[2],
                                            model=record[3],
                                            qty='1',
                                            in_stock=record[6],
                                            price=record[4],
                                            free_shipping='1',
                                            date_updated='2017-06-24',
                                            user_id=request.user.id)

            except Exception:
                print('error1544')
            else:
                print('OKI')

        return JsonResponse(return_dict)



def delete_items(request):
    return_dict = dict()
    # return_dict["my_variable"] = '45'
    print("request ")
    if request.is_ajax():
        print("request is ajax")
        id_item = request.POST
        val_item = id_item.get("id")
        print(val_item)
        return_dict["variable"] = '45'
        Items.objects.get(id=val_item).delete()

        return JsonResponse(return_dict)

"""CSV-files"""


@csrf_exempt
def data_import(request):
    if request.method == 'POST':
        print(request.FILES)
        csv_file = request.FILES['data_input_file']
        print(csv_file, 111)
        fs = FileSystemStorage()

        fs.save('temp_import.csv', csv_file)
        csv_data = fs.open('temp_import.csv', mode='r')
        count = -1
        print(csv_data, 222)

        for record in csv_data:
            count = count + 1
            record = record.split(',')
            if record[0] == 'ID':
                continue
            print(record)
            print(0, record[0])
            print(1, record[1])
            print(2, record[2])
            print(3, record[3])
            print(4, record[4])
            print(5, record[5])
            print(6, record[6])
            print(7, record[7])
            print(8, record[8])
            print(9, record[9])

            Items.objects.get_or_create(upc=record[1], image=record[2], name=record[3], brand=record[4],
                                        model=record[5],
                                        qty='1', in_stock=record[7], price=record[8], free_shipping=True,
                                        date_updated='2017-01-01',
                                        user_id=request.user.id)

        fs.delete('temp_import.csv')
        print('count: '+str(count))
        return HttpResponseRedirect('/')

    else:
        return HttpResponse(json.dumps({'error': 'Something wrong'}))

def csv_list(request):
    all = list()
    user_contacts = Items.objects.filter(user_id=request.user.id)
    for user_contact in user_contacts:

        data = [user_contact.id, user_contact.upc, user_contact.image, user_contact.name, user_contact.brand, user_contact.model, user_contact.qty, user_contact.in_stock, user_contact.price, user_contact.free_shipping, user_contact.date_updated]
        all.append(data)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

    writer = csv.writer(response)
    for item in all:
        writer.writerow(item)
        print(item)

    print(response)
    return response


class UserListView(ListView):
    model = User

    def get_context_data(self, **kwargs):
        just_print.delay()
        return super(UserListView, self).get_context_data(**kwargs)





import json
from    .models import Position
from django.apps import apps

#This is used by the data fetching class in apis.py to conver the data to required keys before
#storing it or further processing it
def modelFilter(model, jsondata):
     app_config =  apps.get_app_config('fnoappbe')
     usecaseslist = app_config.usecaseslist
      
     if (model == usecaseslist['trades']):
        #data_dict = json.loads(jsondata)
        data_dict = jsondata
        # Get the field names from the model
        model_fields = [field.name for field in Position._meta.get_fields()]
        print(model_fields )
        print(data_dict['data'])
        # Filter the dictionary to keep only the relevant keys
        filtered_array = []
        for data in data_dict['data']:
            filtered_data = {k: v for k, v in data.items() if k in model_fields}
            filtered_array.append(filtered_data)

        #filtered_data = {k: v for k, v in data_dict['data'].items() if k in model_fields}
        print(json.dumps(filtered_array))
        return {'Data': filtered_array}
     return jsondata



    
    
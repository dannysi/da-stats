# impor
    
import deviantart
import datetime


da = deviantart.Api("", "")

#fetch daily deviations
dailydeviations = da.browse_dailydeviations()

try:  
    da.auth(code='')
except deviantart.api.DeviantartError as e:
    print("Couldn't authorize user. Error: {}".format(e))

    
all_deviations = []
cont = True
offset = 0
while cont:
    response = da.get_gallery_folder(username="dannysi", folderid="44E813DC-1640-BCAD-33BC-72709A5878A0", offset=offset)
    all_deviations += response["results"]
    cont = response['has_more']
    offset=response['next_offset']
    print('len:', len(all_deviations))    
print(all_deviations)
print(len(all_deviations))


deviation = da.get_deviation("34A55E88-C354-7EF6-4D56-6B528544B4FE")

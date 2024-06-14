from django.shortcuts import render, get_object_or_404
from .models import Truck, Warehouse
from .forms import UnloadCoordinatesForm
from shapely.geometry import Point, Polygon, LineString
from shapely import wkt


def check_point_in_polygon(point, polygon):
    return polygon.contains(point)


def table_view(request):
    trucks = Truck.objects.all()
    warehouse = get_object_or_404(Warehouse, id=1)

    polygon = wkt.loads(warehouse.polygon)

    if request.method == 'POST':

        for i in range(len(request.POST.getlist('truck_id'))):
            form_data = {'csrfmiddlewaretoken': request.POST['csrfmiddlewaretoken'][0],
                         'truck_id': request.POST.getlist('truck_id')[i],
                         'unload_coordinates': request.POST.getlist('unload_coordinates')[i]}

            form = UnloadCoordinatesForm(form_data)

            if form.is_valid():

                truck_id = form.cleaned_data['truck_id']
                coordinates = form.cleaned_data['unload_coordinates']
                truck = trucks.get(pk=truck_id)
                coords = coordinates.split()
                point = Point(float(coords[0]), float(coords[1]))

                if check_point_in_polygon(point, polygon):
                    weight_before = warehouse.volume_before_unload
                    warehouse.volume_before_unload = warehouse.volume_after_unload
                    warehouse.volume_after_unload += truck.current_load

                    sio2_after = warehouse.sio2_percentage_after
                    warehouse.sio2_percentage_after = round(
                        (((weight_before * (warehouse.sio2_percentage_before / 100)) +
                          (truck.current_load * (truck.sio2_percentage / 100)))
                         / warehouse.volume_after_unload) * 100, 1)
                    warehouse.sio2_percentage_before = sio2_after

                    fe_after = warehouse.fe_percentage_after
                    warehouse.fe_percentage_after = round((((weight_before * (warehouse.fe_percentage_before / 100)) +
                                                            (truck.current_load * (truck.fe_percentage / 100)))
                                                           / warehouse.volume_after_unload) * 100, 1)
                    warehouse.sio2_percentage_before = sio2_after

                    warehouse.save()


    else:
        form = UnloadCoordinatesForm()

    return render(request, 'warehouse/tables.html', {
        'trucks': trucks,
        'warehouse': warehouse,
        'form': form
    })

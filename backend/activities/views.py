from rest_framework import generics

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy, reverse

import pandas as pd
from dateutil import parser

from .forms import UploadFileForm
from .models import Activity
from .permissions import IsAuthorOrReadOnly
from .serializers import ActivitySerializer


RENAME_DICT = {
    'Activity ID': 'upload_id',
    'Activity Date': 'date',
    'Activity Name': 'name',
    'Activity Type': 'activity_type',
    'Activity Description': 'description',
    'Elapsed Time': 'elapsed_time',
    'Distance': 'distance',
    'Relative Effort': 'relative_effort',
    'Commute': 'commute',
    'Activity Gear': 'gear',
    'Filename': 'filename',
    'Athlete Weight': 'athlete_weight',
    'Bike Weight': 'bike_weight',
    'Elapsed Time': 'elapsed_time',
    'Moving Time': 'moving_time',
    'Distance': 'distance',
    'Max Speed': 'max_speed',
    'Average Speed': 'average_speed',
    'Elevation Gain': 'elevation_gain',
    'Elevation Loss': 'elevation_loss',
    'Elevation Low': 'elevation_low',
    'Elevation High': 'elevation_high',
    'Max Grade': 'max_grade',
    'Average Grade': 'average_grade',
    'Average Positive Grade': 'average_positive_grade',
    'Average Negative Grade': 'average_negative_grade',
    'Average Cadence': 'average_cadence',
    'Max Cadence': 'max_cadence',
    'Max Heart Rate': 'max_heart_rate',
    'Average Heart Rate': 'average_heart_rate',
    'Max Watts': 'max_watts',
    'Average Watts': 'average_watts',
    'Calories': 'calories',
    'Max Temperature': 'max_temperature',
    'Average Temperature': 'average_temperature',
    'Total Work': 'total_work',
    'Number of Runs': 'number_of_runs',
    'Uphill Time': 'uphill_time',
    'Downhill Time': 'downhill_time',
    'Other Time': 'other_time',
    'Perceived Exertion': 'perceived_exertion',
    'Weighted Average Power': 'weighted_average_power'}


class ActivityList(generics.ListCreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class ActivityDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


def without_keys(d, keys):
    return {k: v for k, v in d.items() if k not in keys}


def upload_from_csv(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                csv_file = request.FILES['file']
                data = pd.read_csv(csv_file)
                data = data.loc[:, ~data.columns.duplicated()]
                data = data.rename(
                    columns=RENAME_DICT)
                for col in data.columns:
                    if col not in RENAME_DICT.values():
                        del data[col]

                data['date'] = data['date'].apply(parser.parse)
                data['user'] = request.user

                data = data.where(data.notnull(), None)

                for record in data.to_dict('records'):
                    try:
                        obj, created = Activity.objects.update_or_create(
                            defaults=without_keys(record, {'upload_id'}), **{'upload_id': record['upload_id']})

                        print(obj, "detected, created:", created)
                    except Exception as error:
                        messages.error(
                            request, "Could not import activity. " + repr(error))

            except Exception as e:
                messages.error(request, "Unable to upload file. " + repr(e))
                print(repr(e))

            return redirect('activities_bulk_upload')
    else:
        form = UploadFileForm()

    return render(request, 'activities/activities_bulk_upload.html', {'form': form})

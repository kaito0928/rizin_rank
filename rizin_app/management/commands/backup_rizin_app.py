import csv
import datetime
import os

from django.conf import settings
from django.core.management.base import BaseCommand

from ...models import BantamRank,FeatherRank


class Command(BaseCommand):
    help = 'Backup rizin_app data'

    def handle(self,*args,**options):
        date = datetime.date.today().strftime("%Y%m%d")

        file_path = settings.BACKUP_PATH + 'rizin_app_' + date + '.csv'

        os.makedirs(settings.BACKUP_PATH,exist_ok=True)

        with open(file_path,'w') as file:
            writer = csv.writer(file)

            bantam_header = [field.name for field in BantamRank._meta.fields]
            writer.writerow(bantam_header)

            bantamranks = BantamRank.objects.all()

            for bantamrank in bantamranks:
                writer.writerow([str(bantamrank.user),
                                 bantamrank.one,
                                 bantamrank.two,
                                 bantamrank.three,
                                 bantamrank.four,
                                 bantamrank.five,
                                 bantamrank.six,
                                 bantamrank.seven,
                                 bantamrank.eight,
                                 bantamrank.nine,
                                 bantamrank.ten,
                                 str(bantamrank.created_at)])

            files = os.listdir(settings.BACKUP_PATH)

            if len(files) >= settings.NUM_SAVED_BACKUP:
                files.sort()
                os.remove(settings.BACKUP_PATH + files[0])


            feather_header = [field.name for field in FeatherRank._meta.fields]
            writer.writerow(feather_header)

            featherranks = FeatherRank.objects.all()

            for featherrank in featherranks:
                writer.writerow([str(featherrank.user),
                                 featherrank.one,
                                 featherrank.two,
                                 featherrank.three,
                                 featherrank.four,
                                 featherrank.five,
                                 featherrank.six,
                                 featherrank.seven,
                                 featherrank.eight,
                                 featherrank.nine,
                                 featherrank.ten,
                                 str(featherrank.created_at)])

            files = os.listdir(settings.BACKUP_PATH)

            if len(files) >= settings.NUM_SAVED_BACKUP:
                files.sort()
                os.remove(settings.BACKUP_PATH + files[0])

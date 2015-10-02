from django.core.management.base import BaseCommand
from django.core.management.base import CommandError
from cornerstone.models import CornerstoneUserProfile
import  csv
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Command(BaseCommand):
    args = BASE_DIR  + "/data/CSOD_Users.csv"
    help = "Imports movies from a local CSV file."
    def handle(self, *args, **options):
        if args:
            file_path = args[0]
        else:
            raise CommandError("Pass a path to a CSV file")
            print "=== csv file imported ==="

        with open(file_path) as f:
            rows = csv.reader(f)
            for row in rows:
                if rows.line_num == 1:
                    continue
                print "GUID: " + row[0]
                print "User_ID: " + row[1]
                print "First_Name: " + row[2]
                print "Last_Name: " + row[3]
                print "Manager_ID"  + row[4]
                csv_created = CornerstoneUserProfile.objects.create(GUID = row[0], User_ID = row[1], First_Name = row[2], Last_Name = row[3], Manager_ID = row[4])
                csv_created.save()
                print csv_created
                print "Users created Successfully"

                #Adding parent
                print "Updating Parent"
                for row in rows:
                    try:
                        print"hello"
                        user = CornerstoneUserProfile.objects.get(user_ID = row[1])
                        print user
                        parent = CornerstoneUserProfile.objects.get(user_ID = row[4])
                        user.parent = parent

                        user.save()
                    except:
                        pass
                print "parent updated Successfully"